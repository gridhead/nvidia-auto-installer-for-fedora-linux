import subprocess, os
from colorama import init, Fore, Back, Style

init()

def main():
    print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "LOOKING FOR EXISTING PACKAGES..." + Style.RESET_ALL)
    comand = "rpm -qa | grep 'nvidia'"
    prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = prompt.communicate()[0].decode("utf-8")
    linect = output.count("\n")
    if linect == 0:
        print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "No existing NVIDIA drivers were detected!" + Style.RESET_ALL)
    else:
        print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "A total of " + str(linect) + " driver packages were detected!" + Style.RESET_ALL)
        pkname = output.split("\n")
        for indx in pkname:
            if indx != "":
                print("      " + Fore.WHITE + indx + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Do you wish to reinstall the drivers? (Y/N)" + Style.RESET_ALL)

if __name__ == "__main__":
    main()