<h1 align="center">NVIDIA Auto Installer for Fedora Linux</h1>
<p align="center">A CLI tool which lets you install proprietary NVIDIA drivers and much more easily on Fedora Linux (32 or above and Rawhide)</p>

<p align="center">
    <img src="https://img.shields.io/github/issues/t0xic0der/nvidia-auto-installer-for-fedora-linux?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/forks/t0xic0der/nvidia-auto-installer-for-fedora-linux?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/stars/t0xic0der/nvidia-auto-installer-for-fedora-linux?style=flat-square&logo=appveyor&color=teal">
    <img src="https://img.shields.io/github/license/t0xic0der/nvidia-auto-installer-for-fedora-linux?style=flat-square&logo=appveyor&color=teal">
</p>

<p align="center">
    <a href="https://copr.fedorainfracloud.org/coprs/t0xic0der/nvidia-auto-installer-for-fedora/package/nvautoinstall/"><img src="https://copr.fedorainfracloud.org/coprs/t0xic0der/nvidia-auto-installer-for-fedora/package/nvautoinstall/status_image/last_build.png" /></a>
</p>

### Requirements
* Active internet connection
* Fedora Linux (32 or above and Rawhide)
* Device with a discrete NVIDIA GPU

### Installation
If you use Fedora Linux (32 or above and Rawhide) - you can install NVIDIA Auto Installer for Fedora by enabling my 
COPR repository. Simply execute the following commands in succession to install the tool.

```shell
# dnf install dnf-plugins-core -y
# dnf copr enable t0xic0der/nvidia-auto-installer-for-fedora -y
# dnf install nvautoinstall -y
```

### Usage
1. Make sure you have a working internet connection
2. Install the tool from COPR with the above instructions
3. Execute `nvautoinstall` to check installation modes
4. Run the installation modes according to your needs
5. Give stars to the repository if you found this helpful

### Modes of installation
Active internet connection and superuser privilege is required to execute the following installation modes.
- **`sudo nvautoinstall rpmadd`**  
  This mode enables the RPM Fusion NVIDIA drivers repository.
- **`sudo nvautoinstall driver`**  
  This mode simply installs the NVIDIA drivers. Enabling the RPM Fusion NVIDIA drivers repository is mandatory before 
  doing this.(Acceptable fedora repo versions are f33-34-35-36)
- **`sudo nvautoinstall nvrepo f36`**  
  This mode enables the official NVIDIA repository for CUDA software.
- **`sudo nvautoinstall plcuda`**  
  This mode installs only the CUDA support softwares. Enabling the RPM Fusion NVIDIA drivers and NVIDIA official 
  repository, and installing the basic drivers are mandatory before doing this.
- **`sudo nvautoinstall ffmpeg`**  
  This mode installs only the FFMPEG acceleration. Enabling the RPM Fusion NVIDIA drivers repository and installing the 
  basic drivers are mandatory before doing this.
- **`sudo nvautoinstall vulkan`**  
  This mode installs only the Vulkan renderer. Enabling the RPM Fusion NVIDIA drivers repository and installing the 
  basic drivers are mandatory before doing this.
- **`sudo nvautoinstall vidacc`**  
  This mode installs only the VDPAU/VAAPI acceleration. Enabling the RPM Fusion NVIDIA drivers repository and 
  installing the basic drivers are mandatory before doing this.
- **`sudo nvautoinstall getall`**  
  This mode installs all the above packages. (Not been implemented yet)
- **`sudo nvautoinstall cheksu`**  
  This mode allows you to check the current user privilege level. You can use this tool effectively only when you have 
  logged in as a root or sudo user.
- **`sudo nvautoinstall compat`**  
  This mode allows you to check your hardware and host compatibility. The tool would check your hardware and host and 
  tell if your device is supported by the tool or not.
- **`sudo nvautoinstall primec`**  
  This mode allows you to toggle the PRIME offloading to render all display elements using the discrete card. This has 
  only been tested on Workstation variant of Fedora Linux.
- **`sudo nvautoinstall --version`**  
  This mode shows the tool version and exits out.
