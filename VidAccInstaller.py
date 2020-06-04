import os

def main():
    ExecStatusCode = os.system("dnf install -y vdpauinfo libva-vdpau-driver libva-utils")
    if ExecStatusCode == 0:
        return True
    else:
        return False