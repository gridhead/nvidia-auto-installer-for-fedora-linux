%global srcname nvidia-auto-installer-for-fedora

Name: nvautoinstall
Version: 0.3.5
Release: 0%{?dist}
License: GPLv3
Summary: A CLI tool that helps you install proprietary NVIDIA drivers and much more
Url: https://github.com/t0xic0der/%{srcname}
Source0: https://github.com/t0xic0der/%{srcname}/archive/%{name}-%{version}.tar.gz

BuildArch: noarch

%if 0%{?el6}
BuildRequires: python34-devel
BuildRequires: python34-setuptools
%else
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif

%description
NVAutoInstall is a small CLI tool designed to facilitate installation of the
proprietary NVidia graphics drivers & related tools. It supports installation
of base drivers, CUDA software, Vulkan, VDPAU/VDAAPI and FFMPEG acceleration
as well as check your system for compatibility and manage RPMFusion and NVidia
repositories.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
%py3_build

%install
%py3_install

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%doc pics/
%doc SCREENSHOTS.md
%license LICENSE
%{_bindir}/nvautoinstall
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
