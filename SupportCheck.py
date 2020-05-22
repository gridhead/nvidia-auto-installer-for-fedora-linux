import subprocess, os
from colorama import init, Fore, Back, Style

init()

def main():
    print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "CHECKING FOR GPU COMPATIBILITY..." + Style.RESET_ALL)
    comand = "lspci | grep -E 'VGA|3D'"
    prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = prompt.communicate()[0].decode("utf-8")
    linect = output.count("\n")
    pkname = output.split("\n")
    print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Compatibility infomation was obtained!" + Style.RESET_ALL)
    for indx in pkname:
        if indx != "":
            print("      " + Fore.WHITE + indx + Style.RESET_ALL)
    if "NVIDIA" not in output:
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "No supported NVIDIA GPU was detected!" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Leaving installer with ERROR CODE - NVNF" + Style.RESET_ALL)
        exit()
    else:
        print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "An active NVIDIA GPU was detected!" + Style.RESET_ALL)
    if linect == 1:
        print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "An single dedicated GPU setup was detected!" + Style.RESET_ALL)
    else:
        print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "An Optimus Dual GPU setup was detected!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()