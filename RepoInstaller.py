import subprocess, os
from colorama import init, Fore, Back, Style

init()

def main():
    print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "FETCHING REPOSITORY DATA..." + Style.RESET_ALL)
    retndata = subprocess.getstatusoutput("sudo dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0]
    if retndata == 0:
        print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "RPMFusion NVIDIA repository was enabled!" + Style.RESET_ALL)
        os.system("sudo dnf update --refresh")
        print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Your packages have been updated!" + Style.RESET_ALL)
    else:
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "RPMFusion NVIDIA repository could not be enabled!" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer" + Style.RESET_ALL)
        exit()

if __name__ == "__main__":
    main()