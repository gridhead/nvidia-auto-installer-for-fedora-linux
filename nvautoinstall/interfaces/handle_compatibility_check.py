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


import sys

from . import Objc_HandleCompatibilityCheck, failure, general, section, success, warning


class HandleCompatibilityCheck:
    def __init__(self):
        section("CHECKING FOR GPU COMPATIBILITY...")
        data = Objc_HandleCompatibilityCheck.gpuc()
        warning("Compatibility infomation was obtained")
        if data is False:
            failure("No supported NVIDIA GPU was detected")
            general("This tool is supported only on devices having one or more active NVIDIA GPUs")
        else:
            success("One or more active NVIDIA GPUs were detected")
            supprt = data["supprt"]
            gpulst = data["gpulst"]
            for indx in gpulst:
                if indx != "":
                    general(indx)
            if supprt == "single":
                success("A single dedicated GPU setup was detected")
            else:
                success("An Optimus Dual GPU setup was detected")
            section("GATHERING CURRENT HOST INFORMATION...")
            data = Objc_HandleCompatibilityCheck.main()
            warning("Host information was gathered")
            for indx in data.keys():
                general(indx + ": " + data[indx])
            section("CHECKING FOR HOST COMPATIBILITY...")
            data = Objc_HandleCompatibilityCheck.avbl()
            if data is False:
                failure("Unsupported OS detected")
                general("This tool cannot be used here")
            else:
                if data:
                    success("Supported OS detected")
                    general("This tool is expected to work correctly here")
                else:
                    warning("Minimally supported OS detected")
                    general("Discretion is advised while using this tool")
        failure("Leaving installer")
        sys.exit(0)
