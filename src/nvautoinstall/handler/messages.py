from gettext import gettext as gt


nv_msgs: dict[str, str] = {
    "checkinggtrpmgtfusiongtnvidiagtrepository": gt("CHECKING AVAILABILITY OF RPM FUSION NVIDIA REPOSITORY..."),
    "nvidiagtdrivergtdetected": gt("RPM Fusion repository for Proprietary NVIDIA Driver was detected"),
    "nogtfurthergtaction": gt("No further action is necessary"),
    "nvidiagtdrivergtnotgtdetected": gt("RPM Fusion repository for Proprietary NVIDIA Driver was not detected"),
    "repositorygtenablinggtisgtrequired": gt("Repository enabling is required"),
    "attemptinggtconnectiongttogtrpmgtserver": gt("ATTEMPTING CONNECTION TO RPM FUSION SERVERS..."),
    "connectiongttogtrpmgtservergtestablished": gt("Connection to RPM Fusion servers was established"),
    "installinggtnvidiagtrepository": gt("INSTALLING RPM FUSION NVIDIA REPOSITORY..."),
    "nvidiagtrepositorygtenabled": gt("RPM Fusion NVIDIA repository was enabled"),
    "nvidiagtrepositorygtnotgtenabled": gt("RPM Fusion NVIDIA repository could not be enabled"),
    "connectiongttogtrpmgtservergtnotgtestablished": gt("Connection to RPM Fusion servers could not be established"),
    "leavinggtinstaller": gt("Leaving installer"),
    "lookinggtexistinggtdrivergtpackages": gt("LOOKING FOR EXISTING DRIVER PACKAGES..."),
    "nogtexistinggtnvidiagtdrivergtdetected": gt("No existing NVIDIA driver packages were detected"),
    "installinggtproprietarygtdrivers": gt("INSTALLING PROPRIETARY DRIVERS..."),
    "drivergtinstalationgtcompleted": gt("Driver package installation completed"),
    "proprietartgtdriversgtnotgtinstalled": gt("Proprietary drivers could not be installed"),
    "installinggtx86gtlibrariesgtforgtxorg": gt("INSTALLING x86 LIBRARIES FOR XORG..."),
    "x86gtlibrariesgtinstalled": gt("x86 libraries for XORG were successfully installed"),
    "x86gtlibrariesgtnotgtinstalled": gt("x86 libraries for XORG could not be installed"),
    "checkinggtavailabilitygtcudogtrepository": gt("CHECKING AVAILABILITY OF OFFICIAL CUDA REPOSITORY..."),
    "cudogtrepositorygtdetected": gt("Official CUDA repository was detected"),
}
