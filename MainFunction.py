import os, subprocess, sys, click, distro
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
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
            "Distribution": str(distro.os_release_info()["name"]) + " " + str(distro.os_release_info()["version_id"]) + " " + str(os.uname().machine),
        }
        return jsondt

    def avbl(self):
        if str(distro.os_release_info()["name"]) == "Fedora":
            if int(distro.os_release_info()["version_id"]) >= 32:
                return "full"
            else:
                return "half"
        else:
            return False

class Coll_RPMFHandler(object):
    def avbl(self):
        comand = "dnf repolist | grep 'rpmfusion-nonfree-nvidia-driver'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        if "rpmfusion-nonfree-nvidia-driver" in output:
            return True
        else:
            return False

    def conn(self):
        retndata = subprocess.getstatusoutput("ping -c 3 -W 3 rpmfusion.org")[0]
        if retndata == 0:
            return True
        else:
            return False

    def main(self):
        os.system("dnf install -y fedora-workstation-repositories")
        retndata = subprocess.getstatusoutput("dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0]
        if retndata == 0:
            return True
        else:
            return False

class Coll_DriverInstaller(object):
    def main(self):
        ExecStatusCode = os.system(
            "dnf install -y gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs")
        if ExecStatusCode == 0:
            return True
        else:
            return False

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
        if ExecStatusCode == 0:
            return True
        else:
            return False

class Coll_PlCudaInstaller(object):
    def rpck(self):
        comand = "dnf repolist | grep 'cuda'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        if "cuda" in output:
            return True
        else:
            return False

    def rpin(self):
        retndata = subprocess.getstatusoutput("dnf config-manager --add-repo http://developer.download.nvidia.com/compute/cuda/repos/fedora29/x86_64/cuda-fedora29.repo")[0]
        print(retndata)
        if retndata == 0:
            return True
        else:
            return False

    def conn(self):
        retndata = subprocess.getstatusoutput("ping -c 3 -W 3 developer.download.nvidia.com")[0]
        if retndata == 0:
            return True
        else:
            return False

    def rpup(self):
        ExecStatusCode = os.system("dnf clean all")
        if ExecStatusCode == 0:
            return True
        else:
            return False

    def meta(self):
        ExecStatusCode = os.system("dnf install -y xorg-x11-drv-nvidia-cuda")
        if ExecStatusCode == 0:
            return True
        else:
            return False

    def main(self):
        ExecStatusCode = os.system("dnf install -y cuda")
        if ExecStatusCode == 0:
            return True
        else:
            return False

class Coll_FFMPEGInstaller(object):
    def main(self):
        ExecStatusCode = os.system("dnf install -y xorg-x11-drv-nvidia-cuda-libs")
        if ExecStatusCode == 0:
            return True
        else:
            return False

class Coll_VidAccInstaller(object):
    def main(self):
        ExecStatusCode = os.system("dnf install -y vdpauinfo libva-vdpau-driver libva-utils")
        if ExecStatusCode == 0:
            return True
        else:
            return False

class Coll_VulkanInstaller(object):
    def main(self):
        ExecStatusCode = os.system("dnf install -y vulkan")
        if ExecStatusCode == 0:
            return True
        else:
            return False

class Coll_SuperuserCheck(object):
    def main(self):
        data = os.geteuid()
        if data == 0:
            return True
        else:
            return False

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
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser privilege acquired")
            DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.SuccessMessage("No further action is necessary")
            else:
                DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
                DecoratorObject.WarningMessage("Repository enabling is required")
                DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.SuccessMessage("Connection to RPM Fusion servers was established")
                    DecoratorObject.SectionHeader("INSTALLING RPM FUSION NVIDIA REPOSITORY...")
                    if RPMFHandler.main():
                        DecoratorObject.SuccessMessage("RPM Fusion NVIDIA repository was enabled")
                    else:
                        DecoratorObject.FailureMessage("RPM Fusion NVIDIA repository could not be enabled")
                else:
                    DecoratorObject.FailureMessage("Connection to RPM Fusion servers could not be established")
        else:
            DecoratorObject.FailureMessage("Superuser privilege could not be acquired")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def driver(self):
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser privilege acquired")
            DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.SuccessMessage("Connection to RPM Fusion servers was established")
                    DecoratorObject.SectionHeader("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.WarningMessage("No existing NVIDIA driver packages were detected")
                        DecoratorObject.SectionHeader("INSTALLING PROPRIETARY DRIVERS...")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.NormalMessage(indx)
                        DecoratorObject.WarningMessage("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.SectionHeader("REINSTALLING PROPRIETARY DRIVERS...")
                    if DriverInstaller.main():
                        DecoratorObject.SuccessMessage("Driver package installation completed")
                    else:
                        DecoratorObject.FailureMessage("Proprietary drivers could not be installed")
                else:
                    DecoratorObject.FailureMessage("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.FailureMessage("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.FailureMessage("Superuser privilege could not be acquired")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def x86lib(self):
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser privilege acquired")
            DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.SuccessMessage("Connection to RPM Fusion servers was established")
                    DecoratorObject.SectionHeader("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.FailureMessage("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.NormalMessage(indx)
                        DecoratorObject.WarningMessage("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.SectionHeader("INSTALLING x86 LIBRARIES FOR XORG...")
                        if x86LibInstaller.main():
                            DecoratorObject.SuccessMessage("x86 libraries for XORG were successfully installed")
                        else:
                            DecoratorObject.FailureMessage("x86 libraries for XORG could not be installed")
                else:
                    DecoratorObject.FailureMessage("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.FailureMessage("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.FailureMessage("Superuser privilege could not be acquired")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def nvrepo(self):
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser privilege acquired")
            DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF OFFICIAL CUDA REPOSITORY...")
            if PlCudaInstaller.rpck():
                DecoratorObject.WarningMessage("Official CUDA repository was detected")
                DecoratorObject.SuccessMessage("No further action is necessary")
            else:
                DecoratorObject.WarningMessage("Official CUDA repository was not detected")
                DecoratorObject.WarningMessage("Repository enabling is required")
                DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO NVIDIA SERVERS...")
                if PlCudaInstaller.conn():
                    DecoratorObject.SuccessMessage("Connection to NVIDIA servers was established")
                    DecoratorObject.SectionHeader("INSTALLING OFFICIAL CUDA REPOSITORY...")
                    if PlCudaInstaller.rpin():
                        DecoratorObject.SuccessMessage("Official CUDA repository was enabled")
                        DecoratorObject.SectionHeader("REFRESHING REPOSITORY LIST...")
                        if PlCudaInstaller.rpup():
                            DecoratorObject.SuccessMessage("Repositories have been refreshed")
                        else:
                            DecoratorObject.FailureMessage("Repositories could not be refreshed")
                    else:
                        DecoratorObject.FailureMessage("Official CUDA repository could not be enabled")
                else:
                    DecoratorObject.FailureMessage("Connection to NVIDIA servers could not be established")
        else:
            DecoratorObject.FailureMessage("Superuser privilege could not be acquired")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def plcuda(self):
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser privilege acquired")
            DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.SuccessMessage("Connection to RPM Fusion servers was established")
                    DecoratorObject.SectionHeader("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.FailureMessage("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.NormalMessage(indx)
                        DecoratorObject.WarningMessage("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF OFFICIAL CUDA REPOSITORY...")
                        if PlCudaInstaller.rpck():
                            DecoratorObject.WarningMessage("Official CUDA repository was detected")
                            DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO NVIDIA SERVERS...")
                            if PlCudaInstaller.conn():
                                DecoratorObject.SuccessMessage("Connection to NVIDIA servers was established")
                                DecoratorObject.SectionHeader("INSTALLING RPM FUSION METAPACKAGE FOR CUDA...")
                                if PlCudaInstaller.meta():
                                    DecoratorObject.SuccessMessage("RPM Fusion CUDA metapackage was successfully installed")
                                    DecoratorObject.SectionHeader("INSTALLING NVIDIA CUDA CORE PACKAGES...")
                                    if PlCudaInstaller.main():
                                        DecoratorObject.SuccessMessage("NVIDIA CUDA core packages were successfully installed")
                                    else:
                                        DecoratorObject.FailureMessage("NVIDIA CUDA core packages could not be installed")
                                else:
                                    DecoratorObject.FailureMessage("RPM Fusion CUDA metapackage packages could not be installed")
                            else:
                                DecoratorObject.FailureMessage("Connection to NVIDIA servers could not be established")
                        else:
                            DecoratorObject.FailureMessage("Official CUDA repository was not detected")
                else:
                    DecoratorObject.FailureMessage("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.FailureMessage("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.FailureMessage("Superuser privilege could not be acquired")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def ffmpeg(self):
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser privilege acquired")
            DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.SuccessMessage("Connection to RPM Fusion servers was established")
                    DecoratorObject.SectionHeader("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.FailureMessage("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.NormalMessage(indx)
                        DecoratorObject.WarningMessage("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.SectionHeader("INSTALLING NVENC/NVDEC FOR FFMPEG ACCELERATION...")
                        if FFMPEGInstaller.main():
                            DecoratorObject.SuccessMessage("NVENC/NVDEC for FFMPEG acceleration were successfully installed")
                        else:
                            DecoratorObject.FailureMessage("NVENC/NVDEC for FFMPEG acceleration could not be installed")
                else:
                    DecoratorObject.FailureMessage("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.FailureMessage("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.FailureMessage("Superuser privilege could not be acquired")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def vulkan(self):
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser privilege acquired")
            DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.SuccessMessage("Connection to RPM Fusion servers was established")
                    DecoratorObject.SectionHeader("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.FailureMessage("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.NormalMessage(indx)
                        DecoratorObject.WarningMessage("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.SectionHeader("INSTALLING VULKAN RENDERER SUPPORT...")
                        if VulkanInstaller.main():
                            DecoratorObject.SuccessMessage("Vulkan renderer support were successfully installed")
                        else:
                            DecoratorObject.FailureMessage("Vulkan renderer support could not be installed")
                else:
                    DecoratorObject.FailureMessage("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.FailureMessage("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.FailureMessage("Superuser privilege could not be acquired")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def vidacc(self):
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser privilege acquired")
            DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if RPMFHandler.avbl():
                DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if RPMFHandler.conn():
                    DecoratorObject.SuccessMessage("Connection to RPM Fusion servers was established")
                    DecoratorObject.SectionHeader("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = DriverInstaller.avbl()
                    if data is False:
                        DecoratorObject.FailureMessage("No existing NVIDIA driver packages were detected")
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                DecoratorObject.NormalMessage(indx)
                        DecoratorObject.WarningMessage("A total of " + str(qant) + " driver packages were detected")
                        DecoratorObject.SectionHeader("INSTALLING VIDEO ACCELERATION SUPPORT...")
                        if VidAccInstaller.main():
                            DecoratorObject.SuccessMessage("Video acceleration were successfully installed")
                        else:
                            DecoratorObject.FailureMessage("Video acceleration could not be installed")
                else:
                    DecoratorObject.FailureMessage("Connection to RPM Fusion servers could not be established")
            else:
                DecoratorObject.FailureMessage("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        else:
            DecoratorObject.FailureMessage("Superuser privilege could not be acquired")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def getall(self):
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser privilege acquired")
            DecoratorObject.SectionHeader("FULL FLEDGED INSTALLATION BEGINNING...")
            DecoratorObject.NormalMessage("This mode is yet to be implemented")
        else:
            DecoratorObject.FailureMessage("Superuser privilege could not be acquired")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def cheksu(self):
        DecoratorObject.SectionHeader("CHECKING SUPERUSER PERMISSIONS...")
        if SuperuserCheck.main():
            DecoratorObject.SuccessMessage("Superuser permission is available")
            DecoratorObject.NormalMessage("This tool is expected to work correctly here")
        else:
            DecoratorObject.FailureMessage("Superuser permission is not available")
            DecoratorObject.NormalMessage("This tool cannot be used here")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def compat(self):
        DecoratorObject.SectionHeader("CHECKING FOR GPU COMPATIBILITY...")
        data = SupportCheck.gpuc()
        DecoratorObject.WarningMessage("Compatibility infomation was obtained")
        if data is False:
            DecoratorObject.FailureMessage("No supported NVIDIA GPU was detected")
        else:
            DecoratorObject.SuccessMessage("One or more active NVIDIA GPUs were detected")
            supprt = data["supprt"]
            gpulst = data["gpulst"]
            for indx in gpulst:
                if indx != "":
                    DecoratorObject.NormalMessage(indx)
            if supprt == "single":
                DecoratorObject.SuccessMessage("An single dedicated GPU setup was detected")
            else:
                DecoratorObject.SuccessMessage("An Optimus Dual GPU setup was detected")
            DecoratorObject.SectionHeader("GATHERING CURRENT HOST INFORMATION...")
            data = SupportCheck.main()
            DecoratorObject.WarningMessage("Host information was gathered")
            for indx in data.keys():
                DecoratorObject.NormalMessage(indx + ": " + data[indx])
            DecoratorObject.SectionHeader("CHECKING FOR HOST COMPATIBILITY...")
            data = SupportCheck.avbl()
            if data is False:
                DecoratorObject.FailureMessage("Unsupported OS detected")
                DecoratorObject.NormalMessage("This tool cannot be used here")
            else:
                if data == "full":
                    DecoratorObject.SuccessMessage("Supported OS detected")
                    DecoratorObject.NormalMessage("This tool is expected to work correctly here")
                elif data == "half":
                    DecoratorObject.WarningMessage("Minimally supported OS detected")
                    DecoratorObject.NormalMessage("Discretion is advised while using this tool")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def lsmenu(self):
        DecoratorObject.SectionHeader("OPTIONS")
        for indx in self.menudict.keys():
            DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + indx + Style.RESET_ALL + " → " + self.menudict[indx])
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
@click.version_option(version="v0.3.0", prog_name="NVAutoInstFedora32 by t0xic0der")
def clim(instmode):
    instobjc = InstallationMode()
    print(Style.BRIGHT + Fore.GREEN + "[ # ] NVIDIA AUTOINSTALLER FOR FEDORA 32 AND ABOVE" + Style.RESET_ALL)
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
    else:
        instobjc.lsmenu()

if __name__ == "__main__":
    clim()