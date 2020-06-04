import os, subprocess

def main():
    ExecStatusCode = os.system("dnf install -y gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs")
    if ExecStatusCode == 0:
        return True
    else:
        return False

def avbl():
    comand = "rpm -qa | grep 'nvidia'"
    prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = prompt.communicate()[0].decode("utf-8")
    linect = output.count("\n")
    if linect == 0:
        return False
    else:
        pkname = output.split("\n")
        return pkname

if __name__ == "__main__":
    main()