import subprocess, sys
from colorama import init
from ColoramaCalls import StatusDecorator

init()
DecoratorObject = StatusDecorator()

def main():
    DecoratorObject.SectionHeader("CHECKING FOR GPU COMPATIBILITY...")
    comand = "lspci | grep -E 'VGA|3D'"
    prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = prompt.communicate()[0].decode("utf-8")
    linect = output.count("\n")
    pkname = output.split("\n")
    DecoratorObject.SuccessMessage("Compatibility infomation was obtained")
    for indx in pkname:
        if indx != "":
            DecoratorObject.NormalMessage(indx)
    if "NVIDIA" not in output:
        DecoratorObject.FailureMessage("No supported NVIDIA GPU was detected!")
        DecoratorObject.FailureMessage("Leaving installer with ERROR CODE - NVNF")
        sys.exit(0)
    else:
        DecoratorObject.SuccessMessage("An active NVIDIA GPU was detected!")
    if linect == 1:
        DecoratorObject.SuccessMessage("An single dedicated GPU setup was detected!")
    else:
        DecoratorObject.SuccessMessage("An Optimus Dual GPU setup was detected!")

if __name__ == "__main__":
    main()