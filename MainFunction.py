import os, sys, click
import SupportCheck, RPMFHandler, DriverInstaller, x86LibInstaller, PlCudaInstaller, FFMPEGInstaller, VidAccInstaller, VulkanInstaller, SuperuserCheck
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

class InstallationMode(object):
    def __init__(self):
        pass

    def rpmadd(self):
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
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def driver(self):
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
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def x86lib(self):
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
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def nvrepo(self):
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
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def plcuda(self):
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
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def ffmpeg(self):
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
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def vulkan(self):
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
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def vidacc(self):
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
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def getall(self):
        DecoratorObject.SectionHeader("FULL FLEDGED INSTALLATION BEGINNING...")
        DecoratorObject.NormalMessage("This mode is yet to be implemented")
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

def PrintHelpMessage():
    DecoratorObject.SectionHeader("OPTIONS")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--rpmadd" + Style.RESET_ALL + " → This mode enables the RPM Fusion NVIDIA drivers repository")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--driver" + Style.RESET_ALL + " → This mode simply installs the NVIDIA driver")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--x86lib" + Style.RESET_ALL + " → This mode installs only the x86 libraries for Xorg")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--nvrepo" + Style.RESET_ALL + " → This mode enables the Official NVIDIA repository for CUDA")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--plcuda" + Style.RESET_ALL + " → This mode installs only the CUDA support softwares")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--ffmpeg" + Style.RESET_ALL + " → This mode installs only the FFMPEG acceleration")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--vulkan" + Style.RESET_ALL + " → This mode installs only the Vulkan renderer")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--vidacc" + Style.RESET_ALL + " → This mode installs only the VDPAU/VAAPI acceleration")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--getall" + Style.RESET_ALL + " → This mode installs all the above packages")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--cheksu" + Style.RESET_ALL + " → This mode allows you to check the user privilege level")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--compat" + Style.RESET_ALL + " → This mode allows you to check your compatibility")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--help  " + Style.RESET_ALL + " → Show this message and exit")

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
        PrintHelpMessage()

if __name__ == "__main__":
    clim()