"""
##########################################################################
*
*   Copyright © 2019-2021 Akashdeep Dhar <t0xic0der@fedoraproject.org>
*
*   This program is free software: you can redistribute it and/or modify
*   it under the terms of the GNU General Public License as published by
*   the Free Software Foundation, either version 3 of the License, or
*   (at your option) any later version.
*
*   This program is distributed in the hope that it will be useful,
*   but WITHOUT ANY WARRANTY; without even the implied warranty of
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*   GNU General Public License for more details.
*
*   You should have received a copy of the GNU General Public License
*   along with this program.  If not, see <https://www.gnu.org/licenses/>.
*
##########################################################################
"""

from nvautoinstall.functions.install_mode import InstallationMode
from nvautoinstall.functions.status_decorator import DecoratorObject
from nvautoinstall.functions.checksu import SuperuserCheck
import click


try:
    # Imports version in the packaged environment
    from nvautoinstall import __version__, __author__
except ModuleNotFoundError:
    # Imports version in the development environment
    from __init__ import __version__, __author__


@click.command()
@click.option("--rpmadd", "instmode", flag_value="rpmadd", help="This mode enables the RPM Fusion NVIDIA drivers repository.")
@click.option("--driver", "instmode", flag_value="driver", help="This mode simply installs the NVIDIA driver.")
@click.option("--x86lib", "instmode", flag_value="x86lib", help="This mode installs only the x86 libraries for Xorg.")
@click.option("--nvrepo", "instmode", flag_value="nvrepo", help="This mode enables the Official NVIDIA repository for CUDA.")
@click.option("--plcuda", "instmode", flag_value="plcuda", help="This mode installs only the CUDA support softwares.")
@click.option("--ffmpeg", "instmode", flag_value="ffmpeg", help="This mode installs only the FFMPEG acceleration.")
@click.option("--vulkan", "instmode", flag_value="vulkan", help="This mode installs only the Vulkan renderer.")
@click.option("--vidacc", "instmode", flag_value="vidacc", help="This mode installs only the VDPAU/VAAPI acceleration.")
@click.option("--getall", "instmode", flag_value="getall", help="This mode installs all the above packages.")
@click.option("--checksu", "instmode", flag_value="checksu", help="This mode allows you to check the user privilege level.")
@click.option("--compat", "instmode", flag_value="compat", help="This mode allows you to check your compatibility.")
@click.option("--primec", "instmode", flag_value="primec", help="This mode allows you to setup PRIME configuration.")
@click.version_option(
    version=__version__,
    prog_name=click.style(__author__, fg="green", bold=True),
)
def main(instmode):
    DecoratorObject.send_message("HEAD", "CHECKING SUPERUSER PERMISSIONS...", "magenta", True)
    if SuperuserCheck.main():
        DecoratorObject.send_message("PASS", "Superuser privilege acquired")
    else:
        DecoratorObject.send_message("FAIL", "Superuser privilege could not be acquired")

    instobjc = InstallationMode()
    click.echo(click.style("[ # ] NVIDIA AUTOINSTALLER FOR FEDORA", fg="green", bold=True))

    instmode_dict: dict[str, InstallationMode] = {
        "rpmadd": instobjc.rpmadd(),
        "driver": instobjc.driver(),
        "x86lib": instobjc.x86lib(),
        "nvrepo": instobjc.nvrepo(),
        "checksu": instobjc.checksu(),
        "compat": instobjc.compat(),
        "primec": instobjc.primec(),
        "plcuda": instobjc.plcuda(),
        "ffmpeg": instobjc.ffmpeg(),
        "vulkan": instobjc.vulkan(),
        "vidacc": instobjc.vidacc(),
        "getall": instobjc.getall(),
    }
    instobjc.lsmenu() if not instmode_dict.get[instmode] else instmode_dict.get(instmode)


if __name__ == "__main__":
    main()