- **`sudo nvautoinstall --help`**  
  This mode shows the help message and exits out.

### Note
* Active internet connection is required to download drivers.
* Requires secure boot to be turned off in UEFI systems.
* Requires superuser access for repo addition and driver setup.
* The drivers are fetched from the RPM Fusion repository.
* Use discretion while using this on other spins.
* Only tested on 9XX/10XX/20XX/30XX series discrete NVIDIA cards.
* Use discretion while installing with older discrete NVIDIA cards.
* No additional configuration is required for Optimus setups.
* Native support for PRIME configuration on Optimus.

### Coming soon
* CLI "Launch using Dedicated Graphics Card" option.
* Intuitive mode switching for hybrid graphics.
* Distinct mode for using integrated or discrete GPU.
* Experimental support for RHEL 8 and CentOS 8.
* Support for older cards by active querying at NVIDIA.

### Disclaimer
This tool has been tried and tested multiple times and is expected to work flawlessly in Fedora Linux (32 or above, 
and Rawhide). It has not been tested on any of the spins yet so you are requested to proceed with caution. While the 
chances of things going wrong is pretty slim, you would still want to make backups, should things do not go as expected. 
As always, you are choosing to use this tool at your will and you cannot hold me responsible for any mishap that may 
occur due to the misuse of this tool.

### Previews

#### Starting without any command

```
$ nvautoinstall
```

```
Usage: nvautoinstall [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  cheksu  Check the user privilege level.
  compat  Check your system compatibility.
  driver  Install the NVIDIA driver.
  ffmpeg  Install only the FFMPEG support software.
  getall  Install all the above packages.
  nvrepo  Enable the official NVIDIA repository for CUDA.
  plcuda  Install only the CUDA support software.
  primec  Setup PRIME support.
  rpmadd  Enable the RPM Fusion NVIDIA drivers repository.
  vidacc  Install only the VDPAU/VAAPI acceleration.
  vulkan  Install only the Vulkan support software.
```

#### Checking superuser permissions

```
$ sudo nvautoinstall cheksu
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser permission is available
      This tool is expected to work correctly here
[ ✗ ] Leaving installer
```

#### Checking the system compatibility

```
$ sudo nvautoinstall compat
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING FOR GPU COMPATIBILITY...
[ ! ] Compatibility infomation was obtained
[ ✓ ] One or more active NVIDIA GPUs were detected
      01:00.0 VGA compatible controller: NVIDIA Corporation TU117M [GeForce GTX 1650 Mobile / Max-Q] (rev a1)
      04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Picasso/Raven 2 [Radeon Vega Series / Radeon Vega Mobile Series] (rev c2)
[ ✓ ] An Optimus Dual GPU setup was detected
[ ★ ] GATHERING CURRENT HOST INFORMATION...
[ ! ] Host information was gathered
      System: Linux v5.15.6-100.fc34.x86_64
      Hostname: 038e97fb8ac6
      Version: #1 SMP Wed Dec 1 13:41:51 UTC 2021
      Distribution: Fedora Linux x86_64
[ ★ ] CHECKING FOR HOST COMPATIBILITY...
[ ✓ ] Supported OS detected
      This tool is expected to work correctly here
[ ✗ ] Leaving installer
```

#### Handling drivers installation

```
$ sudo nvautoinstall driver
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser privilege acquired
[ ★ ] CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...
[ ! ] RPM Fusion repository for Proprietary NVIDIA Driver was detected
[ ★ ] ATTEMPTING CONNECTION TO RPM FUSION SERVERS...
[ ✓ ] Connection to RPM Fusion servers was established
[ ★ ] LOOKING FOR EXISTING DRIVER PACKAGES...
[ ! ] No existing NVIDIA driver packages were detected
[ ★ ] INSTALLING PROPRIETARY DRIVERS...
.....
.....
.....
[ ✓ ] Driver package installation completed
[ ✗ ] Leaving installer
```

#### Installing FFMPEG support software

