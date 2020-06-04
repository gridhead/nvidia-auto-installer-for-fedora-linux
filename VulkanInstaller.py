import os

def main():
    ExecStatusCode = os.system("dnf install -y vulkan")
    if ExecStatusCode == 0:
        return True
    else:
        return False