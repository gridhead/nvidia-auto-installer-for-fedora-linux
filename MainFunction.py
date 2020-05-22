import os, HostDetection, SupportCheck, RPMFHandler, PackageCheck
from colorama import init, Fore, Back, Style

init()

def main():
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "[ ! ] NVIDIA AUTOINSTALLER FOR FEDORA WORKSTATION" + Style.RESET_ALL)
    HostDetection.main()
    SupportCheck.main()
    PackageCheck.main()
    RPMFHandler.main()

if __name__ == "__main__":
    try:
        main()
    except BaseException:
        print("")
        print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Abort call received or exception found - Leaving installer." + Style.RESET_ALL)
        exit()