import os

def main():
    ExecStatusCode = os.system("dnf install -y gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs")
    if ExecStatusCode == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()