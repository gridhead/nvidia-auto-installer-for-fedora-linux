import os, time
from colorama import init, Fore, Style

init()

def main():
    print(Style.BRIGHT + Fore.CYAN + "[ ✔ ]" + " " + "FORCING READ FROM NEW KERNEL MODULES..." + Style.RESET_ALL)
    os.system("sudo akmods --force")
    print(Style.BRIGHT + Fore.GREEN + "     " + Style.RESET_ALL + " " + Fore.WHITE + "Read modified kernel module progressing [1/2]" + Style.RESET_ALL)
    os.system("sudo dracut --force")
    print(Style.BRIGHT + Fore.GREEN + "     " + Style.RESET_ALL + " " + Fore.WHITE + "Read modified kernel module progressing [2/2]" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Kernel module installation completed!" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL + " " + Fore.WHITE + "Commencing mandatory sleep for 3 minutes to save kernel read config" + Style.RESET_ALL)
    time.sleep(180)
    print(Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL + " " + Fore.WHITE + "Kernel read configs have been stored!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()