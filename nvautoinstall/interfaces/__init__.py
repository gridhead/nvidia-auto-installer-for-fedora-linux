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


from nvautoinstall.decoration import failure, general, section, success, warning
from nvautoinstall.operations import (
    CheckSuperuserPermissions,
    HandleCompatibilityCheck,
    HandleCudaInstallation,
    HandleDriversInstallation,
    HandlePrimeSupport,
    HandleRPMFusionRepositories,
    InstallFfmpegSupport,
    InstallVideoAcceleration,
    InstallVulkanSupport,
)

__all__ = tuple(k for k in locals() if not k.startswith("_"))


Objc_CheckSuperuserPermissions = CheckSuperuserPermissions()
Objc_HandlePrimeSupport = HandlePrimeSupport()
Objc_HandleCompatibilityCheck = HandleCompatibilityCheck()
Objc_HandleCudaInstallation = HandleCudaInstallation()
Objc_HandleRPMFusionRepositories = HandleRPMFusionRepositories()
Objc_InstallFfmpegSupport = InstallFfmpegSupport()
Objc_HandleDriversInstallation = HandleDriversInstallation()
Objc_InstallVideoAcceleration = InstallVideoAcceleration()
Objc_InstallVulkanSupport = InstallVulkanSupport()
