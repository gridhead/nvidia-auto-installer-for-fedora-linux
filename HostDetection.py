import os
from colorama import init, Fore, Back, Style

init()

def main():
    print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "GATHERING ACTIVE INFORMATION..." + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Host information was gathered!" + Style.RESET_ALL)
    datadict = {
        "System": str(os.uname().sysname),
        "Hostname": str(os.uname().nodename),
        "Release": str(os.uname().release),
        "Version": str(os.uname().version),
        "Machine": str(os.uname().machine),
    }
    for indx in datadict.keys():
        print(Style.BRIGHT + Fore.GREEN + "     " + Style.RESET_ALL + " " + Fore.WHITE + indx + ": " + datadict[indx] + Style.RESET_ALL)

if __name__ == "__main__":
    main()