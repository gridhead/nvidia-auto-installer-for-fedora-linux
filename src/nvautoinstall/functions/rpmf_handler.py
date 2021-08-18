import os
import subprocess
from dataclasses import dataclass


@dataclass
class CollRPMFHandler(object):
    @staticmethod
    def avbl() -> bool:
        comand = "dnf repolist | grep 'rpmfusion-nonfree-nvidia-driver'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        return "rpmfusion-nonfree-nvidia-driver" in output

    def conn(self) -> int:
        retndata = subprocess.getstatusoutput("curl https://rpmfusion.org")[0]
        return retndata == 0

    def rpmf_repo_install(self):
        os.system("dnf install -y fedora-workstation-repositories")
        retndata = subprocess.getstatusoutput("dnf config-manager --set-enable rpmfusion-nonfree-nvidia-driver")[0]
        return retndata == 0