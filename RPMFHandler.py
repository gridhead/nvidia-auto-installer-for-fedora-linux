import subprocess
from colorama import init, Fore, Style

init()

def main():
    print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "ATTEMPTING CONNECTION TO RPMFUSION..." + Style.RESET_ALL)
    retndata = subprocess.getstatusoutput("ping -c 3 -W 3 rpmfusion.org")[0]
    if retndata == 0:
        print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Connection to RPMFusion server was established!" + Style.RESET_ALL)
        comand = "dnf repolist | grep 'rpmfusion-nonfree-nvidia-driver'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        if "rpmfusion-nonfree-nvidia-driver" in output:
            print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "RPMFusion repository for Proprietary NVIDIA Driver detected!" + Style.RESET_ALL)
        else:
            print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "RPMFusion repository for Proprietary NVIDIA Driver not detected!" + Style.RESET_ALL)
            while True:
                userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to fetch packages from this repository? (Y/N) " + Style.RESET_ALL)
                if userpick == "y" or userpick == "Y":
                    return 1
                elif userpick == "n" or userpick == "N":
                    return -1
    else:
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Connection to RPMFusion server could not be established!" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer" + Style.RESET_ALL)
        exit()

if __name__ == "__main__":
    main()