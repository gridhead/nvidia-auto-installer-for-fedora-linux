# To-do

## Converting to Click composition tool
[Click](https://click.palletsprojects.com/en/7.x/) is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun while also preventing any frustration caused by the inability to implement an intended CLI API.

## Purpose of converting to composition options
The installer is under diverse development process now. It is self sufficient to just install the NVIDIA drivers right now but it is too limited to do this task only. The aim of this conversion is grow this installer into a capable NVIDIA manager.

This planned manager would be then able to
- **Install**  
    - **NVIDIA drivers (without x86 libraries)**  
    By default, the Xorg x86 libraries are not required for general applications which are not based on x86 architecture - so it been done away in the default mode of installation. No option argument is required to trigger this type of installation.
    - **NVIDIA drivers (with x86 libraries)**  
    As the Xorg x86 libraries are required for applications for Steam Proton, DXVK and Lutris, installing and configuring x86 libraries along with the driver installation would be a right thing to do. This installation mode can be selected during execution.
    - **CUDA support softwares**  
    The CUDA support softwares are important for machine learning and deep learning applications so it would be only justified if the CUDA modules are installed along with drivers. This installation mode can be selected during execution.
    - **NVENC/NVDEC for FFMPEG support**  
    RPM Fusion support ffmpeg compiled with NVENC/NVDEC with Fedora 25 and later. You need to have a recent NVIDIA card (see the support matrix), and install the cuda sub-package. This installation mode can be selected during execution.
    - **Vulkan API for display rendering**  
    Vulkan is a low-overhead, cross-platform 3D graphics and computing API. Vulkan targets high-performance realtime 3D graphics applications such as interactive media across all platforms. This installation mode can be selected during execution.
    - **VDPAU/VAAPI for video acceleration support**  
    With recent enough discrete NVIDIA GPU (any GPU with Geforce 8 series and above), video accleration can be provided to video players using these modules if they are installed. This installation mode can be selected during exectution.

- **Uninstall**
    - **NVIDIA drivers**
    - **Xorg x86 libraries**
    - **CUDA support softwares**
    - **Vulkan (Fall back to OpenGL)**
    - **VDPAU/VAAPI**

- **Recover from binary installation**  
    - Installing via the NVIDIA's RUN binary available on the official website is truly a bad option. Just because it is general to most distributions, changes are not made keeping Fedora in mind so there are a lot of untracked changes.  
    - With that, even uninstalling and updating is difficult from the binary so this is definitely not a recommended way to get the proprietary drivers. If at all, you might have used it then this mode will help you clean up the mess made.

## Modes of installation

- **`--driver`**  
This mode simply installs the NVIDIA driver
- **`--x86lib`**  
This mode installs only the x86 libraries for Xorg
- **`--plcuda`**  
This mode installs only the CUDA support softwares
- **`--ffmpeg`**  
This mode installs only the FFMPEG acceleration
- **`--vulkan`**  
This mode installs only the Vulkan renderer
- **`--vidacc`**  
This mode installs only the VDPAU/VAAPI acceleration 
- **`--getall`**  
This mode installs all the above packages

## Notes
- Some packages might overlap due to them being interdependent. In such cases, installation of an already installed package would be skipped and only the new package would be installed.
- Uninstalling some packages might fail with some packages as there are other packages dependent on it. If you are persistent on removing them, you are better off removing the dependent apps first.
- If you are a machine learning enthusiast or an avid gaming or multimedia fan, the simplest way would be to install all the packages provided herewith using the **`--getall`** mode of installation.