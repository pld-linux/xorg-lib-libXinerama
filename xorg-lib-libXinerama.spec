
#
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
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	libtool
BuildRequires:	xorg-proto-panoramixproto-devel
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXinerama
BuildRoot:	%{tmpdir}/libXinerama-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Xinerama extension library.

%description -l pl
Biblioteka rozszerzenia Xinerama.


%package devel
Summary:	Header files libXinerama development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXinerama
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXinerama = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-panoramixproto-devel
Obsoletes:	libXinerama-devel

%description devel
Xinerama extension library.

This package contains the header files needed to develop programs that
use these libXinerama.

%description devel -l pl
Biblioteka rozszerzenia Xinerama.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXinerama.


%package static
Summary:	Static libXinerama libraries
Summary(pl):	Biblioteki statyczne libXinerama
Group:		Development/Libraries
Requires:	xorg-lib-libXinerama-devel = %{version}-%{release}
Obsoletes:	libXinerama-static

%description static
Xinerama extension library.

This package contains the static libXinerama library.

%description static -l pl
Biblioteka rozszerzenia Xinerama.

Pakiet zawiera statyczn± bibliotekê libXinerama.


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
%attr(755,root,wheel) %{_libdir}/libXinerama.so.*


%files devel
%defattr(644,root,root,755)
%{_libdir}/libXinerama.la
%attr(755,root,wheel) %{_libdir}/libXinerama.so
%{_pkgconfigdir}/xinerama.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXinerama.a
