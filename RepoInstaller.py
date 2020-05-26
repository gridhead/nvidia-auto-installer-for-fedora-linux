import subprocess, os, sys
from ColoramaCalls import StatusDecorator

init()

def main():
    StatusDecorator.SectionHeader("FETCHING REPOSITORY DATA...")
    retndata = subprocess.getstatusoutput("sudo dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0]
    if retndata == 0:
        StatusDecorator.SuccessMessage("RPMFusion NVIDIA repository was enabled")
        os.system("sudo dnf update --refresh")
        StatusDecorator.SuccessMessage("Your packages have been updated")
    else:
        StatusDecorator.FailureMessage("RPMFusion NVIDIA repository could not be enabled")
        StatusDecorator.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()