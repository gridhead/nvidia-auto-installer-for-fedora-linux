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

import os


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
            # KDE SDDM needs to be configured appropriately
            if os.environ["XDG_CURRENT_DESKTOP"] == "KDE":
                x_setup = "/etc/sddm/Xsetup"
                with open(x_setup, "r") as xsetup_read:
                    # Prevents adding it twice when called multiple times
                    if "# KDE SDDM setup" not in xsetup_read.read():
                        with open(x_setup, "a") as xsetup_append:
                            xsetup_append.write("\n# KDE SDDM setup")
                            xsetup_append.write("\nxrandr --setprovideroutputsource modesetting NVIDIA-G0")
                            xsetup_append.write("\nxrandr --auto")
            return True
        except Exception:
            return False
