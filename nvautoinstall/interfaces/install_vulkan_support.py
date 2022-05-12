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
    Objc_HandleDriversInstallation,
    Objc_HandleRPMFusionRepositories,
    Objc_InstallVulkanSupport,
    failure,
    general,
    section,
    success,
    warning,
)


class InstallVulkanSupport:
    def __init__(self):
        section("CHECKING SUPERUSER PERMISSIONS...")
        if Objc_CheckSuperuserPermissions.main():
            success("Superuser privilege acquired")
            section("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if Objc_HandleRPMFusionRepositories.avbl():
                warning("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
                section("ATTEMPTING CONNECTION TO RPM FUSION SERVERS...")
                if Objc_HandleRPMFusionRepositories.conn():
                    success("Connection to RPM Fusion servers was established")
                    section("LOOKING FOR EXISTING DRIVER PACKAGES...")
                    data = Objc_HandleDriversInstallation.avbl()
                    if data is False:
                        failure("No existing NVIDIA driver packages were detected")
                        general(
                            "Please try executing `nvautoinstall driver` with elevated privileges before this"  # noqa
                        )
                    else:
                        qant = 0
                        for indx in data:
                            if indx != "":
                                qant += 1
                                general(indx)
                        warning("A total of " + str(qant) + " driver packages were detected")
                        section("INSTALLING VULKAN RENDERER SUPPORT...")
                        if Objc_InstallVulkanSupport.main():
                            success("Vulkan renderer support were successfully installed")
                        else:
                            failure("Vulkan renderer support could not be installed")
                            general(
                                "Please try executing `dnf update` with elevated privileges before this"  # noqa
                            )
                else:
                    failure("Connection to RPM Fusion servers could not be established")
                    general(
                        "Please check the internet connection or firewall configuration and try again"  # noqa
                    )
            else:
                failure("RPM Fusion repository for Proprietary NVIDIA Driver was not detected")
                general(
                    "Please try executing `nvautoinstall rpmadd` with elevated privileges before this"  # noqa
                )
        else:
            failure("Superuser privilege could not be acquired")
            general("Please try executing this command with elevated privileges")
        failure("Leaving installer")
        sys.exit(0)
