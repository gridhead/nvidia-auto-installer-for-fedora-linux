import subprocess, sys
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()

def main():
    StatusDecorator.SectionHeader("ATTEMPTING CONNECTION TO RPMFUSION...")
    retndata = subprocess.getstatusoutput("ping -c 3 -W 3 rpmfusion.org")[0]
    if retndata == 0:
        StatusDecorator.SuccessMessage("Connection to RPMFusion server was estabilished")
        comand = "dnf repolist | grep 'rpmfusion-nonfree-nvidia-driver'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        if "rpmfusion-nonfree-nvidia-driver" in output:
            StatusDecorator.SuccessMessage("RPMFusion repository for Proprietary NVIDIA Driver detected")
            return 0
        else:
            StatusDecorator.WarningMessage("RPMFusion repository for Proprietary NVIDIA Driver not detected")
            while True:
                userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to fetch packages from this repository? (Y/N) " + Style.RESET_ALL)
                if userpick == "y" or userpick == "Y":
                    return 1
                elif userpick == "n" or userpick == "N":
                    return -1
    else:
        StatusDecorator.FailureMessage("Connection to RPMFusion server could not be established!")
        StatusDecorator.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()