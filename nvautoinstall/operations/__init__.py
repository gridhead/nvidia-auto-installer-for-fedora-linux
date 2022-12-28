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


from .check_superuser_permissions import CheckSuperuserPermissions  # noqa
from .handle_compatibility_check import HandleCompatibilityCheck  # noqa
from .handle_cuda_installation import HandleCudaInstallation  # noqa
from .handle_drivers_installation import HandleDriversInstallation  # noqa
from .handle_prime_support import HandlePrimeSupport  # noqa
from .handle_rpmfusion_repositories import HandleRPMFusionRepositories  # noqa
from .install_ffmpeg_support import InstallFfmpegSupport  # noqa
from .install_video_acceleration import InstallVideoAcceleration  # noqa
from .install_vulkan_support import InstallVulkanSupport  # noqa
from .install_cublas_support import InstallCuBLASSupport  # noqa
from .install_cudnn_support import InstallCuDNNSupport  # noqa
