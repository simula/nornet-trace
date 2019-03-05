Name: nornet-trace-service
Version: 2.0.0~beta1
Release: 1
Summary: NorNet Control
Group: Applications/Internet
License: GPLv3
URL: https://www.nntb.no/
Source: https://packages.nntb.no/software/nornet-trace-service/%{name}-%{version}.tar.xz

AutoReqProv: on
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRoot: %{_tmppath}/%{name}-%{version}-build


# This package does not generate debug information (no executables):
%global debug_package %{nil}

# TEST ONLY:
# define _unpackaged_files_terminate_build 0


%description
NorNet is a testbed for multi-homed systems. This package
contains the NorNet Trace serice scripts.
See https://www.nntb.no for details on NorNet!

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install



%package trace-importer
Summary: NorNet Trace Importer
Group: Applications/Internet
BuildArch: noarch
Recommends: hipercontracer

%description trace-service
 NorNet Trace Importer is the importer cron job to import results from the
 NorNet Trace Service into a database.
 See https://www.nntb.no for details on NorNet!



%package trace-service
Summary: NorNet Trace Service
Group: Applications/Internet
BuildArch: noarch
Requires: %{name}-trace-importer = %{version}-%{release}
Requires: nornet-tunnelbox = %{version}-%{release}
Requires: hipercontracer

%description trace-service
 NorNet Trace Service is the traceroute service for the NorNet testbed.
 It performs regular traceroute/traceroute6 runs among all sites.
 See https://www.nntb.no for details on NorNet!

%files trace-service
/usr/bin/nornetinfogenerator
/usr/share/man/man1/nornetinfogenerator.1.gz



%changelog
* Fri Nov 16 2018 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.0.0
- Created RPM package.
