# nvidia-auto-installer-for-fedora-ws
A CLI tool which lets you install proprietary NVIDIA drivers in Fedora WS 32+

The CLI look and feel is heavily inspired from `systemd` and `eopkg` prompts.

## Note
* Requires secure boot to be turned off in UEFI systems.
* Requires superuser access for repo addition and driver setup.
* Active internet connection is required to download drivers.
* The drivers are fetched from the RPMFusion repository.
* Discrete cards from 9XX/10XX/20XX series only are supported.
* Native support for PRIME configuration is coming soon.
* No additional configuration is required for Optimus setups.
* Consider using executables provided in releases section only.

## Coming soon
* CLI "Launch using Dedicated Graphics Card" option.
* Intuitive mode switching for hybrid graphics.
* Distinct mode for using integrated or discrete GPU.
* Option to install CUDA, NVENC/NVDEC and more.