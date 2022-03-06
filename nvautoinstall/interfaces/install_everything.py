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

from . import Objc_CheckSuperuserPermissions, failure, general, section, success


class InstallEverything:
    def __init__(self):
        section("CHECKING SUPERUSER PERMISSIONS...")
        if Objc_CheckSuperuserPermissions.main():
            success("Superuser privilege acquired")
            section("FULL FLEDGED INSTALLATION BEGINNING...")
            general("This mode is yet to be implemented")
        else:
            failure("Superuser privilege could not be acquired")
        failure("Leaving installer")
        sys.exit(0)
