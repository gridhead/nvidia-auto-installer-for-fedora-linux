import os, HostDetection, SupportCheck, RPMFHandler, PackageCheck
from colorama import init, Fore, Back, Style

init()

def main():
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX + "[ ! ] NVIDIA AUTOINSTALLER FOR FEDORA WORKSTATION" + Style.RESET_ALL)
    HostDetection.main()
    SupportCheck.main()
    PackageCheck.main()

if __name__ == "__main__":
    main()