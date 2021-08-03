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
import subprocess
import sys

import click
import distro

try:
    # Imports version in the packaged environment
    from nvautoinstall import __version__
except ModuleNotFoundError:
    # Imports version in the development environment
    from __init__ import __version__


class StatusDecorator(object):
    def __init__(self):
        self.PASS = click.style("[ \u2713 ]", fg="green", bold=True)
        self.FAIL = click.style("[ \u2717 ]", fg="red", bold=True)
        self.WARN = click.style("[ ! ]", fg="yellow", bold=True)
        self.HEAD = click.style("[ \u2605 ]", fg="magenta", bold=True)
        self.STDS = "     "

    def success_message(self, request_message):
        click.echo(self.PASS + " " + request_message)

    def failure_message(self, request_message):
        click.echo(self.FAIL + " " + request_message)

    def warning_message(self, request_message):
        click.echo(self.WARN + " " + request_message)

    def section_heading(self, request_message):
        click.echo(self.HEAD + " " + click.style(request_message, fg="magenta", bold=True))

    def general_message(self, request_message):
        click.echo(self.STDS + " " + request_message)


DecoratorObject = StatusDecorator()


class CollSupportCheck(object):
    def gpuc(self):
        comand = "lspci | grep -E 'VGA|3D'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        linect = output.count("\n")
        pkname = output.split("\n")
        if "NVIDIA" not in output:
            return False
        else:
            if linect == 1:
                supprt = "single"
            else:
                supprt = "optims"
            jsondt = {
                "supprt": supprt,
                "gpuqnt": linect,
                "gpulst": pkname,
            }
            return jsondt

    def main(self):
        jsondt = {
            "System": str(os.uname().sysname) + " v" + str(os.uname().release),
            "Hostname": str(os.uname().nodename),
            "Version": str(os.uname().version),
            "Distribution": str(distro.os_release_info()["name"]) + " " + str(os.uname().machine),
        }
        return jsondt

    def avbl(self):
        try:
            if str(distro.os_release_info()["name"]) == "Fedora":
                if int(distro.os_release_info()["version_id"]) >= 32:
                    return "full"
                else:
                    return "half"
            else:
                return False
        except KeyError:
            return False


