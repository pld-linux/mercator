
Summary:	A WorldForge terrain library
Name:		mercator
Version:	0.2.4
Release:	0.1
License:	GPL
Group:		Libraries
URL:		http://www.worldforge.org/dev/eng/libraries/mercator
Source0:	http://dl.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
# Source0-md5:	2b937519bc90ba00e0ae4cbe50e7760f
BuildRequires:	wfmath-devel >= 0.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mercator is designed to handle terrain data.

%package devel
Summary:	A WorldForge terrain library headers and static libs
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	wfmath-devel >= 0.3.2

%description devel
Mercator is designed to handle terrain data.

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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*
%doc AUTHORS COPYING NEWS README ChangeLog

%files devel
%defattr(644,root,root,755)
#%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_pkgconfigdir}/*
%{_includedir}/*
