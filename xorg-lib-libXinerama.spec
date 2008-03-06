Summary:	Xinerama extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia Xinerama
Name:		xorg-lib-libXinerama
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXinerama-%{version}.tar.bz2
# Source0-md5:	cd9f7c46439ac40e0517a302d2434d2c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXinerama
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xinerama extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia Xinerama.

%package devel
Summary:	Header files for libXinerama library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXinerama
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-xineramaproto-devel
Obsoletes:	libXinerama-devel

%description devel
Xinerama extension library.

This package contains the header files needed to develop programs that
use libXinerama.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia Xinerama.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXinerama.

%package static
Summary:	Static libXinerama library
Summary(pl.UTF-8):	Biblioteka statyczna libXinerama
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXinerama-static

%description static
Xinerama extension library.

This package contains the static libXinerama library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia Xinerama.

Pakiet zawiera statyczną bibliotekę libXinerama.

%prep
%setup -q -n libXinerama-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXinerama.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXinerama.so
%{_libdir}/libXinerama.la
%{_pkgconfigdir}/xinerama.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXinerama.a
