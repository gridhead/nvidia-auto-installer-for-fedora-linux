import os, sys, click
import HostDetection, SupportCheck, RPMFHandler, DriverInstaller
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
            DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION...")
            if RPMFHandler.conn():
                DecoratorObject.SuccessMessage("Connection to RPM Fusion server was estabilished")
                DecoratorObject.SectionHeader("INSTALLING RPM FUSION NVIDIA REPOSITORY...")
                if RPMFHandler.main():
                    DecoratorObject.SuccessMessage("RPM Fusion NVIDIA repository was enabled")
                else:
                    DecoratorObject.FailureMessage("RPM Fusion NVIDIA repository could not be enabled")
            else:
                DecoratorObject.FailureMessage("RPM Fusion servers could not be connected")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def driver(self):
        DecoratorObject.SectionHeader("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
        if RPMFHandler.avbl():
            DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
            DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION...")
            if RPMFHandler.conn():
                DecoratorObject.SuccessMessage("Connection to RPM Fusion server was estabilished")
                DecoratorObject.SectionHeader("INSTALLING PROPRIETARY DRIVERS...")
                if DriverInstaller.main():
                    DecoratorObject.SuccessMessage("Driver package installation completed")
                else:
                    DecoratorObject.FailureMessage("Proprietary drivers could not be installed")
            else:
                DecoratorObject.FailureMessage("RPM Fusion servers could not be connected")
        else:
            DecoratorObject.FailureMessage("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

    def x86lib(self):
        pass

    def plcuda(self):
        pass

    def ffmpeg(self):
        pass

    def vidacc(self):
        pass

    def getall(self):
        pass

    def cheksu(self):
        pass

def PrintHelpMessage():
    DecoratorObject.SectionHeader("OPTIONS")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--rpmadd" + Style.RESET_ALL + " → This mode enables the RPM Fusion NVIDIA drivers repository")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--driver" + Style.RESET_ALL + " → This mode simply installs the NVIDIA driver")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--x86lib" + Style.RESET_ALL + " → This mode installs only the x86 libraries for Xorg")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--plcuda" + Style.RESET_ALL + " → This mode installs only the CUDA support softwares")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--ffmpeg" + Style.RESET_ALL + " → This mode installs only the FFMPEG acceleration")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--vulkan" + Style.RESET_ALL + " → This mode installs only the Vulkan renderer")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--vidacc" + Style.RESET_ALL + " → This mode installs only the VDPAU/VAAPI acceleration")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--getall" + Style.RESET_ALL + " → This mode installs all the above packages")
    DecoratorObject.NormalMessage(Style.BRIGHT + Fore.GREEN + "--help  " + Style.RESET_ALL + " → Show this message and exit")

@click.command()
@click.option("--rpmadd", "instmode", flag_value="rpmadd", help="This mode enables the RPM Fusion NVIDIA drivers repository")
@click.option("--driver", "instmode", flag_value="driver", help="This mode simply installs the NVIDIA driver")
@click.option("--x86lib", "instmode", flag_value="x86lib", help="This mode installs only the x86 libraries for Xorg")
@click.option("--plcuda", "instmode", flag_value="plcuda", help="This mode installs only the CUDA support softwares")
@click.option("--ffmpeg", "instmode", flag_value="ffmpeg", help="This mode installs only the FFMPEG acceleration")
@click.option("--vulkan", "instmode", flag_value="vulkan", help="This mode installs only the Vulkan renderer")
@click.option("--vidacc", "instmode", flag_value="vidacc", help="This mode installs only the VDPAU/VAAPI acceleration")
@click.option("--getall", "instmode", flag_value="getall", help="This mode installs all the above packages")
def clim(instmode):
    instobjc = InstallationMode()
    print(Style.BRIGHT + Fore.GREEN + "[ # ] NVIDIA AUTOINSTALLER FOR FEDORA 32 AND ABOVE" + Style.RESET_ALL)
    if instmode == "driver":
        instobjc.driver()
    elif instmode == "x86lib":
        click.echo(2)
    elif instmode == "plcuda":
        click.echo(3)
    elif instmode == "ffmpeg":
        click.echo(4)
    elif instmode == "vulkan":
        click.echo(5)
    elif instmode == "vidacc":
        click.echo(6)
    elif instmode == "getall":
        click.echo(7)
    elif instmode == "rpmadd":
        instobjc.rpmadd()
    else:
        PrintHelpMessage()

if __name__ == "__main__":
    clim()