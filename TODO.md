# To-do

## Converting to Click composition tool
[Click](https://click.palletsprojects.com/en/7.x/) is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by the inability to implement an intended CLI API.

## Purpose of converting to composition options
The installer is under diverse development process now. It is self sufficient to just install the NVIDIA drivers right now but it is too limited to do this task only. The aim of this conversion is grow this installer into a capable NVIDIA manager.

This planned manager would be then able to
- **Install NVIDIA drivers (without x86 libraries)**  
By default, the Xorg x86 libraries are not required for general applications which are not based on x86 architecture - so it been done away in the default mode of installation. No option argument is required to trigger this type of installation.
- **Install NVIDIA drivers (with x86 libraries)**  
As the Xorg x86 libraries are required for applications for Steam Proton, DXVK and Lutris, installing and configuring x86 libraries along with the driver installation would be a right thing to do. This installation mode can be selected during execution.
- **Install CUDA support softwares**  
The CUDA support softwares are important for machine learning and deep learning applications so it would be only justified if the CUDA modules are installed along with drivers. This installation mode can be selected during execution.
- **Install NVENC/NVDEC for FFMPEG support**  
RPM Fusion support ffmpeg compiled with NVENC/NVDEC with Fedora 25 and later. You need to have a recent NVIDIA card (see the support matrix), and install the cuda sub-package. This installation mode can be selected during execution.
- **Install Vulkan API for display rendering**  
Vulkan is a low-overhead, cross-platform 3D graphics and computing API. Vulkan targets high-performance realtime 3D graphics applications such as interactive media across all platforms. This installation mode can be selected during execution.
- **Install VDPAU/VAAPI for video acceleration support**  
With recent enough discrete NVIDIA GPU (any GPU with Geforce 8 series and above), video accleration can be provided to video players using these modules if they are installed. This installation mode can be selected during exectution.
- **Uninstall NVIDIA drivers**
- **Uninstall CUDA support softwares**
- **Uninstall Vulkan (Fall back to OpenGL)**
- **Uninstall VDPAU/VAAPI**
- **Recover from binary installation**