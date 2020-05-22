import os, HostDetection, SupportCheck, RPMFHandler, PackageCheck, RepoInstaller
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
        else:
            print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Installation cannot proceed without RPMFusion NVIDIA repository!" + Style.RESET_ALL)
            print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer" + Style.RESET_ALL)
            exit()
    else:
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Installation was cancelled voluntarily!" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer" + Style.RESET_ALL)
        exit()

if __name__ == "__main__":
    main()