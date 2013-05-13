Name: lbxproxy
Version: 1.0.2
Release: %mkrel 3
Summary: Low Bandwidth X proxy
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(ice) >= 1.0.0
BuildRequires: pkgconfig(lbxutil) >= 1.0.0
BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xext) >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-xtrans-devel >= 1.0.0

Patch0:		aarch64.patch

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
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/lbxproxy
%{_libdir}/X11/lbxproxy/AtomControl
%{_mandir}/man1/lbxproxy.1*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdv2011.0
+ Revision: 666062
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 606396
- rebuild

* Tue Jan 12 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 490181
- New version: 1.0.2
  Improved package description

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-8mdv2010.0
+ Revision: 425502
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 351348
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 222357
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2008.1
+ Revision: 150440
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 52688
- don't specify man page extension
- rebuild for 2008


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:31:58 (27464)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

