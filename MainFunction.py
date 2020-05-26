import os, sys
import HostDetection, SupportCheck, RPMFHandler, PackageCheck, RepoInstaller, DriverInstaller, ForcingLoader
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()

def main():
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "[ # ] NVIDIA AUTOINSTALLER FOR FEDORA WORKSTATION" + Style.RESET_ALL)
    HostDetection.main()
    SupportCheck.main()
    userinst = PackageCheck.main()
    if userinst == 1:
        repofetc = RPMFHandler.main()
        if repofetc == 1:
            RepoInstaller.main()
            DriverInstaller.main()
            ForcingLoader.main()
            StatusDecorator.SectionHeader("DRIVER INSTALLATION SUCCESSFULLY COMPLETED")
            while True:
                userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to reboot your system now? (Y/N) " + Style.RESET_ALL)
                if userpick == "y" or userpick == "Y":
                    StatusDecorator.WarningMessage("Rebooting now")
                    os.system("sudo systemctl reboot")
                elif userpick == "n" or userpick == "y":
                    StatusDecorator.WarningMessage("You would need to reboot to load up installed drivers")
                    StatusDecorator.FailureMessage("Leaving installer")
                    sys.exit(0)
        elif repofetc == -1:
            StatusDecorator.FailureMessage("Installation cannot proceed without RPMFusion NVIDIA repository!")
            StatusDecorator.FailureMessage("Leaving installer")
            sys.exit(0)
        else:
            DriverInstaller.main()
            ForcingLoader.main()
            StatusDecorator.SectionHeader("DRIVER INSTALLATION SUCCESSFULLY COMPLETED")
            while True:
                userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to reboot your system now? (Y/N) " + Style.RESET_ALL)
                if userpick == "y" or userpick == "Y":
                    StatusDecorator.WarningMessage("Rebooting now")
                    os.system("sudo systemctl reboot")
                elif userpick == "n" or userpick == "y":
                    StatusDecorator.WarningMessage("You would need to reboot to load up installed drivers")
                    StatusDecorator.FailureMessage("Leaving installer")
                    sys.exit(0)
    else:
        StatusDecorator.FailureMessage("Installation was cancelled voluntarily!")
        StatusDecorator.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()