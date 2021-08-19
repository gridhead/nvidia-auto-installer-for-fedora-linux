from dataclasses import dataclass
from nvautoinstall.functions.status_decorator import DecoratorObject
from nvautoinstall.handler.messages import nv_msgs
import subprocess
import os


@dataclass
class CollDriverInstaller:
    @staticmethod
    def main():
        return os.system("dnf install -y gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs") == 0

    @staticmethod
    def avbl():
        DecoratorObject.send_message("HEAD", nv_msgs.get("looking_existing_driver_packages"), "magenta", True)
        comand = "rpm -qa | grep 'nvidia'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        linect = output.count("\n")
        if linect != 0:
            pkname = output.split("\n")
            return pkname
        return False


class CollX86LibInstaller(object):
    @staticmethod
    def main():
        return os.system("dnf install -y xorg-x11-drv-nvidia-libs.i686") == 0


class CollPlCudaInstaller(object):
    @staticmethod
    def rpck():
        comand = "dnf repolist | grep 'cuda'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        return "cuda" in output

    @staticmethod
    def rpin():
        return (
            subprocess.getstatusoutput("dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/fedora33/x86_64/cuda-fedora33.repo")[0]
            == 0
        )

    @staticmethod
    def conn():
        retndata = subprocess.getstatusoutput("curl https://developer.download.nvidia.com/compute/cuda/repos/")[0]
        return retndata == 0

    @staticmethod
    def rpup():
        return os.system("dnf clean all") == 0

    @staticmethod
    def meta():
        return os.system("dnf install -y xorg-x11-drv-nvidia-cuda") == 0

    @staticmethod
    def stop():
        return os.system("dnf module disable -y nvidia-driver") == 0

    @staticmethod
    def main():
        return os.system("dnf install -y cuda") == 0


class CollFFMPEGInstaller(object):
    @staticmethod
    def main():
        return os.system("dnf install -y xorg-x11-drv-nvidia-cuda-libs") == 0


class CollVidAccInstaller(object):
    @staticmethod
    def main():
        return os.system("dnf install -y vdpauinfo libva-vdpau-driver libva-utils") == 0


class CollVulkanInstaller(object):
    @staticmethod
    def main():
        return os.system("dnf install -y vulkan") == 0
