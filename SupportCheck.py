import subprocess, sys
from colorama import init
from ColoramaCalls import StatusDecorator

init()

def main():
    StatusDecorator.SectionHeader("CHECKING FOR GPU COMPATIBILITY...")
    comand = "lspci | grep -E 'VGA|3D'"
    prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = prompt.communicate()[0].decode("utf-8")
    linect = output.count("\n")
    pkname = output.split("\n")
    StatusDecorator.SuccessMessage("Compatibility infomation was obtained")
    for indx in pkname:
        if indx != "":
            StatusDecorator.NormalMessage(indx)
    if "NVIDIA" not in output:
        StatusDecorator.FailureMessage("No supported NVIDIA GPU was detected!")
        StatusDecorator.FailureMessage("Leaving installer with ERROR CODE - NVNF")
        sys.exit(0)
    else:
        StatusDecorator.SuccessMessage("An active NVIDIA GPU was detected!")
    if linect == 1:
        StatusDecorator.SuccessMessage("An single dedicated GPU setup was detected!")
    else:
        StatusDecorator.SuccessMessage("An Optimus Dual GPU setup was detected!")

if __name__ == "__main__":
    main()