Summary:	Low Bandwidth X proxy
Name:		lbxproxy
Version:	1.0.3
Release:	14
License:	MIT
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(ice) >= 1.0.0
BuildRequires:	pkgconfig(lbxutil) >= 1.0.0
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xtrans)

%description
Applications that would like to take advantage of the Low Bandwidth
extension to X (LBX) must make their connections to an lbxproxy. These
applications need to know nothing about LBX, they simply connect to the
lbxproxy as if were a regular server. The lbxproxy accepts client connections,
multiplexes them over a single connection to the X server, and performs various
optimizations on the X protocol to make it faster over low bandwidth and/or
high latency connections.
Note that current X servers don't support the LBX extension, so this package is
only useful to connect to old X servers.

%prep
%autosetup -p1

%build
# make autoreconf more happy
sed -i -e 's,\(^AM_INIT_AUTOMAKE(\[\),\1subdir-objects ,' configure.ac
autoreconf -vfi

%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/lbxproxy
%{_sysconfdir}/X11/lbxproxy/AtomControl
%{_mandir}/man1/lbxproxy.1*

