import os, subprocess

def rpck():
    comand = "dnf repolist | grep 'cuda'"
    prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = prompt.communicate()[0].decode("utf-8")
    if "cuda" in output:
        return True
    else:
        return False

def rpin():
    retndata = subprocess.getstatusoutput("dnf config-manager --add-repo http://developer.download.nvidia.com/compute/cuda/repos/fedora29/x86_64/cuda-fedora29.repo")[0]
    print(retndata)
    if retndata == 0:
        return True
    else:
        return False

def conn():
    retndata = subprocess.getstatusoutput("ping -c 3 -W 3 developer.download.nvidia.com")[0]
    if retndata == 0:
        return True
    else:
        return False

def rpup():
    ExecStatusCode = os.system("dnf clean all")
    if ExecStatusCode == 0:
        return True
    else:
        return False

def meta():
    ExecStatusCode = os.system("dnf install -y xorg-x11-drv-nvidia-cuda")
    if ExecStatusCode == 0:
        return True
    else:
        return False

def main():
    ExecStatusCode = os.system("dnf install -y cuda")
    if ExecStatusCode == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()