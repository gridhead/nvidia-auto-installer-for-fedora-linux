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


class HandleRPMFusionRepositories(object):
    def avbl(self):
        comand = "dnf repolist | grep 'rpmfusion-nonfree-updates'"
        prompt = subprocess.Popen(
            comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        output = prompt.communicate()[0].decode("utf-8")
        return "rpmfusion-nonfree-updates" in output

    def conn(self):
        retndata = subprocess.getstatusoutput("curl https://rpmfusion.org")[0]
        return retndata == 0

    def main(self):
        os.system("dnf install -y fedora-workstation-repositories")
        os.system(
            "dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm"
        )
        os.system(
            "dnf install -y https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm"
        )
        retndata = subprocess.getstatusoutput(
            "dnf config-manager --set-enable rpmfusion-free rpmfusion-free-updates rpmfusion-nonfree rpmfusion-nonfree-updates"
        )[0]
        return retndata == 0
