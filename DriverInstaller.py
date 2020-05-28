import os, sys, time
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("INSTALLING PROPRIETARY DRIVERS...")
    ExecStatusCode = os.system("dnf install -y gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs xorg-x11-drv-nvidia-libs.i686")
    if ExecStatusCode == 0:
        DecoratorObject.SuccessMessage("Driver package installation completed")
        DecoratorObject.WarningMessage("Kernel modules would be built up on the next boot")
    else:
        DecoratorObject.FailureMessage("Could not install proprietary drivers")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()