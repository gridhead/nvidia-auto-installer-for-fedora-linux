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


import subprocess


class InstallCuBLASSupport(object):
    def search(self, version):
        # print("TODO: INSTALL CUBLAS VERSION", version)
        command = "dnf search libcublas -q | grep -v devel"
        prompt = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        output = prompt.communicate()[0].decode("utf-8")
        lines = output.splitlines()
        assert lines[0].startswith("====="), lines[0]
        # print("dnf search:", lines)
        lines = lines[1:]
        packages = [l.split(" : ")[0] for l in lines]
        version_numbers = [p[p.index("-")+1:p.rindex(".")] for p in packages]
        # print("versions:", version_numbers)
        if len(version_numbers) == 0:
            return version_numbers, None
        if version == "latest":
            version_to_install = version_numbers[-1]
        else:
            version_to_install = next((v for v in version_numbers if v == version), None)
        if version_to_install is None:
            return version_numbers, None
        package_to_install = "libcublas-" + version_to_install
        print("MATCHED PACKAGE", version_to_install, package_to_install)
        return version_numbers, package_to_install

    def main(self, package_name):
        print("TODO: INSTALL", package_name)
        return True