```
$ sudo nvautoinstall ffmpeg
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser privilege acquired
[ ★ ] CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...
[ ! ] RPM Fusion repository for Proprietary NVIDIA Driver was detected
[ ★ ] ATTEMPTING CONNECTION TO RPM FUSION SERVERS...
[ ✓ ] Connection to RPM Fusion servers was established
[ ★ ] LOOKING FOR EXISTING DRIVER PACKAGES...
      xorg-x11-drv-nvidia-kmodsrc-495.44-4.fc35.x86_64
      xorg-x11-drv-nvidia-libs-495.44-4.fc35.x86_64
      akmod-nvidia-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-495.44-4.fc35.x86_64
      nvidia-settings-495.44-1.fc35.x86_64
[ ! ] A total of 5 driver packages were detected
[ ★ ] INSTALLING NVENC/NVDEC FOR FFMPEG ACCELERATION...
.....
.....
.....
[ ✓ ] NVENC/NVDEC for FFMPEG acceleration were successfully installed
[ ✗ ] Leaving installer
```

#### Installing all the above packages

```
$ sudo nvautoinstall getall
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser privilege acquired
[ ★ ] FULL FLEDGED INSTALLATION BEGINNING...
      This mode is yet to be implemented
[ ✗ ] Leaving installer
```

#### Enabling the official NVIDIA repository for CUDA

```
$ sudo nvautoinstall nvrepo
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser privilege acquired
[ ★ ] CHECKING AVAILABILITY OF OFFICIAL CUDA REPOSITORY...
[ ! ] Official CUDA repository was not detected
[ ! ] Repository enabling is required
[ ★ ] ATTEMPTING CONNECTION TO NVIDIA SERVERS...
[ ✓ ] Connection to NVIDIA servers was established
[ ★ ] INSTALLING OFFICIAL CUDA REPOSITORY...
[ ✓ ] Official CUDA repository was enabled
[ ★ ] REFRESHING REPOSITORY LIST...
.....
[ ✓ ] Repositories have been refreshed
[ ★ ] DISABLING NVIDIA DRIVER MODULE...
.....
.....
.....
[ ✓ ] NVIDIA DRIVER module has been disabled
[ ✗ ] Leaving installer
```

#### Installing CUDA support software

```
$ sudo nvautoinstall plcuda
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser privilege acquired
[ ★ ] CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...
[ ! ] RPM Fusion repository for Proprietary NVIDIA Driver was detected
[ ★ ] ATTEMPTING CONNECTION TO RPM FUSION SERVERS...
[ ✓ ] Connection to RPM Fusion servers was established
[ ★ ] LOOKING FOR EXISTING DRIVER PACKAGES...
      xorg-x11-drv-nvidia-kmodsrc-495.44-4.fc35.x86_64
      xorg-x11-drv-nvidia-libs-495.44-4.fc35.x86_64
      akmod-nvidia-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-495.44-4.fc35.x86_64
      nvidia-settings-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-cuda-libs-495.44-4.fc35.x86_64
[ ! ] A total of 6 driver packages were detected
[ ★ ] CHECKING AVAILABILITY OF OFFICIAL CUDA REPOSITORY...
[ ! ] Official CUDA repository was detected
[ ★ ] ATTEMPTING CONNECTION TO NVIDIA SERVERS...
[ ✓ ] Connection to NVIDIA servers was established
[ ★ ] INSTALLING RPM FUSION METAPACKAGE FOR CUDA...
.....
.....
.....
[ ✓ ] RPM Fusion CUDA metapackage was successfully installed
[ ★ ] INSTALLING NVIDIA CUDA CORE PACKAGES...
.....
.....
.....
[ ✓ ] NVIDIA CUDA core packages were successfully installed
[ ✗ ] Leaving installer
```

#### Setting up PRIME support

