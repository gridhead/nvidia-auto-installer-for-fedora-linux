"""
##########################################################################
*
*   Copyright © 2019-2021 Akashdeep Dhar <t0xic0der@fedoraproject.org>
*
*   This program is free software: you can redistribute it and/or modify
*   it under the terms of the GNU General Public License as published by
*   the Free Software Foundation, either version 3 of the License, or
*   (at your option) any later version.
*
*   This program is distributed in the hope that it will be useful,
*   but WITHOUT ANY WARRANTY; without even the implied warranty of
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*   GNU General Public License for more details.
*
*   You should have received a copy of the GNU General Public License
*   along with this program.  If not, see <https://www.gnu.org/licenses/>.
*
##########################################################################
"""

import os
import sys
from dataclasses import dataclass
from typing import Any
from nvautoinstall.functions.rpmf_handler import CollRPMFHandler
from nvautoinstall.functions.support_check import CollSupportCheck
from nvautoinstall.functions.status_decorator import DecoratorObject
from nvautoinstall.functions.installer_functions import (
    CollDriverInstaller,
    CollFFMPEGInstaller,
    CollPlCudaInstaller,
    CollVidAccInstaller,
    CollVulkanInstaller,
    CollX86LibInstaller,
)
from nvautoinstall.handler.messages import nv_msgs
import click


try:
    # Imports version in the packaged environment
    from nvautoinstall import __version__, __author__
except ModuleNotFoundError:
    # Imports version in the development environment
    from __init__ import __version__, __author__


class CollSuperuserCheck(object):
    @staticmethod
    def main():
        return os.geteuid() == 0


@dataclass
class CollPrimeSupportEnabler(object):
    @staticmethod
    def main(opts):
        try:
            with open("/usr/share/X11/xorg.conf.d/nvidia.conf", "r") as sharconf:
                shardata = sharconf.read()
            primemod = ""
            for indx in shardata.split("\n"):
                primemod += indx + "\n"
                if opts is True and indx == '\tOption "BaseMosaic" "on"':
                    primemod += '\tOption "PrimaryGPU" "yes"' + "\n"
            with open("/etc/X11/xorg.conf.d/nvidia.conf", "w") as etcdconf:
                etcdconf.write(primemod)
            return True
        except Exception:
            return False


SupportCheck: CollSupportCheck = CollSupportCheck()
RPMFHandler: CollRPMFHandler = CollRPMFHandler()
DriverInstaller: CollDriverInstaller = CollDriverInstaller()
x86LibInstaller: CollX86LibInstaller = CollX86LibInstaller()
PlCudaInstaller: CollPlCudaInstaller = CollPlCudaInstaller()
FFMPEGInstaller: CollFFMPEGInstaller = CollFFMPEGInstaller()
VidAccInstaller: CollVidAccInstaller = CollVidAccInstaller()
VulkanInstaller: CollVulkanInstaller = CollVulkanInstaller()
SuperuserCheck: CollSuperuserCheck = CollSuperuserCheck()
PrimeSupportEnabler: CollPrimeSupportEnabler = CollPrimeSupportEnabler()


