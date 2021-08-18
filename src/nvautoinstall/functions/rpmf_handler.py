import os
import subprocess
from dataclasses import dataclass
from nvautoinstall.handler.messages import nv_msgs
from nvautoinstall.functions.status_decorator import DecoratorObject


@dataclass
class CollRPMFHandler(object):
    @staticmethod
    def avbl() -> bool:
        DecoratorObject.send_message("HEAD", nv_msgs.get("checking_rpm_fusion_nvidia_repository"), "magenta", True)
        comand = "dnf repolist | grep 'rpmfusion-nonfree-nvidia-driver'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        return "rpmfusion-nonfree-nvidia-driver" in output

    def conn(self) -> int:
        DecoratorObject.send_message("HEAD", nv_msgs.get("attempting_connection_to_rpm_server"), "magenta", True)
        return subprocess.getstatusoutput("curl https://rpmfusion.org")[0] == 0

    def rpmf_repo_install(self) -> int:
        os.system("dnf install -y fedora-workstation-repositories")
        return subprocess.getstatusoutput("dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0] == 0