%global srcname nvidia-auto-installer-for-fedora-linux

Name:    nvautoinstall
Version: 0.4.1
Release: 2%{?dist}
Summary: NVIDIA Auto Installer for Fedora Linux

License: GPLv3+
Url:     https://github.com/t0xic0der/%{srcname}
Source0: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel

Requires:      dnf-plugins-core

%description
A CLI tool which lets you install proprietary NVIDIA drivers and much more easily on Fedora Linux (32 or above and Rawhide)

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nvautoinstall

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/nvautoinstall

%changelog

* Sun Oct 09 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.4.1-2
- rebuild for py11
- cosmetic changes for spec file

* Thu May 12 2022 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.4.1-1
- v0.4.1
- Included code quality compliance checks in the repository
- Setup GitHub Actions for code compliance checks
- Setup Dependabot alerts in the repository for security and updates
- Loosened Python version requirement to support older Fedora releases
- Added .gitignore of Python template to the repository
- Dependabot - Bumped pyparsing from 3.0.7 to 3.0.8
- Dependabot - Bumped platformdirs from 2.5.1 to 2.5.2
- Dependabot - Bumped typing-extensions from 4.1.1 to 4.2.0
- Updated NVIDIA CUDA repositories for Fedora Linux 36
- Added quality-of-life enhancing error correction messages

* Thu Dec 16 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.4.0-1
- v0.4.0
- Restructured the project to make the codebase more modular
- Performed repository clean up and removal of static files
- Reworked the dependency management with the use of Poetry
- Deprecated COPR build updates for Mageia, EPEL and OpenSUSE
- Reimplimented CLI compositing to make use of commands over options
- Removed dedicated installation of x86 NVIDIA libraries due to inclusion
- Fixed RPM Fusion Non-free repo detection by force installation
- Updated official CUDA repositories to point to Fedora 34 or later

* Thu Aug 12 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.3.9-1
- v0.3.9
- Reworked RPM specfile with pyproject directives
- Removed dependency on python3-setuptools for build
- Added dnf-plugins-core in the list of runtime dependencies

* Mon Aug 02 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.3.8-1
- v0.3.8
- Replaced ping with curl for checking availability of RPM Fusion servers
- Replaced ping with curl for checking availability of NVIDIA Developer servers

* Sat May 22 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.3.7-1
- v0.3.7
- Added option to enable/disable PRIME support on Optimus-supported devices
- Added other miscellaneous changes for ease of maintenance

* Sun May 09 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.3.6-1
- v0.3.6
- Reworked installation method for CUDA repo compatibility
- Minor patch leading to a version bump

* Thu Apr 29 2021 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.3.5-1
- v0.3.5
- Corrected unicode escape sequences for colors
- Changed CUDA repository to the most recent F33 remote install
- Fixed imports for development/packaged environment
- Refactored the code to remove needless lines
- Made compliance related changes here and there
- Tested and confirmed the tool to be working in F34 Workstation

* Thu Jun 04 2020 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.3.0-1
- v0.3.0
- Combined RPM Fusion pinging, checking, installing into a single module
- Combined driver installer and existing package checking into a single module
- Combined host detection with GPU support checking into a single module
- Revamped installation mode using command line arguments
- Withdrew x86 libraries from the default installation mode
- Added a new x86 libraries mode of installation for Xorg
- Added integrated CUDA module for repository checking, adding and installing
- Added support for FFMPEG acceleration using NVENC/NVDEC
- Added dedicated privilege check for each installation mode
- Added video hardware acceleration using VDPAU/VAAPI
- Added support for installation of Vulkan renderer
- Placeholder added for install everything mode of installation (Yet to be completed)
- Converged all low-level module operations into a single file for speed
- All print operations have been replaced by click-echo for optimization
- Added checks for NVIDIA repository and RPM Fusion repository availability
- Added network availability check before pinging respective repo servers
- Improved handling of interrupt. halt and suspend system calls for tool

* Mon Jun 01 2020 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.6-1
- v0.2.6
- Fixed broken repository addition module
- Added installation of fedora-workstation-repositories first
- Added enabling of repository after the install is complete

* Sun May 31 2020 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.5-1
- v0.2.5
- Removed mandatory sleep for kernel module load
- Removed dependency on kernel module loader
- Removed kernel module force-read altogether
- Defaulted textual messages to autocolor for better legibility
- Fixed boolean choices in main function
- Fixed boolean choices in package check
- Fixed prompt colors for custom-themed terminals

* Wed May 27 2020 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.2.0-1
- v0.2.0
- Cleaned up repeated code using class implemented decorator calls
- Enforced root access for whole operation instead of sudo implementation
- Added support for x86 libraries of Xorg display server
- Added distribution identification with support status display
- Scaled up to accompany Workstation as well as Fedora Spins
- Added dedicated status check for driver installation
- Added dedicated status check for kernel module reader
- Fixed confirmation choice during package check
- Fixed typo in RPM Fusion mentions throughout the tool interface

* Fri May 22 2020 Akashdeep Dhar <t0xic0der@fedoraproject.org> - 0.1.0-1
- v0.1.0
- Added host detection with display of system details and hostname
- Added GPU compatibility check for detecting active NVIDIA GPU
- Added detection for Optimus Dual GPU and dedicated GPU setups
- Declination to install if no active NVIDIA GPU is detected
- Added check for existing driver installations with listing of packages
- Added ability to install over an existing driver installation
- Added reachability check for RPMFusion servers before fetching
- Added automatic fetching and enabling of RPMFusion NVIDIA Repo
- Declination to install if repository addition is voluntarily cancelled
- Added skipping repo fetch and update if repository is present
- Added exclusive 64-bit driver installation with kernel load sleeptime
- Added forced kernel config read events with forced sleeptime
- Added restart feature activated with consent of the user
