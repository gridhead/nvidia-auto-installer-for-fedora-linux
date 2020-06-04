import os

def main():
    ExecStatusCode = os.system("dnf install -y xorg-x11-drv-nvidia-cuda-libs")
    if ExecStatusCode == 0:
        return True
    else:
        return False