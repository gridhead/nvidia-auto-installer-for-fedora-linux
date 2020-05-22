import subprocess
from colorama import init, Fore, Back, Style

init()

def main():
    print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "ATTEMPTING CONNECTION TO RPMFUSION..." + Style.RESET_ALL)
    retndata = subprocess.getstatusoutput("ping -c 3 -W 3 rpmfusion.org")[0]
    if retndata == 0:
        print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Connection to RPMFusion server was established!" + Style.RESET_ALL)
    else:
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Connection to RPMFusion server could not be established!" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer" + Style.RESET_ALL)
        exit()

if __name__ == "__main__":
    main()