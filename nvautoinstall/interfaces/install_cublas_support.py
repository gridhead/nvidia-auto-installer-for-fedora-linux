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
    Objc_HandleCuBLASInstallation,
    Objc_HandleCudaInstallation,
    failure,
    general,
    section,
    success,
    warning,
)


class InstallCuBLASSupport:
    """
    Interface to install the CuBLAS library.
    """
    def __init__(self, version):
        section("CHECKING SUPERUSER PERMISSIONS...")
        if Objc_CheckSuperuserPermissions.main():
            success("Superuser privilege acquired")
            section("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...")
            if Objc_HandleRPMFusionRepositories.avbl():
                success("RPM Fusion repository for Proprietary NVIDIA Driver was detected")
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
                        if qant == 0:
                            report_fn = warning
                        else:
                            report_fn = success
                        report_fn("A total of " + str(qant) + " driver packages were detected")

                        section("LOOKING FOR EXISTING CUDA INSTALLATION...")
                        if Objc_HandleCudaInstallation.avbl():
                            success("CUDA support software was detected")
                            section("INSTALLING CuBLAS LIBRARY...")
                            detected_versions, package_name = Objc_HandleCuBLASInstallation.search(version)
                            if package_name is not None:
                                success("Found CuBLAS package " + package_name)
                                section("INSTALLING CuBLAS PACKAGE...")
                                if Objc_HandleCuBLASInstallation.main(package_name):
                                    success("CuBLAS library were successfully installed")
                                else:
                                    failure("CuBLAS library could not be installed")
                                    general(
                                        "Please try executing `dnf update` with elevated privileges before this"  # noqa
                                    )
                            else:
                                failure("CuBLAS library matching version " + version + " was not found. Detected versions:\n" + "\n".join("      * " + v for v in detected_versions))
                                general(
                                    "Please check the version number and try again"  # noqa
                                )
                        else:
                            failure("CUDA support software was not detected")
                            general(
                                "Please try executing `nvautoinstall plcuda` with elevated privileges before this"  # noqa
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