@dataclass
class InstallationMode(object):
    def __init__(self):
        self.menudict = {
            "--rpmadd ": "This mode enables the RPM Fusion NVIDIA drivers repository.",
            "--driver ": "This mode simply installs the NVIDIA driver.",
            "--x86lib ": "This mode installs only the x86 libraries for Xorg.",
            "--nvrepo ": "This mode enables the Official NVIDIA repository for CUDA.",
            "--plcuda ": "This mode installs only the CUDA support softwares.",
            "--ffmpeg ": "This mode installs only the FFMPEG acceleration.",
            "--vulkan ": "This mode installs only the Vulkan renderer.",
            "--vidacc ": "This mode installs only the VDPAU/VAAPI acceleration.",
            "--getall ": "This mode installs all the above packages.",
            "--checksu ": "This mode allows you to check the user privilege level.",
            "--compat ": "This mode allows you to check your compatibility.",
            "--primec ": "This mode allows you to setup PRIME configuration.",
            "--version": "Show the version and exit.",
            "--help   ": "Show this message and exit.",
        }

    @staticmethod
    def rpmadd():
        if RPMFHandler.avbl():
            DecoratorObject.send_message("WARN", nv_msgs.get("nvidia_driver_detected"))
            DecoratorObject.send_message("PASS", nv_msgs.get("no_further_action"))
        else:
            DecoratorObject.send_message("WARN", nv_msgs.get("nvidia_driver_not_detected"))
            DecoratorObject.send_message("WARN", nv_msgs.get("repository_enabling_is_required"))
            if RPMFHandler.conn():
                DecoratorObject.send_message("PASS", nv_msgs.get("connection_to_rpm_server_established"))
                DecoratorObject.send_message("HEAD", nv_msgs.get("installing_nvidia_repository"), "magenta", True)
                if RPMFHandler.rpmf_repo_install():
                    DecoratorObject.send_message("PASS", nv_msgs.get("nvidia_repository_enabled"))
                else:
                    DecoratorObject.send_message("FAIL", nv_msgs.get("nvidia_repository_not_enabled"))
            else:
                DecoratorObject.send_message("FAIL", nv_msgs.get("connection_to_rpm_server_not_established"))

        DecoratorObject.send_message("FAIL", nv_msgs.get(nv_msgs.get("Leaving installer")))
        sys.exit(0)

    @staticmethod
    def driver():

        if RPMFHandler.avbl():
            DecoratorObject.send_message("WARN", nv_msgs.get("nvidia_driver_detected"))
            if RPMFHandler.conn():
                DecoratorObject.send_message("PASS", nv_msgs.get("connection_to_rpm_server_established"))
                if data := DriverInstaller.avbl() is False:
                    DecoratorObject.send_message("WARN", nv_msgs.get("no_existing_nvidia_driver_detected"))
                    DecoratorObject.send_message("HEAD", nv_msgs.get("installing_proprietary_drivers"), "magenta", True)
                else:
                    qant = 0
                    for indx in data:
                        if indx != "":
                            qant += 1
                            DecoratorObject.send_message("STDS", indx)
                    DecoratorObject.send_message("WARN", "A total of " + str(qant) + " driver packages were detected")
                    DecoratorObject.send_message("HEAD", nv_msgs.get("installing_proprietary_drivers"), "magenta", True)
                if DriverInstaller.main():
                    DecoratorObject.send_message("PASS", nv_msgs.get("driver_instalation_completed"))
                else:
                    DecoratorObject.send_message("FAIL", nv_msgs.get("proprietart_drivers_not_installed"))
            else:
                DecoratorObject.send_message("FAIL", nv_msgs.get("connection_to_rpm_server_not_established"))
        else:
            DecoratorObject.send_message("FAIL", nv_msgs.get("nvidia_driver_not_detected"))
        DecoratorObject.send_message("FAIL", nv_msgs.get(nv_msgs.get("Leaving installer")))
        sys.exit(0)

    @staticmethod
    def x86lib():
        if RPMFHandler.avbl():
            DecoratorObject.send_message("WARN", nv_msgs.get("nvidia_driver_detected"))
            if RPMFHandler.conn():
                DecoratorObject.send_message("PASS", nv_msgs.get("connection_to_rpm_server_established"))
                data = DriverInstaller.avbl()
                if data is False:
                    DecoratorObject.send_message("FAIL", nv_msgs.get("no_existing_nvidia_driver_detected"))
                else:
                    qant = 0
                    for indx in data:
                        if indx != "":
                            qant += 1
                            DecoratorObject.send_message("STDS", indx)
                    DecoratorObject.send_message("WARN", "A total of " + str(qant) + " driver packages were detected")
                    DecoratorObject.send_message("HEAD", nv_msgs.get("installing_x86_libraries_for_xorg"), "magenta", True)
                    if x86LibInstaller.main():
                        DecoratorObject.send_message("PASS", nv_msgs.get("x86_libraries_installed"))
                    else:
                        DecoratorObject.send_message("FAIL", nv_msgs.get("x86_libraries_not_installed"))
            else:
                DecoratorObject.send_message("FAIL", nv_msgs.get("connection_to_rpm_server_not_established"))
        else:
            DecoratorObject.send_message("FAIL", nv_msgs.get("nvidia_driver_not_detected"))
        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    @staticmethod
    def nvrepo():
        DecoratorObject.send_message("HEAD", nv_msgs.get("checking_availability_cudo_repository"), "magenta", True)
        if PlCudaInstaller.rpck():
            DecoratorObject.send_message("WARN", nv_msgs.get("cudo_repository_detected"))
            DecoratorObject.send_message("PASS", nv_msgs.get("no_further_action"))
        else:
            DecoratorObject.send_message("WARN", "Official CUDA repository was not detected")
            DecoratorObject.send_message("WARN", nv_msgs.get("repository_enabling_is_required"))
            DecoratorObject.send_message("HEAD", "ATTEMPTING CONNECTION TO NVIDIA SERVERS...", "magenta", True)
            if PlCudaInstaller.conn():
                DecoratorObject.send_message("PASS", "Connection to NVIDIA servers was established")
                DecoratorObject.send_message("HEAD", "INSTALLING OFFICIAL CUDA REPOSITORY...", "magenta", True)
                if PlCudaInstaller.rpin():
                    DecoratorObject.send_message("PASS", "Official CUDA repository was enabled")
                    DecoratorObject.send_message("HEAD", "REFRESHING REPOSITORY LIST...", "magenta", True)
                    if PlCudaInstaller.rpup():
                        DecoratorObject.send_message("PASS", "Repositories have been refreshed")
                        DecoratorObject.send_message("HEAD", "DISABLING NVIDIA DRIVER MODULE...", "magenta", True)
                        if PlCudaInstaller.stop():
                            DecoratorObject.send_message("PASS", "NVIDIA DRIVER module has been disabled")
                        else:
                            DecoratorObject.send_message("FAIL", "NVIDIA DRIVER module could not be disabled")
                    else:
                        DecoratorObject.send_message("FAIL", "Repositories could not be refreshed")
                else:
                    DecoratorObject.send_message("FAIL", "Official CUDA repository could not be enabled")
            else:
                DecoratorObject.send_message("FAIL", "Connection to NVIDIA servers could not be established")
        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    @staticmethod
    def plcuda():
        if RPMFHandler.avbl():
            DecoratorObject.send_message("WARN", nv_msgs.get("nvidia_driver_detected"))
            if RPMFHandler.conn():
                DecoratorObject.send_message("PASS", nv_msgs.get("connection_to_rpm_server_established"))
                if data := DriverInstaller.avbl() is False:
                    DecoratorObject.send_message("FAIL", nv_msgs.get("no_existing_nvidia_driver_detected"))
                else:
                    qant = 0
                    for indx in data:
                        if indx != "":
                            qant += 1
                            DecoratorObject.send_message("STDS", indx)
                    DecoratorObject.send_message("WARN", "A total of " + str(qant) + " driver packages were detected")
                    DecoratorObject.send_message("HEAD", nv_msgs.get("checking_availability_cudo_repository"), "magenta", True)
                    if PlCudaInstaller.rpck():
                        DecoratorObject.send_message("WARN", nv_msgs.get("cudo_repository_detected"))
                        DecoratorObject.send_message("HEAD", "ATTEMPTING CONNECTION TO NVIDIA SERVERS...", "magenta", True)
                        if PlCudaInstaller.conn():
                            DecoratorObject.send_message("PASS", "Connection to NVIDIA servers was established")
                            DecoratorObject.send_message("HEAD", "INSTALLING RPM FUSION METAPACKAGE FOR CUDA...", "magenta", True)
                            if PlCudaInstaller.meta():
                                DecoratorObject.send_message("PASS", "RPM Fusion CUDA metapackage was successfully installed")
                                DecoratorObject.send_message("HEAD", "INSTALLING NVIDIA CUDA CORE PACKAGES...", "magenta", True)
                                if PlCudaInstaller.main():
                                    DecoratorObject.send_message(
                                        "PASS",
                                        "NVIDIA CUDA core packages were successfully installed",
                                    )
                                else:
                                    DecoratorObject.send_message("FAIL", "NVIDIA CUDA core packages could not be installed")
                            else:
                                DecoratorObject.send_message(
                                    "FAIL",
                                    "RPM Fusion CUDA metapackage packages could not be installed",
                                )
                        else:
                            DecoratorObject.send_message("FAIL", "Connection to NVIDIA servers could not be established")
                    else:
                        DecoratorObject.send_message("FAIL", "Official CUDA repository was not detected")
            else:
                DecoratorObject.send_message("FAIL", nv_msgs.get("connection_to_rpm_server_not_established"))
        else:
            DecoratorObject.send_message("FAIL", nv_msgs.get("nvidia_driver_not_detected"))

        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    @staticmethod
    def ffmpeg():
        DecoratorObject.send_message("HEAD", "CHECKING SUPERUSER PERMISSIONS...", "magenta", True)
        if SuperuserCheck.main():
            DecoratorObject.send_message("PASS", "Superuser privilege acquired")
            if RPMFHandler.avbl():
                DecoratorObject.send_message("WARN", nv_msgs.get("nvidia_driver_detected"))
                if RPMFHandler.conn():
                    DecoratorObject.send_message("PASS", nv_msgs.get("connection_to_rpm_server_established"))

                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.send_message("FAIL", nv_msgs.get("no_existing_nvidia_driver_detected"))
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.send_message("STDS", indx)
                        DecoratorObject.send_message("WARN", "A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.send_message("HEAD", "INSTALLING NVENC/NVDEC FOR FFMPEG ACCELERATION...", "magenta", True)
                        if FFMPEGInstaller.main():
                            DecoratorObject.send_message("PASS", "NVENC/NVDEC for FFMPEG acceleration were successfully installed")
                        else:
                            DecoratorObject.send_message("FAIL", "NVENC/NVDEC for FFMPEG acceleration could not be installed")
                else:
                    DecoratorObject.send_message("FAIL", nv_msgs.get("connection_to_rpm_server_not_established"))
            else:
                DecoratorObject.send_message("FAIL", nv_msgs.get("nvidia_driver_not_detected"))
        else:
            DecoratorObject.send_message("FAIL", "Superuser privilege could not be acquired")
        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    @staticmethod
    def vulkan():
        if RPMFHandler.avbl():
            DecoratorObject.send_message("WARN", nv_msgs.get("nvidia_driver_detected"))
            if RPMFHandler.conn():
                DecoratorObject.send_message("PASS", nv_msgs.get("connection_to_rpm_server_established"))
                data = DriverInstaller.avbl()
                if data is False:
                    DecoratorObject.send_message("FAIL", nv_msgs.get("no_existing_nvidia_driver_detected"))
                else:
                    qant = 0
                    for indx in data:
                        if indx != "":
                            qant += 1
                            DecoratorObject.send_message("STDS", indx)
                    DecoratorObject.send_message("WARN", "A total of " + str(qant) + " driver packages were detected")
                    DecoratorObject.send_message("HEAD", "INSTALLING VULKAN RENDERER SUPPORT...", "magenta", True)
                    if VulkanInstaller.main():
                        DecoratorObject.send_message("PASS", "Vulkan renderer support were successfully installed")
                    else:
                        DecoratorObject.send_message("FAIL", "Vulkan renderer support could not be installed")
            else:
                DecoratorObject.send_message("FAIL", nv_msgs.get("connection_to_rpm_server_not_established"))
        else:
            DecoratorObject.send_message("FAIL", nv_msgs.get("nvidia_driver_not_detected"))

        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    @staticmethod
    def vidacc():
        if RPMFHandler.avbl():
            DecoratorObject.send_message("WARN", nv_msgs.get("nvidia_driver_detected"))
            if RPMFHandler.conn():
                DecoratorObject.send_message("PASS", nv_msgs.get("connection_to_rpm_server_established"))
                data = DriverInstaller.avbl()
                if data is False:
                    DecoratorObject.send_message("FAIL", nv_msgs.get("no_existing_nvidia_driver_detected"))
                else:
                    qant = 0
                    for indx in data:
                        if indx != "":
                            qant += 1
                            DecoratorObject.send_message("STDS", indx)
                    DecoratorObject.send_message("WARN", "A total of " + str(qant) + " driver packages were detected")
                    DecoratorObject.send_message("HEAD", "INSTALLING VIDEO ACCELERATION SUPPORT...", "magenta", True)
                    if VidAccInstaller.main():
                        DecoratorObject.send_message("PASS", "Video acceleration were successfully installed")
                    else:
                        DecoratorObject.send_message("FAIL", "Video acceleration could not be installed")
            else:
                DecoratorObject.send_message("FAIL", nv_msgs.get("connection_to_rpm_server_not_established"))
        else:
            DecoratorObject.send_message("FAIL", nv_msgs.get("nvidia_driver_not_detected"))
        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    @staticmethod
    def getall():
        DecoratorObject.send_message("HEAD", "CHECKING SUPERUSER PERMISSIONS...", "magenta", True)
        if SuperuserCheck.main():
            DecoratorObject.send_message("PASS", "Superuser privilege acquired")
            DecoratorObject.send_message("HEAD", "FULL FLEDGED INSTALLATION BEGINNING...", "magenta", True)
            DecoratorObject.send_message("STDS", "This mode is yet to be implemented")
        else:
            DecoratorObject.send_message("FAIL", "Superuser privilege could not be acquired")
        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    @staticmethod
    def checksu():
        DecoratorObject.send_message("HEAD", "CHECKING SUPERUSER PERMISSIONS...", "magenta", True)
        if SuperuserCheck.main():
            DecoratorObject.send_message("PASS", "Superuser permission is available")
            DecoratorObject.send_message("STDS", "This tool is expected to work correctly here")
        else:
            DecoratorObject.send_message("FAIL", "Superuser permission is not available")
            DecoratorObject.send_message("STDS", "This tool cannot be used here")
        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    @staticmethod
    def compat():
        DecoratorObject.send_message("HEAD", "CHECKING FOR GPU COMPATIBILITY...", "magenta", True)
        data = SupportCheck.gpuc()
        DecoratorObject.send_message("WARN", "Compatibility infomation was obtained")
        if data is False:
            DecoratorObject.send_message("FAIL", "No supported NVIDIA GPU was detected")
        else:
            DecoratorObject.send_message("PASS", "One or more active NVIDIA GPUs were detected")
            supprt = data["supprt"]
            gpulst = data["gpulst"]
            for indx in gpulst:
                if indx != "":
                    DecoratorObject.send_message("STDS", indx)
            if supprt == "single":
                DecoratorObject.send_message("PASS", "An single dedicated GPU setup was detected")
            else:
                DecoratorObject.send_message("PASS", "An Optimus Dual GPU setup was detected")
            DecoratorObject.send_message("HEAD", "GATHERING CURRENT HOST INFORMATION...", "magenta", True)
            data = SupportCheck.main()
            DecoratorObject.send_message("WARN", "Host information was gathered")
            for indx in data.keys():
                DecoratorObject.send_message("STDS", indx + ": " + data[indx])
            DecoratorObject.send_message("HEAD", "CHECKING FOR HOST COMPATIBILITY...", "magenta", True)
            if data := SupportCheck.avbl() is False:
                DecoratorObject.send_message("FAIL", "Unsupported OS detected")
                DecoratorObject.send_message("STDS", "This tool cannot be used here")
            else:
                if data == "full":
                    DecoratorObject.send_message("PASS", "Supported OS detected")
                    DecoratorObject.send_message("STDS", "This tool is expected to work correctly here")
                elif data == "half":
                    DecoratorObject.send_message("WARN", "Minimally supported OS detected")
                    DecoratorObject.send_message("STDS", "Discretion is advised while using this tool")
        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    @staticmethod
    def primec():
        if RPMFHandler.avbl():
            DecoratorObject.send_message("WARN", nv_msgs.get("nvidia_driver_detected"))
            if RPMFHandler.conn():
                DecoratorObject.send_message("PASS", nv_msgs.get("connection_to_rpm_server_established"))
                data = DriverInstaller.avbl()
                if data is False:
                    DecoratorObject.send_message("FAIL", nv_msgs.get("no_existing_nvidia_driver_detected"))
                else:
                    qant = 0
                    for indx in data:
                        if indx != "":
                            qant += 1
                            DecoratorObject.send_message("STDS", indx)
                    DecoratorObject.send_message("WARN", "A total of " + str(qant) + " driver packages were detected")
                    DecoratorObject.send_message("HEAD", "SETTING UP PRIME SUPPORT...", "magenta", True)
                    DecoratorObject.send_message("WARN", "Intervention required")
                    DecoratorObject.send_message("STDS", click.style("< Y >", fg="green", bold=True) + " to enable PRIME support")
                    DecoratorObject.send_message("STDS", click.style("< N >", fg="red", bold=True) + " to disable PRIME support")
                    DecoratorObject.send_message("STDS", click.style("< * >", fg="yellow", bold=True) + " anything else to leave")
                    solution = input("[Y/N] ")
                    if solution.upper() == "Y":
                        DecoratorObject.send_message("HEAD", "ENABLING PRIME SUPPORT...", "magenta", True)
                        if PrimeSupportEnabler.main(True):
                            DecoratorObject.send_message("PASS", "PRIME Support was successfully enabled")
                        else:
                            DecoratorObject.send_message("FAIL", "PRIME Support could not be enabled")
                    elif solution.upper() == "N":
                        DecoratorObject.send_message("HEAD", "DISABLING PRIME SUPPORT...", "magenta", True)
                        if PrimeSupportEnabler.main(False):
                            DecoratorObject.send_message("PASS", "PRIME Support was successfully disabled")
                        else:
                            DecoratorObject.send_message("FAIL", "PRIME Support could not be disabled")
                    else:
                        DecoratorObject.send_message("HEAD", "SAFE AND GOOD ANSWER...", "magenta", True)
            else:
                DecoratorObject.send_message("FAIL", nv_msgs.get("connection_to_rpm_server_not_established"))
        else:
            DecoratorObject.send_message("FAIL", nv_msgs.get("nvidia_driver_not_detected"))
        DecoratorObject.send_message("FAIL", nv_msgs.get("Leaving installer"))
        sys.exit(0)

    def lsmenu(self):
        DecoratorObject.send_message("HEAD", "OPTIONS", "magenta", True)
        for indx in self.menudict.keys():
            DecoratorObject.send_message("STDS", click.style(indx, fg="green", bold=True) + "  " + self.menudict[indx])
        sys.exit(0)


@click.command()
@click.option("--rpmadd", "instmode", flag_value="rpmadd", help="This mode enables the RPM Fusion NVIDIA drivers repository.")
@click.option("--driver", "instmode", flag_value="driver", help="This mode simply installs the NVIDIA driver.")
@click.option("--x86lib", "instmode", flag_value="x86lib", help="This mode installs only the x86 libraries for Xorg.")
@click.option("--nvrepo", "instmode", flag_value="nvrepo", help="This mode enables the Official NVIDIA repository for CUDA.")
@click.option("--plcuda", "instmode", flag_value="plcuda", help="This mode installs only the CUDA support softwares.")
@click.option("--ffmpeg", "instmode", flag_value="ffmpeg", help="This mode installs only the FFMPEG acceleration.")
@click.option("--vulkan", "instmode", flag_value="vulkan", help="This mode installs only the Vulkan renderer.")
@click.option("--vidacc", "instmode", flag_value="vidacc", help="This mode installs only the VDPAU/VAAPI acceleration.")
@click.option("--getall", "instmode", flag_value="getall", help="This mode installs all the above packages.")
@click.option("--checksu", "instmode", flag_value="checksu", help="This mode allows you to check the user privilege level.")
@click.option("--compat", "instmode", flag_value="compat", help="This mode allows you to check your compatibility.")
@click.option("--primec", "instmode", flag_value="primec", help="This mode allows you to setup PRIME configuration.")
@click.version_option(
    version=__version__,
    prog_name=click.style(__author__, fg="green", bold=True),
)
def main(instmode):
    DecoratorObject.send_message("HEAD", "CHECKING SUPERUSER PERMISSIONS...", "magenta", True)
    if SuperuserCheck.main():
        DecoratorObject.send_message("PASS", "Superuser privilege acquired")
    else:
        DecoratorObject.send_message("FAIL", "Superuser privilege could not be acquired")

    instobjc = InstallationMode()
    click.echo(click.style("[ # ] NVIDIA AUTOINSTALLER FOR FEDORA", fg="green", bold=True))

    instmode_dict: dict[str, Any] = {
        "rpmadd": instobjc.rpmadd(),
        "driver": instobjc.driver(),
        "x86lib": instobjc.x86lib(),
        "nvrepo": instobjc.nvrepo(),
        "checksu": instobjc.checksu(),
        "compat": instobjc.compat(),
        "primec": instobjc.primec(),
        "plcuda": instobjc.plcuda(),
        "ffmpeg": instobjc.ffmpeg(),
        "vulkan": instobjc.vulkan(),
        "vidacc": instobjc.vidacc(),
        "getall": instobjc.getall(),
    }
    instobjc.lsmenu() if not instmode_dict.get[instmode] else instmode_dict.get(instmode)


if __name__ == "__main__":
    main()
