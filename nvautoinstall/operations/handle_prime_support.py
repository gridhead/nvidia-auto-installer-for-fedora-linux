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


class HandlePrimeSupport(object):
    def main(self, opts):
        try:
            with open("/usr/share/X11/xorg.conf.d/nvidia.conf", "r") as sharconf:
                shardata = sharconf.read()
            primemod = ""
            for indx in shardata.split("\n"):
                primemod += indx + "\n"
                if opts is True and indx == '\tOption "BaseMosaic" "on"':
                    primemod += '\tOption "PrimaryGPU" "yes"' + "\n"
            with open("/etc/X11/xorg.conf.d/nvidia.conf", "w") as etcdconf:
                etcdconf.write(primemod)
            return True
        except Exception:
            return False
