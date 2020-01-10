Name:		xcb-util-image
Version:	0.4.0
Release:	3%{?dist}
Summary:	Port of Xlib's XImage and XShmImage functions on top of libxcb
Group:		System Environment/Libraries
License:	MIT
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(xcb-util) >= 0.3.8
BuildRequires:	m4

%description
XCB util-image module provides the following library:

  - image: Port of Xlib's XImage and XShmImage functions.


%package 	devel
Summary:	Development and header files for xcb-util-image
Group:		System Environment/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Development files for xcb-util-image.


%prep
%setup -q


%build
%configure --with-pic --disable-static --disable-silent-rules
make %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm %{buildroot}%{_libdir}/*.la


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc README COPYING
%{_libdir}/*.so.*


%files devel
%doc NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/xcb/*.h


%changelog
* Tue Nov 10 2015 Adam Jackson <ajax@redhat.com> 0.4.0-3
- Rebuild against new xcb-utils

* Wed Oct 22 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-2
- Include COPYING.

* Sat Oct 18 2014 Thomas Moschny <thomas.moschny@gmx.de> - 0.4.0-1
- Update to 0.4.0.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 20 2012 Adam Jackson <ajax@redhat.com> 0.3.9-1
- xcb-util-image 0.3.9
- Rebuilt for new xcb-util soname

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr  6 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.8-3
- Fix explicit requires.

* Thu Apr  5 2012 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.8-2
- Specfile cleanups.

* Mon Dec  5 2011 Thomas Moschny <thomas.moschny@gmx.de> - 0.3.8-1
- New package.

