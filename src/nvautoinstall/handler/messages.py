from gettext import gettext as gt


nv_msgs: dict[str, str] = {
    "checking_rpm_fusion_nvidia_repository": gt("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY..."),
    "nvidia_driver_detected": gt("RPM Fusion repository for Proprietary NVIDIA Driver was detected"),
    "no_further_action": gt("No further action is necessary"),
    "nvidia_driver_not_detected": gt("RPM Fusion repository for Proprietary NVIDIA Driver was not detected"),
    "repository_enabling_is_required": gt("Repository enabling is required"),
    "attempting_connection_to_rpm_server": gt("ATTEMPTING CONNECTION TO RPM FUSION SERVERS..."),
    "connection_to_rpm_server_established": gt("Connection to RPM Fusion servers was established"),
    "installing_nvidia_repository": gt("INSTALLING RPM FUSION NVIDIA REPOSITORY..."),
    "nvidia_repository_enabled": gt("RPM Fusion NVIDIA repository was enabled"),
    "nvidia_repository_not_enabled": gt("RPM Fusion NVIDIA repository could not be enabled"),
    "connection_to_rpm_server_not_established": gt("Connection to RPM Fusion servers could not be established"),
    "leaving_installer": gt("Leaving installer"),
    "looking_existing_driver_packages": gt("LOOKING FOR EXISTING DRIVER PACKAGES..."),
    "no_existing_nvidia_driver_detected": gt("No existing NVIDIA driver packages were detected"),
    "installing_proprietary_drivers": gt("INSTALLING PROPRIETARY DRIVERS..."),
    "driver_instalation_completed": gt("Driver package installation completed"),
    "proprietart_drivers_not_installed": gt("Proprietary drivers could not be installed"),
    "installing_x86_libraries_for_xorg": gt("INSTALLING x86 LIBRARIES FOR XORG..."),
    "x86_libraries_installed": gt("x86 libraries for XORG were successfully installed"),
    "x86_libraries_not_installed": gt("x86 libraries for XORG could not be installed"),
    "checking_availability_cudo_repository": gt("CHECKING AVAILABILITY OF OFFICIAL CUDA REPOSITORY..."),
    "cudo_repository_detected": gt("Official CUDA repository was detected"),
}
