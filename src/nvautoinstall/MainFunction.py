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

    def success_message(self, RequestMessage):
        click.echo(self.PASS + " " + RequestMessage)

    def failure_message(self, RequestMessage):
        click.echo(self.FAIL + " " + RequestMessage)

    def warning_message(self, RequestMessage):
        click.echo(self.WARN + " " + RequestMessage)

    def section_heading(self, RequestMessage):
        click.echo(self.HEAD + " " + click.style(RequestMessage, fg="magenta", bold=True))

    def general_message(self, RequestMessage):
        click.echo(self.STDS + " " + RequestMessage)


DecoratorObject = StatusDecorator()


class Coll_SupportCheck(object):
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


class Coll_RPMFHandler(object):
    def avbl(self):
        comand = "dnf repolist | grep 'rpmfusion-nonfree-nvidia-driver'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        return "rpmfusion-nonfree-nvidia-driver" in output

    def conn(self):
        retndata = subprocess.getstatusoutput("ping -c 3 -W 3 rpmfusion.org")[0]
        return retndata == 0

    def main(self):
        os.system("dnf install -y fedora-workstation-repositories")
        retndata = subprocess.getstatusoutput("dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0]
        return retndata == 0


class Coll_DriverInstaller(object):
    def main(self):
        ExecStatusCode = os.system("dnf install -y gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs")
        return ExecStatusCode == 0

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


class Coll_X86LibInstaller(object):
    def main(self):
        ExecStatusCode = os.system("dnf install -y xorg-x11-drv-nvidia-libs.i686")
        return ExecStatusCode == 0


class Coll_PlCudaInstaller(object):
    def rpck(self):
        comand = "dnf repolist | grep 'cuda'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        return "cuda" in output

    def rpin(self):
        retndata = subprocess.getstatusoutput("dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/fedora33/x86_64/cuda-fedora33.repo")[0]
        return retndata == 0

    def conn(self):
        retndata = subprocess.getstatusoutput("ping -c 3 -W 3 developer.download.nvidia.com")[0]
        return retndata == 0

    def rpup(self):
        ExecStatusCode = os.system("dnf clean all")
        return ExecStatusCode == 0

    def meta(self):
        ExecStatusCode = os.system("dnf install -y xorg-x11-drv-nvidia-cuda")
        return ExecStatusCode == 0

    def main(self):
        ExecStatusCode = os.system("dnf install -y cuda")
        return ExecStatusCode == 0


class Coll_FFMPEGInstaller(object):
    def main(self):
        ExecStatusCode = os.system("dnf install -y xorg-x11-drv-nvidia-cuda-libs")
        return ExecStatusCode == 0


class Coll_VidAccInstaller(object):
    def main(self):
        ExecStatusCode = os.system("dnf install -y vdpauinfo libva-vdpau-driver libva-utils")
        return ExecStatusCode == 0


class Coll_VulkanInstaller(object):
    def main(self):
        ExecStatusCode = os.system("dnf install -y vulkan")
        return ExecStatusCode == 0


class Coll_SuperuserCheck(object):
    def main(self):
        data = os.geteuid()
        return data == 0


SupportCheck = Coll_SupportCheck()
RPMFHandler = Coll_RPMFHandler()
DriverInstaller = Coll_DriverInstaller()
x86LibInstaller = Coll_X86LibInstaller()
PlCudaInstaller = Coll_PlCudaInstaller()
FFMPEGInstaller = Coll_FFMPEGInstaller()
VidAccInstaller = Coll_VidAccInstaller()
VulkanInstaller = Coll_VulkanInstaller()
SuperuserCheck = Coll_SuperuserCheck()


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

    def lsmenu(self):
        DecoratorObject.section_heading("OPTIONS")
        for indx in self.menudict.keys():
            DecoratorObject.general_message(click.style(indx, fg="green", bold=True) + "  " + self.menudict[indx])
        sys.exit(0)


@click.command()
@click.option("--rpmadd", "instmode", flag_value="rpmadd", help="This mode enables the RPM Fusion NVIDIA drivers repository")
@click.option("--driver", "instmode", flag_value="driver", help="This mode simply installs the NVIDIA driver")
@click.option("--x86lib", "instmode", flag_value="x86lib", help="This mode installs only the x86 libraries for Xorg")
@click.option("--nvrepo", "instmode", flag_value="nvrepo", help="This mode enables the Official NVIDIA repository for CUDA")
@click.option("--plcuda", "instmode", flag_value="plcuda", help="This mode installs only the CUDA support softwares")
@click.option("--ffmpeg", "instmode", flag_value="ffmpeg", help="This mode installs only the FFMPEG acceleration")
@click.option("--vulkan", "instmode", flag_value="vulkan", help="This mode installs only the Vulkan renderer")
@click.option("--vidacc", "instmode", flag_value="vidacc", help="This mode installs only the VDPAU/VAAPI acceleration")
@click.option("--getall", "instmode", flag_value="getall", help="This mode installs all the above packages")
@click.option("--cheksu", "instmode", flag_value="cheksu", help="This mode allows you to check the user privilege level")
@click.option("--compat", "instmode", flag_value="compat", help="This mode allows you to check your compatibility")
@click.version_option(version=__version__, prog_name=click.style("NVAutoInstall by Akashdeep Dhar <t0xic0der@fedoraproject>", fg="green", bold=True))
def clim(instmode):
    instobjc = InstallationMode()
    click.echo(click.style("[ # ] NVIDIA AUTOINSTALLER FOR FEDORA", fg="green", bold=True))
    if instmode == "rpmadd":    instobjc.rpmadd()
    elif instmode == "driver":  instobjc.driver()
    elif instmode == "x86lib":  instobjc.x86lib()
    elif instmode == "nvrepo":  instobjc.nvrepo()
    elif instmode == "plcuda":  instobjc.plcuda()
    elif instmode == "ffmpeg":  instobjc.ffmpeg()
    elif instmode == "vulkan":  instobjc.vulkan()
    elif instmode == "vidacc":  instobjc.vidacc()
    elif instmode == "getall":  instobjc.getall()
    elif instmode == "cheksu":  instobjc.cheksu()
    elif instmode == "compat":  instobjc.compat()
    else:                       instobjc.lsmenu()


if __name__ == "__main__":
    clim()
