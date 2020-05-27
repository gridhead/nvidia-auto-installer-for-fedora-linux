import os, sys, time
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("FORCING READ FROM NEW KERNEL MODULES...")
    DecoratorObject.NormalMessage("Read modified kernel module progressing [1/2]")
    ExecStatusCode01 = os.system("sudo akmods --force")
    if ExecStatusCode01 == 0:
        DecoratorObject.NormalMessage("Read modified kernel module progressing [2/2]")
        ExecStatusCode02 = os.system("sudo dracut --force")
        if ExecStatusCode02 == 0:
            DecoratorObject.SuccessMessage("Kernel module installation completed!")
            DecoratorObject.WarningMessage("Commencing mandatory sleep for 3 minutes to save kernel read config")
            #time.sleep(180)
            DecoratorObject.SuccessMessage("Kernel read configs have been stored!")
        else:
            DecoratorObject.FailureMessage("Reading modified kernel configs was terminated prematurely")
            DecoratorObject.FailureMessage("Leaving installer")
            sys.exit(0)
    else:
        DecoratorObject.FailureMessage("Reading modified kernel configs was terminated prematurely")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()