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


from .interfaces.check_superuser_permissions import CheckSuperuserPermissions  # noqa
from .interfaces.handle_compatibility_check import HandleCompatibilityCheck  # noqa
from .interfaces.handle_drivers_installation import HandleDriverInstallation  # noqa
from .interfaces.handle_prime_support import HandlePrimeSupport  # noqa
from .interfaces.handle_rpmfusion_repositories import HandleRPMFusionRepositories  # noqa
from .interfaces.install_cuda_support import InstallCudaSupport  # noqa
from .interfaces.install_everything import InstallEverything  # noqa
from .interfaces.install_ffmpeg_support import InstallFfmpegSupport  # noqa
from .interfaces.install_nvidia_repositories import InstallNvidiaRepositories  # noqa
from .interfaces.install_video_acceleration import InstallVideoAcceleration  # noqa
from .interfaces.install_vulkan_support import InstallVulkanSupport  # noqa
from .interfaces.install_cublas_support import InstallCuBLASSupport  # noqa
from .interfaces.install_cudnn_support import InstallCuDNNSupport  # noqa

__version__ = "0.4.1"
