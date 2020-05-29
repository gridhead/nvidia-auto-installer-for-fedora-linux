import os, sys
import HostDetection, SupportCheck, RPMFHandler, PackageCheck, RepoInstaller, DriverInstaller
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "[ # ] NVIDIA AUTOINSTALLER FOR FEDORA 32 AND ABOVE" + Style.RESET_ALL)
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
                    userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to reboot your system now? (Y/N) " + Style.RESET_ALL)
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
                    userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to reboot your system now? (Y/N) " + Style.RESET_ALL)
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

if __name__ == "__main__":
    main()