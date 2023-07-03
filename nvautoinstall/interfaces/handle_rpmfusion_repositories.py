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

from . import (
    Objc_CheckSuperuserPermissions,
    Objc_HandleRPMFusionRepositories,
    failure,
    general,
    section,
    success,
    warning,
)


class HandleRPMFusionRepositories:
    def __init__(self):
        section("CHECKING SUPERUSER PERMISSIONS...")
        if Objc_CheckSuperuserPermissions.main():
            success("Superuser privilege acquired")
            section("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if Objc_HandleRPMFusionRepositories.avbl():
                warning(
                    "RPM Fusion repository for                     Proprietary NVIDIA Driver was"
                    " detected"
                )
                general(
                    "Please try executing `nvautoinstall driver`"
                    "with elevated privileges now to install the drivers"
                )
                success("No further action is necessary")
            else:
                warning(
                    "RPM Fusion repository for                         Proprietary NVIDIA Driver"
                    " was not detected"
                )
                warning("Repository enabling is required")
                section("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if Objc_HandleRPMFusionRepositories.conn():
                    success("Connection to RPM Fusion servers was established")
                    section("INSTALLING RPM FUSION NVIDIA REPOSITORY...")
                    if Objc_HandleRPMFusionRepositories.main():
                        success("RPM Fusion NVIDIA repository was enabled")
                        general(
                            "Please try executing `nvautoinstall driver`"
                            "with elevated privileges now to install the drivers"
                        )
                    else:
                        failure("RPM Fusion NVIDIA repository could not be enabled")
                        general(
                            "Please try executing `dnf update` with elevated privileges before this"
                        )
                else:
                    failure("Connection to RPM Fusion servers could not be established")
                    general(
                        "Please check the internet connection or firewall configuration and try"
                        " again"
                    )
        else:
            failure("Superuser privilege could not be acquired")
            general("Please try executing this command with elevated privileges")
        failure("Leaving installer")
        sys.exit(0)
