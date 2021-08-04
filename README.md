<h1 align="center">nvidia-auto-installer-for-fedora</h1>
<p align="center">A CLI tool which lets you install proprietary NVIDIA drivers and much more easily on Fedora 32 and above</p>

<p align="center">
    <img src="https://img.shields.io/github/issues/t0xic0der/nvidia-auto-installer-for-fedora?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/forks/t0xic0der/nvidia-auto-installer-for-fedora?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/stars/t0xic0der/nvidia-auto-installer-for-fedora?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/license/t0xic0der/nvidia-auto-installer-for-fedora?style=flat-square&logo=appveyor&color=teal">
</p>

## Requirements
* Active internet connection
* Fedora 32 or above

## Installation

If you use Fedora (32, 33, 34 ELN, Rawhide or above), CentOS (Stream 8 or above), RHEL (8 or above), Mageia (7, Cauldron or above), OpenSUSE (Leap or Tumbleweed) - you can install NVIDIA Auto Installer for Fedora by enabling my COPR repository. Simply execute the following commands in succession to install the tool.

```shell
# dnf install dnf-plugins-core -y
# dnf copr enable t0xic0der/nvidia-auto-installer-for-fedora -y
# dnf install nvautoinstall -y
```

## Usage
1. Make sure you have a working internet connection
2. Install the tool from COPR with the above instructions
3. Execute `nvautoinstall` to check installation modes
4. Run the installation modes according to your needs
5. Give stars to the repository if you found this helpful

## Modes of installation
Active internet connection and superuser privilege is required to execute the following installation modes.
- **`sudo nvautoinstall --rpmadd`**  
This mode enables the RPM Fusion NVIDIA drivers repository.
- **`sudo nvautoinstall --driver`**  
This mode simply installs the NVIDIA drivers (with x86_64 deps only). Enabling the RPM Fusion NVIDIA drivers repository is mandatory before doing this.
- **`sudo nvautoinstall --x86lib`**  
This mode installs only the x86 libraries for Xorg. Enabling the RPM Fusion NVIDIA drivers repository and installing the basic drivers are mandatory before doing this.
- **`sudo nvautoinstall --nvrepo`**  
This mode enables the official NVIDIA repository for CUDA software.
- **`sudo nvautoinstall --plcuda`**  
This mode installs only the CUDA support softwares. Enabling the RPM Fusion NVIDIA drivers and NVIDIA official repository, and installing the basic drivers are mandatory before doing this.
- **`sudo nvautoinstall --ffmpeg`**  
This mode installs only the FFMPEG accleration. Enabling the RPM Fusion NVIDIA drivers repository and installing the basic drivers are mandatory before doing this.
- **`sudo nvautoinstall --vulkan`**  
This mode installs only the Vulkan renderer. Enabling the RPM Fusion NVIDIA drivers repository and installing the basic drivers are mandatory before doing this.
- **`sudo nvautoinstall --vidacc`**  
This mode installs only the VDPAU/VAAPI acceleration. Enabling the RPM Fusion NVIDIA drivers repository and installing the basic drivers are mandatory before doing this.
- **`sudo nvautoinstall --getall`**  
This mode installs all the above packages. (Not been implemented yet)
- **`sudo nvautoinstall --cheksu`**  
This mode allows you to check the current user privilege level. You can use this tool effectively only when you have logged in as a root or sudo user.
- **`sudo nvautoinstall --compat`**  
This mode allows you to check your hardware and host compatiblity. The tool would check your hardware and host and tell if your device is supported by the tool or not.
- **`sudo nvautoinstall --version`**  
This mode would show the tool version and exit out.
- **`sudo nvautoinstall --help`**  
This mode would show the help message and exit out.

## Note
* Active internet connection is required to download drivers.
* Requires secure boot to be turned off in UEFI systems.
* Requires superuser access for repo addition and driver setup.
* The drivers are fetched from the RPMFusion repository.
* Use discretion while using this on other spins.
* Only tested on 9XX/10XX/20XX series discrete cards.
* Use discretion while installing with older cards.
* No additional configuration is required for Optimus setups.

## Coming soon
* CLI "Launch using Dedicated Graphics Card" option.
* Intuitive mode switching for hybrid graphics.
* Distinct mode for using integrated or discrete GPU.
* Experimental support for RHEL 8 and CentOS 8.
* Support for older cards by active querying at NVIDIA.
* Native support for PRIME configuration on Optimus.

## Disclaimer
This tool has been tried and tested multiple times and is expected to work flawlessly in Fedora Workstation 32 or above. It has not been tested on any of the spins yet so proceed with caution. While the chances of things going wrong is pretty slim but still you would want to make backups, should things do not go as expected. As always, you are choosing to use this tool at your will and you cannot hold me responsible for any mishap there may occur due to the misuse of this tool.
