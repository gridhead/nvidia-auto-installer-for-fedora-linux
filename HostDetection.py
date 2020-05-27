import os, distro, sys
from colorama import init
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("GATHERING ACTIVE INFORMATION...")
    DecoratorObject.SuccessMessage("Host information was gathered")
    datadict = {
        "System": str(os.uname().sysname) + " v" + str(os.uname().release),
        "Hostname": str(os.uname().nodename),
        "Version": str(os.uname().version),
        "Distribution": str(distro.os_release_info()["name"]) + " " + str(distro.os_release_info()["version_id"]) + " " + str(os.uname().machine),
    }
    for indx in datadict.keys():
        DecoratorObject.NormalMessage(indx + ": " + datadict[indx])
    if str(distro.os_release_info()["name"]) == "Fedora":
        if int(distro.os_release_info()["version_id"]) >= 32:
            DecoratorObject.SuccessMessage("Supported OS detected - " + datadict["Distribution"])
        else:
            DecoratorObject.WarningMessage("Minimally supported OS detected - " + datadict["Distribution"])
    else:
        DecoratorObject.FailureMessage("Unsupported OS detected - " + datadict["Distribution"])
        DecoratorObject.FailureMessage("Leaving installer")
        sys.exit(0)

if __name__ == "__main__":
    main()