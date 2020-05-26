import os, time
from colorama import init, Fore, Style
from ColoramaCalls import StatusDecorator

init()

def main():
    StatusDecorator.SectionHeader("INSTALLING PROPRIETARY DRIVERS...")
    os.system("sudo dnf install gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs")
    StatusDecorator.SuccessMessage("Driver package installation completed")
    StatusDecorator.WarningMessage("Commencing mandatory sleep for 5 minutes to load up kernel modules")
    time.sleep(300)
    StatusDecorator.SuccessMessage("Modified kernel modules have been loaded up")

if __name__ == "__main__":
    main()