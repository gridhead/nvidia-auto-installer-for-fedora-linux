import os, HostDetection, SupportCheck, RPMFHandler, PackageCheck, RepoInstaller, DriverInstaller, ForcingLoader, sys
from colorama import init, Fore, Back, Style

init()

def main():
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "[ ! ] NVIDIA AUTOINSTALLER FOR FEDORA WORKSTATION" + Style.RESET_ALL)
    HostDetection.main()
    SupportCheck.main()
    userinst = PackageCheck.main()
    if userinst == 1:
        repofetc = RPMFHandler.main()
        if repofetc == 1:
            RepoInstaller.main()
            DriverInstaller.main()
            ForcingLoader.main()
            print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "DRIVER INSTALLATION SUCCESSFULLY COMPLETED!" + Style.RESET_ALL)
            while True:
                userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to reboot your system now? (Y/N) " + Style.RESET_ALL)
                if userpick == "y" or userpick == "Y":
                    print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Rebooting now" + Style.RESET_ALL)
                    os.system("sudo systemctl reboot")
                elif userpick == "n" or userpick == "y":
                    print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "You would need to reboot to load up installed drivers" + Style.RESET_ALL)
                    print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer" + Style.RESET_ALL)
                    sys.exit(0)
        elif repofetc == -1:
            print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Installation cannot proceed without RPMFusion NVIDIA repository!" + Style.RESET_ALL)
            print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer" + Style.RESET_ALL)
            sys.exit(0)
        else:
            DriverInstaller.main()
            ForcingLoader.main()
            print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "DRIVER INSTALLATION SUCCESSFULLY COMPLETED!" + Style.RESET_ALL)
            while True:
                userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to reboot your system now? (Y/N) " + Style.RESET_ALL)
                if userpick == "y" or userpick == "Y":
                    print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Rebooting now" + Style.RESET_ALL)
                    os.system("sudo systemctl reboot")
                elif userpick == "n" or userpick == "y":
                    print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "You would need to reboot to load up installed drivers" + Style.RESET_ALL)
                    print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer" + Style.RESET_ALL)
                    sys.exit(0)
    else:
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Installation was cancelled voluntarily!" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer" + Style.RESET_ALL)
        sys.exit(0)

if __name__ == "__main__":
    main()