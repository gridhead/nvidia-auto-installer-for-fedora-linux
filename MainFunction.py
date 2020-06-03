import os, sys, click
import HostDetection, SupportCheck, RPMFHandler, PackageCheck, RepoInstaller, DriverInstaller
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "[ # ] NVIDIA AUTOINSTALLER FOR FEDORA 32 AND ABOVE" + Style.RESET_ALL)
    if os.geteuid() == 0:
        HostDetection.main()
        SupportCheck.main()
        userinst = PackageCheck.main()
        if userinst == 1:
            repofetc = RPMFHandler.main()
            if repofetc == 1:
                RepoInstaller.main()
                DriverInstaller.main()
                DecoratorObject.SectionHeader("DRIVER INSTALLATION SUCCESSFULLY COMPLETED")
                while True:
                    userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + "Do you wish to reboot your system now? (Y/N) ")
                    if userpick == "y" or userpick == "Y":
                        DecoratorObject.WarningMessage("Rebooting now")
                        os.system("systemctl reboot")
                    elif userpick == "n" or userpick == "N":
                        DecoratorObject.WarningMessage("You would need to reboot to load up installed drivers")
                        DecoratorObject.FailureMessage("Leaving installer")
                        sys.exit(0)
            elif repofetc == -1:
                DecoratorObject.FailureMessage("Installation cannot proceed without RPM Fusion NVIDIA repository!")
                DecoratorObject.FailureMessage("Leaving installer")
                sys.exit(0)
            else:
                DriverInstaller.main()
                DecoratorObject.SectionHeader("DRIVER INSTALLATION SUCCESSFULLY COMPLETED")
                while True:
                    userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + "Do you wish to reboot your system now? (Y/N) ")
                    if userpick == "y" or userpick == "Y":
                        DecoratorObject.WarningMessage("Rebooting now")
                        os.system("systemctl reboot")
                    elif userpick == "n" or userpick == "N":
                        DecoratorObject.WarningMessage("You would need to reboot to load up installed drivers")
                        DecoratorObject.FailureMessage("Leaving installer")
                        sys.exit(0)
        else:
            DecoratorObject.FailureMessage("Installation was cancelled voluntarily")
            DecoratorObject.FailureMessage("Leaving installer")
            sys.exit(0)
    else:
        DecoratorObject.FailureMessage("Installer cannot proceed without root privileges")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

class InstallationMode(object):
    def __init__(self):
        pass

    def rpmadd(self):
        pass

    def driver(self):
        pass

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
        click.echo(1)
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