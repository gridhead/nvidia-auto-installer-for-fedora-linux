import os, sys, time
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()

def main():
    StatusDecorator.SectionHeader("FORCING READ FROM NEW KERNEL MODULES...")
    os.system("sudo akmods --force")
    StatusDecorator.NormalMessage("Read modified kernel module progressing [1/2]")
    os.system("sudo dracut --force")
    StatusDecorator.NormalMessage("Read modified kernel module progressing [2/2]")
    StatusDecorator.SuccessMessage("Kernel module installation completed!")
    StatusDecorator.WarningMessage("Commencing mandatory sleep for 3 minutes to save kernel read config")
    time.sleep(180)
    StatusDecorator.SuccessMessage("Kernel read configs have been stored!")

if __name__ == "__main__":
    main()