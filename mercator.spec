Summary:	A WorldForge terrain library
Summary(pl.UTF-8):   Biblioteka terenów WorldForge
Name:		mercator
Version:	0.2.4
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
# Source0-md5:	2b937519bc90ba00e0ae4cbe50e7760f
URL:		http://www.worldforge.org/dev/eng/libraries/mercator
BuildRequires:	wfmath-devel >= 0.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mercator is designed to handle terrain data.

%description -l pl.UTF-8
Mercator to biblioteka do obsługi danych terenów.

%package devel
Summary:	Header files for WorldForge terrain library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki terenów WorldForge
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wfmath-devel >= 0.3.2

%description devel
Header files for WorldForge terrain library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki terenów WorldForge.

%package static
Summary:	Static WorldForge terrain library
Summary(pl.UTF-8):   Statyczna biblioteka terenów WorldForge
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static WorldForge terrain library.

%description static -l pl.UTF-8
Statyczna biblioteka terenów WorldForge.

%prep
%setup -q

%build
%configure \
	--enable-static 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
