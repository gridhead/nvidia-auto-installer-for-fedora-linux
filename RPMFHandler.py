import subprocess, os

def avbl():
    comand = "dnf repolist | grep 'rpmfusion-nonfree-nvidia-driver'"
    prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = prompt.communicate()[0].decode("utf-8")
    if "rpmfusion-nonfree-nvidia-driver" in output:
        return True
    else:
        return False

def conn():
    retndata = subprocess.getstatusoutput("ping -c 3 -W 3 rpmfusion.org")[0]
    if retndata == 0:
        return True
    else:
        return False

def main():
    os.system("dnf install -y fedora-workstation-repositories")
    retndata = subprocess.getstatusoutput("dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0]
    if retndata == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()