class CollRPMFHandler(object):
    def avbl(self):
        comand = "dnf repolist | grep 'rpmfusion-nonfree-nvidia-driver'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        return "rpmfusion-nonfree-nvidia-driver" in output

    def conn(self):
        retndata = subprocess.getstatusoutput("curl https://rpmfusion.org")[0]
        return retndata == 0

    def main(self):
        os.system("dnf install -y fedora-workstation-repositories")
        retndata = subprocess.getstatusoutput("dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0]
        return retndata == 0


class CollDriverInstaller(object):
    def main(self):
        exec_status_code = os.system("dnf install -y gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs")
        return exec_status_code == 0

    def avbl(self):
        comand = "rpm -qa | grep 'nvidia'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        linect = output.count("\n")
        if linect == 0:
            return False
        else:
            pkname = output.split("\n")
            return pkname


class CollX86LibInstaller(object):
    def main(self):
        exec_status_code = os.system("dnf install -y xorg-x11-drv-nvidia-libs.i686")
        return exec_status_code == 0


class CollPlCudaInstaller(object):
    def rpck(self):
        comand = "dnf repolist | grep 'cuda'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        return "cuda" in output

    def rpin(self):
        retndata = subprocess.getstatusoutput("dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/fedora33/x86_64/cuda-fedora33.repo")[0]
        return retndata == 0

    def conn(self):
        retndata = subprocess.getstatusoutput("curl https://developer.download.nvidia.com/compute/cuda/repos/")[0]
        return retndata == 0

    def rpup(self):
        exec_status_code = os.system("dnf clean all")
        return exec_status_code == 0

    def meta(self):
        exec_status_code = os.system("dnf install -y xorg-x11-drv-nvidia-cuda")
        return exec_status_code == 0

    def stop(self):
        exec_status_code = os.system("dnf module disable -y nvidia-driver")
        return exec_status_code == 0

    def main(self):
        exec_status_code = os.system("dnf install -y cuda")
        return exec_status_code == 0


class CollFFMPEGInstaller(object):
    def main(self):
        exec_status_code = os.system("dnf install -y xorg-x11-drv-nvidia-cuda-libs")
        return exec_status_code == 0


class CollVidAccInstaller(object):
    def main(self):
        exec_status_code = os.system("dnf install -y vdpauinfo libva-vdpau-driver libva-utils")
        return exec_status_code == 0


class CollVulkanInstaller(object):
    def main(self):
        exec_status_code = os.system("dnf install -y vulkan")
        return exec_status_code == 0


class CollSuperuserCheck(object):
    def main(self):
        data = os.geteuid()
        return data == 0


class CollPrimeSupportEnabler(object):
    def main(self, opts):
        try:
            with open("/usr/share/X11/xorg.conf.d/nvidia.conf", "r") as sharconf:
                shardata = sharconf.read()
            primemod = ""
            for indx in shardata.split("\n"):
                primemod += indx + "\n"
                if opts is True and indx == "\tOption \"BaseMosaic\" \"on\"":
                    primemod += "\tOption \"PrimaryGPU\" \"yes\"" + "\n"
            with open("/etc/X11/xorg.conf.d/nvidia.conf", "w") as etcdconf:
                etcdconf.write(primemod)
            return True
        except Exception:
            return False


SupportCheck = CollSupportCheck()
RPMFHandler = CollRPMFHandler()
DriverInstaller = CollDriverInstaller()
x86LibInstaller = CollX86LibInstaller()
PlCudaInstaller = CollPlCudaInstaller()
FFMPEGInstaller = CollFFMPEGInstaller()
VidAccInstaller = CollVidAccInstaller()
VulkanInstaller = CollVulkanInstaller()
SuperuserCheck = CollSuperuserCheck()
PrimeSupportEnabler = CollPrimeSupportEnabler()


class InstallationMode(object):
    def __init__(self):
        self.menudict = {
            "--rpmadd " : "This mode enables the RPM Fusion NVIDIA drivers repository.",
            "--driver " : "This mode simply installs the NVIDIA driver.",
            "--x86lib " : "This mode installs only the x86 libraries for Xorg.",
            "--nvrepo " : "This mode enables the Official NVIDIA repository for CUDA.",
            "--plcuda " : "This mode installs only the CUDA support softwares.",
            "--ffmpeg " : "This mode installs only the FFMPEG acceleration.",
            "--vulkan " : "This mode installs only the Vulkan renderer.",
            "--vidacc " : "This mode installs only the VDPAU/VAAPI acceleration.",
            "--getall " : "This mode installs all the above packages.",
            "--cheksu " : "This mode allows you to check the user privilege level.",
            "--compat " : "This mode allows you to check your compatibility.",
            "--primec " : "This mode allows you to setup PRIME configuration.",
            "--version" : "Show the version and exit.",
            "--help   " : "Show this message and exit.",
        }

    def rpmadd(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.warning_message("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.success_message("No further action is necessary")
            else:
                DecoratorObject.warning_message("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
                DecoratorObject.warning_message("Repository enabling is required")
                DecoratorObject.section_heading("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.success_message("Connection to RPM Fusion servers was established")
                    DecoratorObject.section_heading("INSTALLING RPM FUSION NVIDIA REPOSITORY...")
                    if RPMFHandler.main():
                        DecoratorObject.success_message("RPM Fusion NVIDIA repository was enabled")
                    else:
                        DecoratorObject.failure_message("RPM Fusion NVIDIA repository could not be enabled")
                else:
                    DecoratorObject.failure_message("Connection to RPM Fusion servers could not be established")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def driver(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.warning_message("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.section_heading("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.success_message("Connection to RPM Fusion servers was established")
                    DecoratorObject.section_heading("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.warning_message("No existing NVIDIA driver packages were detected")
                        DecoratorObject.section_heading("INSTALLING PROPRIETARY DRIVERS...")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.general_message(indx)
                        DecoratorObject.warning_message("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.section_heading("REINSTALLING PROPRIETARY DRIVERS...")
                    if DriverInstaller.main():
                        DecoratorObject.success_message("Driver package installation completed")
                    else:
                        DecoratorObject.failure_message("Proprietary drivers could not be installed")
                else:
                    DecoratorObject.failure_message("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.failure_message("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def x86lib(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.warning_message("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.section_heading("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.success_message("Connection to RPM Fusion servers was established")
                    DecoratorObject.section_heading("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.failure_message("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.general_message(indx)
                        DecoratorObject.warning_message("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.section_heading("INSTALLING x86 LIBRARIES FOR XORG...")
                        if x86LibInstaller.main():
                            DecoratorObject.success_message("x86 libraries for XORG were successfully installed")
                        else:
                            DecoratorObject.failure_message("x86 libraries for XORG could not be installed")
                else:
                    DecoratorObject.failure_message("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.failure_message("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def nvrepo(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("CHECKING AVAILABILITY OF OFFICIAL CUDA REPOSITORY...")
            if PlCudaInstaller.rpck():
                DecoratorObject.warning_message("Official CUDA repository was detected")
                DecoratorObject.success_message("No further action is necessary")
            else:
                DecoratorObject.warning_message("Official CUDA repository was not detected")
                DecoratorObject.warning_message("Repository enabling is required")
                DecoratorObject.section_heading("ATTEMPTING CONNECTION TO NVIDIA SERVERS...")
                if PlCudaInstaller.conn():
                    DecoratorObject.success_message("Connection to NVIDIA servers was established")
                    DecoratorObject.section_heading("INSTALLING OFFICIAL CUDA REPOSITORY...")
                    if PlCudaInstaller.rpin():
                        DecoratorObject.success_message("Official CUDA repository was enabled")
                        DecoratorObject.section_heading("REFRESHING REPOSITORY LIST...")
                        if PlCudaInstaller.rpup():
                            DecoratorObject.success_message("Repositories have been refreshed")
                            DecoratorObject.section_heading("DISABLING NVIDIA DRIVER MODULE...")
                            if PlCudaInstaller.stop():
                                DecoratorObject.success_message("NVIDIA DRIVER module has been disabled")
                            else:
                                DecoratorObject.failure_message("NVIDIA DRIVER module could not be disabled")
                        else:
                            DecoratorObject.failure_message("Repositories could not be refreshed")
                    else:
                        DecoratorObject.failure_message("Official CUDA repository could not be enabled")
                else:
                    DecoratorObject.failure_message("Connection to NVIDIA servers could not be established")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def plcuda(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.warning_message("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.section_heading("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.success_message("Connection to RPM Fusion servers was established")
                    DecoratorObject.section_heading("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.failure_message("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.general_message(indx)
                        DecoratorObject.warning_message("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.section_heading("CHECKING AVAILABILITY OF OFFICIAL CUDA REPOSITORY...")
                        if PlCudaInstaller.rpck():
                            DecoratorObject.warning_message("Official CUDA repository was detected")
                            DecoratorObject.section_heading("ATTEMPTING CONNECTION TO NVIDIA SERVERS...")
                            if PlCudaInstaller.conn():
                                DecoratorObject.success_message("Connection to NVIDIA servers was established")
                                DecoratorObject.section_heading("INSTALLING RPM FUSION METAPACKAGE FOR CUDA...")
                                if PlCudaInstaller.meta():
                                    DecoratorObject.success_message("RPM Fusion CUDA metapackage was successfully installed")
                                    DecoratorObject.section_heading("INSTALLING NVIDIA CUDA CORE PACKAGES...")
                                    if PlCudaInstaller.main():
                                        DecoratorObject.success_message("NVIDIA CUDA core packages were successfully installed")
                                    else:
                                        DecoratorObject.failure_message("NVIDIA CUDA core packages could not be installed")
                                else:
                                    DecoratorObject.failure_message("RPM Fusion CUDA metapackage packages could not be installed")
                            else:
                                DecoratorObject.failure_message("Connection to NVIDIA servers could not be established")
                        else:
                            DecoratorObject.failure_message("Official CUDA repository was not detected")
                else:
                    DecoratorObject.failure_message("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.failure_message("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def ffmpeg(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.warning_message("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.section_heading("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.success_message("Connection to RPM Fusion servers was established")
                    DecoratorObject.section_heading("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.failure_message("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.general_message(indx)
                        DecoratorObject.warning_message("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.section_heading("INSTALLING NVENC/NVDEC FOR FFMPEG ACCELERATION...")
                        if FFMPEGInstaller.main():
                            DecoratorObject.success_message("NVENC/NVDEC for FFMPEG acceleration were successfully installed")
                        else:
                            DecoratorObject.failure_message("NVENC/NVDEC for FFMPEG acceleration could not be installed")
                else:
                    DecoratorObject.failure_message("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.failure_message("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def vulkan(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.warning_message("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.section_heading("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.success_message("Connection to RPM Fusion servers was established")
                    DecoratorObject.section_heading("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.failure_message("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.general_message(indx)
                        DecoratorObject.warning_message("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.section_heading("INSTALLING VULKAN RENDERER SUPPORT...")
                        if VulkanInstaller.main():
                            DecoratorObject.success_message("Vulkan renderer support were successfully installed")
                        else:
                            DecoratorObject.failure_message("Vulkan renderer support could not be installed")
                else:
                    DecoratorObject.failure_message("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.failure_message("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def vidacc(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.warning_message("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.section_heading("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.success_message("Connection to RPM Fusion servers was established")
                    DecoratorObject.section_heading("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.failure_message("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.general_message(indx)
                        DecoratorObject.warning_message("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.section_heading("INSTALLING VIDEO ACCELERATION SUPPORT...")
                        if VidAccInstaller.main():
                            DecoratorObject.success_message("Video acceleration were successfully installed")
                        else:
                            DecoratorObject.failure_message("Video acceleration could not be installed")
                else:
                    DecoratorObject.failure_message("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.failure_message("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def getall(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("FULL FLEDGED INSTALLATION BEGINNING...")
            DecoratorObject.general_message("This mode is yet to be implemented")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def cheksu(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser permission is available")
            DecoratorObject.general_message("This tool is expected to work correctly here")
        else:
            DecoratorObject.failure_message("Superuser permission is not available")
            DecoratorObject.general_message("This tool cannot be used here")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def compat(self):
        DecoratorObject.section_heading("CHECKING FOR GPU COMPATIBILITY...")
        data = SupportCheck.gpuc()
        DecoratorObject.warning_message("Compatibility infomation was obtained")
        if data is False:
            DecoratorObject.failure_message("No supported NVIDIA GPU was detected")
        else:
            DecoratorObject.success_message("One or more active NVIDIA GPUs were detected")
            supprt = data["supprt"]
            gpulst = data["gpulst"]
            for indx in gpulst:
                if indx != "":
                    DecoratorObject.general_message(indx)
            if supprt == "single":
                DecoratorObject.success_message("An single dedicated GPU setup was detected")
            else:
                DecoratorObject.success_message("An Optimus Dual GPU setup was detected")
            DecoratorObject.section_heading("GATHERING CURRENT HOST INFORMATION...")
            data = SupportCheck.main()
            DecoratorObject.warning_message("Host information was gathered")
            for indx in data.keys():
                DecoratorObject.general_message(indx + ": " + data[indx])
            DecoratorObject.section_heading("CHECKING FOR HOST COMPATIBILITY...")
            data = SupportCheck.avbl()
            if data is False:
                DecoratorObject.failure_message("Unsupported OS detected")
                DecoratorObject.general_message("This tool cannot be used here")
            else:
                if data == "full":
                    DecoratorObject.success_message("Supported OS detected")
                    DecoratorObject.general_message("This tool is expected to work correctly here")
                elif data == "half":
                    DecoratorObject.warning_message("Minimally supported OS detected")
                    DecoratorObject.general_message("Discretion is advised while using this tool")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def primec(self):
        DecoratorObject.section_heading("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.success_message("Superuser privilege acquired")
            DecoratorObject.section_heading("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.warning_message("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.section_heading("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.success_message("Connection to RPM Fusion servers was established")
                    DecoratorObject.section_heading("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.failure_message("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.general_message(indx)
                        DecoratorObject.warning_message("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.section_heading("SETTING UP PRIME SUPPORT...")
                        DecoratorObject.warning_message("Intervention required")
                        DecoratorObject.general_message(click.style("< Y >", fg="green", bold=True) + " to enable PRIME support")
                        DecoratorObject.general_message(click.style("< N >", fg="red", bold=True) + " to disable PRIME support")
                        DecoratorObject.general_message(click.style("< * >", fg="yellow", bold=True) + " anything else to leave")
                        solution = input("[Y/N] ")
                        if solution == "Y" or solution == "y":
                            DecoratorObject.section_heading("ENABLING PRIME SUPPORT...")
                            if PrimeSupportEnabler.main(True):
                                DecoratorObject.success_message("PRIME Support was successfully enabled")
                            else:
                                DecoratorObject.failure_message("PRIME Support could not be enabled")
                        elif solution == "N" or solution == "n":
                            DecoratorObject.section_heading("DISABLING PRIME SUPPORT...")
                            if PrimeSupportEnabler.main(False):
                                DecoratorObject.success_message("PRIME Support was successfully disabled")
                            else:
                                DecoratorObject.failure_message("PRIME Support could not be disabled")
                        else:
                            DecoratorObject.section_heading("SAFE AND GOOD ANSWER...")
                else:
                    DecoratorObject.failure_message("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.failure_message("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.failure_message("Superuser privilege could not be acquired")
        DecoratorObject.failure_message("Leaving installer")
        sys.exit(0)

    def lsmenu(self):
        DecoratorObject.section_heading("OPTIONS")
        for indx in self.menudict.keys():
            DecoratorObject.general_message(click.style(indx, fg="green", bold=True) + "  " + self.menudict[indx])
        sys.exit(0)


@click.command()
@click.option(
    "--rpmadd",
    "instmode",
    flag_value="rpmadd",
    help="This mode enables the RPM Fusion NVIDIA drivers repository."
)
@click.option(
    "--driver",
    "instmode",
    flag_value="driver",
    help="This mode simply installs the NVIDIA driver."
)
@click.option(
    "--x86lib",
    "instmode",
    flag_value="x86lib",
    help="This mode installs only the x86 libraries for Xorg."
)
@click.option(
    "--nvrepo",
    "instmode",
    flag_value="nvrepo",
    help="This mode enables the Official NVIDIA repository for CUDA."
)
@click.option(
    "--plcuda",
    "instmode",
    flag_value="plcuda",
    help="This mode installs only the CUDA support softwares."
)
@click.option(
    "--ffmpeg",
    "instmode",
    flag_value="ffmpeg",
    help="This mode installs only the FFMPEG acceleration."
)
@click.option(
    "--vulkan",
    "instmode",
    flag_value="vulkan",
    help="This mode installs only the Vulkan renderer."
)
@click.option(
    "--vidacc",
    "instmode",
    flag_value="vidacc",
    help="This mode installs only the VDPAU/VAAPI acceleration."
)
@click.option(
    "--getall",
    "instmode",
    flag_value="getall",
    help="This mode installs all the above packages."
)
@click.option(
    "--cheksu",
    "instmode",
    flag_value="cheksu",
    help="This mode allows you to check the user privilege level."
)
@click.option(
    "--compat",
    "instmode",
    flag_value="compat",
    help="This mode allows you to check your compatibility."
)
@click.option(
    "--primec",
    "instmode",
    flag_value="primec",
    help="This mode allows you to setup PRIME configuration."
)
@click.version_option(
    version=__version__,
    prog_name=click.style(
        "NVAutoInstall by Akashdeep Dhar <t0xic0der@fedoraproject.org>",
        fg="green",
        bold=True
    )
)
def clim(instmode):
    instobjc = InstallationMode()
    click.echo(click.style("[ # ] NVIDIA AUTOINSTALLER FOR FEDORA", fg="green", bold=True))
    if instmode == "rpmadd":
        instobjc.rpmadd()
    elif instmode == "driver":
        instobjc.driver()
    elif instmode == "x86lib":
        instobjc.x86lib()
    elif instmode == "nvrepo":
        instobjc.nvrepo()
    elif instmode == "plcuda":
        instobjc.plcuda()
    elif instmode == "ffmpeg":
        instobjc.ffmpeg()
    elif instmode == "vulkan":
        instobjc.vulkan()
    elif instmode == "vidacc":
        instobjc.vidacc()
    elif instmode == "getall":
        instobjc.getall()
    elif instmode == "cheksu":
        instobjc.cheksu()
    elif instmode == "compat":
        instobjc.compat()
    elif instmode == "primec":
        instobjc.primec()
    else:
        instobjc.lsmenu()


if __name__ == "__main__":
    clim()
