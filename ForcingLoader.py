import os, sys, time
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("FORCING READ FROM NEW KERNEL MODULES...")
    os.system("sudo akmods --force")
    DecoratorObject.NormalMessage("Read modified kernel module progressing [1/2]")
    os.system("sudo dracut --force")
    DecoratorObject.NormalMessage("Read modified kernel module progressing [2/2]")
    DecoratorObject.SuccessMessage("Kernel module installation completed!")
    DecoratorObject.WarningMessage("Commencing mandatory sleep for 3 minutes to save kernel read config")
    time.sleep(180)
    DecoratorObject.SuccessMessage("Kernel read configs have been stored!")

if __name__ == "__main__":
    main()