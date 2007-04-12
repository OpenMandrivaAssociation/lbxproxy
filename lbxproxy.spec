Name: lbxproxy
Version: 1.0.1
Release: %mkrel 3
Summary: Low BandWidth X proxy
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libice-devel >= 1.0.0
BuildRequires: liblbxutil-devel >= 1.0.0
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0

%description
Applications that would like to take advantage of the Low Bandwidth
extension to X (LBX) must make their connections to an lbxproxy. These
applications need to know nothing about LBX, they simply connect to the
lbxproxy as if were a regular server. The lbxproxy accepts client connections,
multiplexes them over a single connection to the X server, and performs various
optimizations on the X protocol to make it faster over low bandwidth and/or
high latency connections.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/lbxproxy
%{_libdir}/X11/lbxproxy/AtomControl
%{_mandir}/man1/lbxproxy.1x.bz2


