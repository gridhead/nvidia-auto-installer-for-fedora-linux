import subprocess
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("LOOKING FOR EXISTING DRIVER PACKAGES...")
    comand = "rpm -qa | grep 'nvidia'"
    prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = prompt.communicate()[0].decode("utf-8")
    linect = output.count("\n")
    if linect == 0:
        DecoratorObject.WarningMessage("No existing NVIDIA drivers were detected!")
        while True:
            userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to install the drivers? (Y/N) " + Style.RESET_ALL)
            if userpick == "y" or userpick == "Y":
                return 1
            elif userpick == "n" or userpick == "N":
                return -1
    else:
        DecoratorObject.SuccessMessage("A total of " + str(linect) + " driver packages were detected!")
        pkname = output.split("\n")
        for indx in pkname:
            if indx != "":
                DecoratorObject.NormalMessage(indx)
        while True:
            userpick = input(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to reinstall the drivers? (Y/N) " + Style.RESET_ALL)
            if userpick == "y" or userpick == "Y":
                return 1
            elif userpick == "n" or userpick == "N":
                return -1

if __name__ == "__main__":
    main()