```
$ sudo nvautoinstall primec
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser privilege acquired
[ ★ ] CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...
[ ! ] RPM Fusion repository for Proprietary NVIDIA Driver was detected
[ ★ ] ATTEMPTING CONNECTION TO RPM FUSION SERVERS...
[ ✓ ] Connection to RPM Fusion servers was established
[ ★ ] LOOKING FOR EXISTING DRIVER PACKAGES...
      xorg-x11-drv-nvidia-kmodsrc-495.44-4.fc35.x86_64
      xorg-x11-drv-nvidia-libs-495.44-4.fc35.x86_64
      akmod-nvidia-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-495.44-4.fc35.x86_64
      nvidia-settings-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-cuda-libs-495.44-4.fc35.x86_64
[ ! ] A total of 6 driver packages were detected
[ ★ ] SETTING UP PRIME SUPPORT...
[ ! ] Intervention required
      < Y > to enable PRIME support
      < N > to disable PRIME support
      < * > anything else to leave
[Y/N] Y
[ ★ ] ENABLING PRIME SUPPORT...
[ ✓ ] PRIME Support was successfully enabled
[ ✗ ] Leaving installer
```


#### Enabling the RPM Fusion NVIDIA drivers repositories

```
$ sudo nvautoinstall rpmadd
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser privilege acquired
[ ★ ] CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...
[ ! ] RPM Fusion repository for Proprietary NVIDIA Driver was not detected
[ ! ] Repository enabling is required
[ ★ ] ATTEMPTING CONNECTION TO RPM FUSION SERVERS...
[ ✓ ] Connection to RPM Fusion servers was established
[ ★ ] INSTALLING RPM FUSION NVIDIA REPOSITORY...
.....
.....
.....
[ ✓ ] RPM Fusion NVIDIA repository was enabled
[ ✗ ] Leaving installer
```

#### Installing the VDPAU/VAAPI support software

```
$ sudo nvautoinstall vidacc
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser privilege acquired
[ ★ ] CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...
[ ! ] RPM Fusion repository for Proprietary NVIDIA Driver was detected
[ ★ ] ATTEMPTING CONNECTION TO RPM FUSION SERVERS...
[ ✓ ] Connection to RPM Fusion servers was established
[ ★ ] LOOKING FOR EXISTING DRIVER PACKAGES...
      xorg-x11-drv-nvidia-kmodsrc-495.44-4.fc35.x86_64
      xorg-x11-drv-nvidia-libs-495.44-4.fc35.x86_64
      akmod-nvidia-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-495.44-4.fc35.x86_64
      nvidia-settings-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-cuda-libs-495.44-4.fc35.x86_64
      nvidia-persistenced-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-cuda-495.44-4.fc35.x86_64
[ ! ] A total of 8 driver packages were detected
[ ★ ] INSTALLING VIDEO ACCELERATION SUPPORT...
.....
.....
.....
[ ✓ ] Video acceleration were successfully installed
[ ✗ ] Leaving installer
```

#### Installing Vulkan support software

```
$ sudo nvautoinstall vulkan
```

```
[ # ] NVIDIA AUTOINSTALLER FOR FEDORA LINUX
[ ★ ] CHECKING SUPERUSER PERMISSIONS...
[ ✓ ] Superuser privilege acquired
[ ★ ] CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY...
[ ! ] RPM Fusion repository for Proprietary NVIDIA Driver was detected
[ ★ ] ATTEMPTING CONNECTION TO RPM FUSION SERVERS...
[ ✓ ] Connection to RPM Fusion servers was established
[ ★ ] LOOKING FOR EXISTING DRIVER PACKAGES...
      xorg-x11-drv-nvidia-kmodsrc-495.44-4.fc35.x86_64
      xorg-x11-drv-nvidia-libs-495.44-4.fc35.x86_64
      akmod-nvidia-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-495.44-4.fc35.x86_64
      nvidia-settings-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-cuda-libs-495.44-4.fc35.x86_64
      nvidia-persistenced-495.44-1.fc35.x86_64
      xorg-x11-drv-nvidia-cuda-495.44-4.fc35.x86_64
[ ! ] A total of 8 driver packages were detected
[ ★ ] INSTALLING VULKAN RENDERER SUPPORT...
.....
.....
.....
[ ✓ ] Vulkan renderer support were successfully installed
[ ✗ ] Leaving installer
```
