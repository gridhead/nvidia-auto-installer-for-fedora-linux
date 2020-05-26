import os
from colorama import init
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("GATHERING ACTIVE INFORMATION...")
    DecoratorObject.SuccessMessage("Host information was gathered")
    datadict = {
        "System": str(os.uname().sysname),
        "Hostname": str(os.uname().nodename),
        "Release": str(os.uname().release),
        "Version": str(os.uname().version),
        "Machine": str(os.uname().machine),
    }
    for indx in datadict.keys():
        DecoratorObject.NormalMessage(indx + ": " + datadict[indx])

if __name__ == "__main__":
    main()