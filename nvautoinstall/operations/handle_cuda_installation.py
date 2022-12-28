"""
NVIDIA Auto Installer for Fedora Linux
Copyright (C) 2019-2021 Akashdeep Dhar

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import os
import subprocess
import re


MAIN_PACKAGE_NAME = "cuda"
META_PACKAGE_NAME = "xorg-x11-drv-nvidia-cuda"


class HandleCudaInstallation(object):
    def avbl(self):
        """
        Check whether both main and meta packages are installed.
        """
        command = "dnf list installed | grep cuda"
        prompt = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        output = prompt.communicate()[0].decode("utf-8")
        lines = output.splitlines()
        linect = len(lines)
        if linect == 0:
            return False
        else:
            meta_installed = any(re.match(META_PACKAGE_NAME, line) for line in lines)
            main_installed = any(re.match(MAIN_PACKAGE_NAME, line) for line in lines)
            return meta_installed and main_installed

    def rpck(self):
        comand = "dnf repolist | grep 'cuda'"
        prompt = subprocess.Popen(
            comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        output = prompt.communicate()[0].decode("utf-8")
        return "cuda" in output

    def rpin(self):
        retndata = subprocess.getstatusoutput(
            "dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/fedora35/x86_64/cuda-fedora35.repo"  # noqa
        )[0]
        return retndata == 0

    def conn(self):
        retndata = subprocess.getstatusoutput(
            "curl https://developer.download.nvidia.com/compute/cuda/repos/"
        )[0]
        return retndata == 0

    def rpup(self):
        exec_status_code = os.system("dnf clean all")
        return exec_status_code == 0

    def meta(self):
        exec_status_code = os.system("dnf install -y " + META_PACKAGE_NAME)
        return exec_status_code == 0

    def stop(self):
        exec_status_code = os.system("dnf module disable -y nvidia-driver")
        return exec_status_code == 0

    def main(self):
        exec_status_code = os.system("dnf install -y " + MAIN_PACKAGE_NAME)
        return exec_status_code == 0
