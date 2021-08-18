import os, subprocess, distro
from dataclasses import dataclass
from typing import Any, Union, Dict


@dataclass
class CollSupportCheck(object):
    @staticmethod
    def gpuc() -> Union[bool, Dict[str, Union[str, int, list[str]]]]:
        comand = "lspci | grep -E 'VGA|3D'"
        prompt = subprocess.Popen(comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = prompt.communicate()[0].decode("utf-8")
        linect = output.count("\n")
        pkname = output.split("\n")
        if "NVIDIA" in output:
            jsondt: Dict[str, Union[str, int, list[str]]] = {
                "supprt": "optimus" if linect != 1 else "single",
                "gpuqnt": linect,
                "gpulst": pkname,
            }
            return jsondt
        return False

    @staticmethod
    def system_info() -> dict[str, str]:
        jsondt = {
            "System": f"{os.uname().sysname} v {os.uname().release}",
            "Hostname": f"{os.uname().nodename}",
            "Version": f"{os.uname().version}",
            "Distribution": f"{distro.os_release_info()['name']} {os.uname().machine}",
        }
        return jsondt

    @staticmethod
    def avbl() -> Union[bool, str]:
        try:
            if f"{distro.os_release_info()['name']})" == "Fedora":
                return "full" if int(distro.os_release_info()["version_id"]) >= 32 else "half"
            return False
        except KeyError:
            return False
