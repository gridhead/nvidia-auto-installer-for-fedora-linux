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
import os

REPO_URL = "https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo"


class InstallCuDNNSupport(object):
    """
    Install the CuDNN library.
    """

    def add_repo(self):
        exit_code = os.system("dnf config-manager --add-repo " + REPO_URL)
        return exit_code == 0

    def repo_installed(self):
        comand = "dnf repolist | grep 'cuda-rhel8'"
        prompt = subprocess.Popen(
            comand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        output = prompt.communicate()[0].decode("utf-8")
        return "cuda-rhel8" in output

    def search(self, version):
        """
        Search for a libcudnn* package that matches the provided version number.
        version should be a number matching the distributions on the RHEL 8 repo,
        or "latest" to get the most recent available version.
        """
        command = "dnf search libcudnn -q | grep -v devel"
        prompt = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        output = prompt.communicate()[0].decode("utf-8")
        lines = output.splitlines()
        assert lines[0].startswith("====="), lines[0]
        lines = lines[1:]
        packages = [l.split(" : ")[0] for l in lines]
        version_numbers = [p[len("libcudnn"):p.rindex(".")] for p in packages]
        if len(version_numbers) == 0:
            return version_numbers, None
        if version == "latest":
            version_to_install = version_numbers[-1]
        else:
            version_to_install = next((v for v in version_numbers if v == version), None)
        if version_to_install is None:
            return version_numbers, None
        package_to_install = "libcudnn" + version_to_install
        return version_numbers, package_to_install

    def main(self, package_name):
        exit_code = os.system("dnf install " + package_name)
        return exit_code == 0
