# nvidia-auto-installer-for-fedora
A CLI tool which lets you install proprietary NVIDIA drivers easily in Fedora 32+

![](v0.2.0-screenshot.png)

The look and feel is heavily inspired from `systemd` and `eopkg` prompts.

## Requirements
* Active internet connection
* Fedora 32 or above

## Usage
1. Make sure you have a working internet connection
2. Download `NVAutoInstFedora32` from releases
3. Execute `./NVAutoInstFedora32` to install drivers
4. Give stars to the repository if you found this helpful

## Note
* Active internet connection is required to download drivers.
* Requires secure boot to be turned off in UEFI systems.
* Requires superuser access for repo addition and driver setup.
* The drivers are fetched from the RPMFusion repository.
* Only tested on Fedora 32 Workstation.
* Use discretion while using this on other spins.
* Only tested on 9XX/10XX/20XX series discrete cards.
* Use discretion while installing with older cards.
* No additional configuration is required for Optimus setups.
* Consider using executables provided in releases section only.

## Coming soon
* CLI "Launch using Dedicated Graphics Card" option.
* Intuitive mode switching for hybrid graphics.
* Distinct mode for using integrated or discrete GPU.
* Option to install CUDA, NVENC/NVDEC and more.
* Experimental support for RHEL 8 and CentOS 8.
* Support for older cards by active querying at NVIDIA.
* Native support for PRIME configuration on Optimus.

## Disclaimer
This tool has been tried and tested multiple times and is expected to work flawlessly in Fedora Workstation 32 or above. It has not been tested on any of the spins yet so proceed with caution. While the chances of things going wrong is pretty slim but still you would want to make backups, should things do not go as expected. As always, you are choosing to use this tool at your will and you cannot hold me responsible for any mishap there may occur due to the misuse of this tool.