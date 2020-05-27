import subprocess, os, sys
from colorama import init
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("FETCHING REPOSITORY DATA...")
    retndata = subprocess.getstatusoutput("sudo dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0]
    if retndata == 0:
        DecoratorObject.SuccessMessage("RPMFusion NVIDIA repository was enabled")
        os.system("sudo dnf update --refresh")
        DecoratorObject.SuccessMessage("Your packages have been updated")
    else:
        DecoratorObject.FailureMessage("RPMFusion NVIDIA repository could not be enabled")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()