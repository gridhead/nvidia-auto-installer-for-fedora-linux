import subprocess, os, sys
from colorama import init
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("FETCHING REPOSITORY DATA...")
    retndata = subprocess.getstatusoutput("dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0]
    if retndata == 0:
        DecoratorObject.SuccessMessage("RPM Fusion NVIDIA repository was enabled")
        os.system("dnf update --refresh")
        DecoratorObject.SuccessMessage("Your packages have been updated")
    else:
        DecoratorObject.FailureMessage("RPM Fusion NVIDIA repository could not be enabled")
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()