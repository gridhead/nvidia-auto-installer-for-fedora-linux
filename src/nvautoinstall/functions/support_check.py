import os, subprocess, distro
from dataclasses import dataclass
from typing import Any, Union, Dict
from nvautoinstall.handler.messages import nv_msgs
from nvautoinstall.functions.status_decorator import DecoratorObject


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
    def avbl() -> None:
        try:
            if f"{distro.os_release_info()['name']})" == "Fedora":
                if int(distro.os_release_info()["version_id"]) >= 32:
                    DecoratorObject.send_message("PASS", "Supported OS detected")
                    DecoratorObject.send_message("STDS", "This tool is expected to work correctly here")
                else:
                    DecoratorObject.send_message("WARN", "Minimally supported OS detected")
                    DecoratorObject.send_message("STDS", "Discretion is advised while using this tool")
            DecoratorObject.send_message("FAIL", "Unsupported OS detected")
            DecoratorObject.send_message("STDS", "This tool cannot be used here")
        except KeyError:
            DecoratorObject.send_message("FAIL", "Critical Error")