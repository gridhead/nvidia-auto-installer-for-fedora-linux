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


import click

from . import (
    CheckSuperuserPermissions,
    HandleCompatibilityCheck,
    HandleDriverInstallation,
    HandlePrimeSupport,
    HandleRPMFusionRepositories,
    InstallCudaSupport,
    InstallEverything,
    InstallFfmpegSupport,
    InstallNvidiaRepositories,
    InstallVideoAcceleration,
    InstallVulkanSupport,
    InstallCuBLASSupport,
    __version__,
)


@click.group(name="nvautoinstall")
@click.version_option(
    version=__version__,
    prog_name=click.style(
        "NVAutoInstall by Akashdeep Dhar <t0xic0der@fedoraproject.org>",
        fg="green",
        bold=True,
    ),
)
def main():
    click.echo(click.style("[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX", fg="green", bold=True))


@main.command(name="rpmadd", help="Enable the RPM Fusion NVIDIA drivers repository.")
def handle_rpmfusion_repositories():
    HandleRPMFusionRepositories()


@main.command(name="driver", help="Install the NVIDIA driver.")
def handle_driver_installation():
    HandleDriverInstallation()


@main.command(name="nvrepo", help="Enable the official NVIDIA repository for CUDA.")
def install_nvidia_repositories():
    InstallNvidiaRepositories()


@main.command(name="plcuda", help="Install only the CUDA support software.")
def install_cuda_support():
    InstallCudaSupport()


@main.command(name="ffmpeg", help="Install only the FFMPEG support software.")
def install_ffmpeg_support():
    InstallFfmpegSupport()


@main.command(name="vulkan", help="Install only the Vulkan support software.")
def install_vulkan_support():
    InstallVulkanSupport()


@main.command(name="vidacc", help="Install only the VDPAU/VAAPI acceleration.")
def install_video_acceleration():
    InstallVideoAcceleration()


@main.command(name="getall", help="Install all the above packages.")
def install_everything():
    InstallEverything()


@main.command(name="cheksu", help="Check the user privilege level.")
def check_superuser_permissions():
    CheckSuperuserPermissions()


@main.command(name="compat", help="Check your system compatibility.")
def handle_compatibility_check():
    HandleCompatibilityCheck()


@main.command(name="primec", help="Setup PRIME support.")
def handle_prime_support():
    HandlePrimeSupport()


@main.command(name="cublas", help="Setup CuBLAS library.")
@click.argument('version', type=str, required=True, default="latest")
def handle_cublas_support(version):
    InstallCuBLASSupport(version)


if __name__ == "__main__":
    main()
