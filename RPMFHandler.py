import subprocess, sys
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("ATTEMPTING CONNECTION TO RPM FUSION...")
    retndata = subprocess.getstatusoutput("ping -c 3 -W 3 rpmfusion.org")[0]
    if retndata == 0:
        DecoratorObject.SuccessMessage("Connection to RPM Fusion server was estabilished")
        comand = "dnf repolist | grep 'rpmfusion-nonfree-nvidia-driver'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        if "rpmfusion-nonfree-nvidia-driver" in output:
            DecoratorObject.SuccessMessage("RPM Fusion repository for Proprietary NVIDIA Driver detected")
            return 0
        else:
            DecoratorObject.WarningMessage("RPM Fusion repository for Proprietary NVIDIA Driver not detected")
            while True:
                userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + "Do you wish to fetch packages from this repository? (Y/N) ")
                if userpick == "y" or userpick == "Y":
                    return 1
                elif userpick == "n" or userpick == "N":
                    return -1
    else:
        DecoratorObject.FailureMessage("Connection to RPM Fusion server could not be established")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()