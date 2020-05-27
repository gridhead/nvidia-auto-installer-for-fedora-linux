import os, sys, time
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("INSTALLING PROPRIETARY DRIVERS...")
    ExecStatusCode = os.system("dnf install -y gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs")
    if ExecStatusCode == 0:
        DecoratorObject.SuccessMessage("Driver package installation completed")
        DecoratorObject.WarningMessage("Commencing mandatory sleep for 5 minutes to load up kernel modules")
        time.sleep(300)
        DecoratorObject.SuccessMessage("Modified kernel modules have been loaded up")
    else:
        DecoratorObject.FailureMessage("Could not install proprietary drivers")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()