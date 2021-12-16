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

import distro


class HandleCompatibilityCheck(object):
    def gpuc(self):
        comand = "lspci | grep -E 'VGA|3D'"
        prompt = subprocess.Popen(
            comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        output = prompt.communicate()[0].decode("utf-8")
        linect = output.count("\n")
        pkname = output.split("\n")
        if "NVIDIA" not in output:
            return False
        else:
            if linect == 1:
                supprt = "single"
            else:
                supprt = "optims"
            jsondt = {
                "supprt": supprt,
                "gpuqnt": linect,
                "gpulst": pkname,
            }
            return jsondt

    def main(self):
        jsondt = {
            "System": str(os.uname().sysname) + " v" + str(os.uname().release),
            "Hostname": str(os.uname().nodename),
            "Version": str(os.uname().version),
            "Distribution": str(distro.os_release_info()["name"])
            + " "
            + str(os.uname().machine),
        }
        return jsondt

    def avbl(self):
        try:
            if distro.id() == "fedora":
                if int(distro.os_release_info()["version_id"]) >= 32:
                    return "full"
                else:
                    return "half"
            else:
                return False
        except KeyError:
            return False
