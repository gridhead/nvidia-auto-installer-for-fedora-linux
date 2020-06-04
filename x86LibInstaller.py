import os

def main():
    ExecStatusCode = os.system("dnf install -y xorg-x11-drv-nvidia-libs.i686")
    if ExecStatusCode == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()