Summary:	Xinerama extension library
Summary(pl):	Biblioteka rozszerzenia Xinerama
Name:		xorg-lib-libXinerama
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXinerama-%{version}.tar.bz2
# Source0-md5:	90346044dba6cb5c3762d22ebf47c767
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-panoramixproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXinerama
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Xinerama extension library.

%description -l pl
Biblioteka rozszerzenia Xinerama.

%package devel
Summary:	Header files libXinerama development
Summary(pl):	Pliki nagłówkowe do biblioteki libXinerama
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-panoramixproto-devel
Obsoletes:	libXinerama-devel

%description devel
Xinerama extension library.

This package contains the header files needed to develop programs that
use these libXinerama.

%description devel -l pl
Biblioteka rozszerzenia Xinerama.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXinerama.

%package static
Summary:	Static libXinerama library
Summary(pl):	Biblioteka statyczna libXinerama
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXinerama-static

%description static
Xinerama extension library.

This package contains the static libXinerama library.

%description static -l pl
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
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libXinerama.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXinerama.so
%{_libdir}/libXinerama.la
%{_pkgconfigdir}/xinerama.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXinerama.a
