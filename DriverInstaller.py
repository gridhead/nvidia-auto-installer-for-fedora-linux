import os, time
from colorama import init, Fore, Back, Style

init()

def main():
    print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "INSTALLING PROPRIETARY DRIVERS..." + Style.RESET_ALL)
    os.system("sudo dnf install gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs")
    print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Driver package installation completed!" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Commencing mandatory sleep for 5 minutes to load up kernel modules" + Style.RESET_ALL)
    time.sleep(30)
    print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Modified kernel modules have been loaded up!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()