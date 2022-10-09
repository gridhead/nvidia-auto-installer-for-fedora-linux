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
    Objc_HandleCudaInstallation,
    failure,
    general,
    section,
    success,
    warning,
)


class InstallNvidiaRepositories:
    def __init__(self, repover: str):
        self.repovers = [
            "f32",
            "F32",
            "f33",
            "F33",
            "f34",
            "F34",
            "f35",
            "F35",
            "f36",
            "F36",
        ]
        if repover not in self.repovers:
            warning("Invalid fedora version argument")
            general("Example usage: \n  sudo nvautoinstall nvrepo f36")
            sys.exit(0)
        section("CHECKING SUPERUSER PERMISSIONS...")
        if Objc_CheckSuperuserPermissions.main():
            success("Superuser privilege acquired")
            section("CHECKING AVAILABILITY OF OFFICIAL CUDA REPOSITORY...")
            if Objc_HandleCudaInstallation.rpck():
                warning("Official CUDA repository was detected")
                general(
                    "Please try executing \
                    `nvautoinstall plcuda` with \
                    elevated privileges now to install CUDA software"
                )
                success("No further action is necessary")
            else:
                warning("Official CUDA repository was not detected")
                warning("Repository enabling is required")
                section("ATTEMPTING CONNECTION TO NVIDIA SERVERS...")
                if Objc_HandleCudaInstallation.conn():
                    success("Connection to NVIDIA servers was established")
                    section("INSTALLING OFFICIAL CUDA REPOSITORY...")
                    if Objc_HandleCudaInstallation.rpin(repover):
                        success("Official CUDA repository was enabled")
                        section("REFRESHING REPOSITORY LIST...")
                        if Objc_HandleCudaInstallation.rpup():
                            success("Repositories have been refreshed")
                            section("DISABLING NVIDIA DRIVER MODULE...")
                            if Objc_HandleCudaInstallation.stop():
                                success("NVIDIA DRIVER module has been disabled")
                                general(
                                    "Please try executing `nvautoinstall plcuda` with \
                                        elevated privileges now to install CUDA software"
                                )
                            else:
                                failure("NVIDIA DRIVER module could not be disabled")
                                general(
                                    "Please try executing `dnf update` with \
                                        elevated privileges before this"
                                )
                        else:
                            failure("Repositories could not be refreshed")
                            general(
                                "Please try executing `dnf update` with \
                                    elevated privileges before this"
                            )
                    else:
                        failure("Official CUDA repository could not be enabled")
                        general(
                            "Please try executing `dnf update` with \
                                elevated privileges before this"
                        )
                else:
                    failure("Connection to NVIDIA servers could not be established")
                    general(
                        "Please check the internet connection or \
                            firewall configuration and try again"
                    )
        else:
            failure("Superuser privilege could not be acquired")
            general("Please try executing this command with elevated privileges")
        failure("Leaving installer")
        sys.exit(0)
