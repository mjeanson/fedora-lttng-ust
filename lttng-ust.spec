Name:           lttng-ust
Version:        2.0.8
Release:        1%{?dist}
License:        LGPLv2 and GPLv2 and MIT
Group:          Development/Libraries
Summary:        LTTng Userspace Tracer library
URL:            http://lttng.org/ust/
Source0:        http://lttng.org/files/lttng-ust/%{name}-%{version}.tar.bz2

BuildRequires:  libuuid-devel texinfo systemtap-sdt-devel libtool
BuildRequires:  userspace-rcu-devel >= 0.6.6

%description
This library may be used by user space applications to generate 
tracepoints using LTTng.

%package -n %{name}-devel
Summary:        LTTng Userspace Tracer library headers and development files
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       userspace-rcu-devel systemtap-sdt-devel

%description -n %{name}-devel
This library provides support for developing programs using 
LTTng userspace tracing

%prep
%setup -q

%build
#Reinitialize libtool with the fedora version to remove Rpath
libtoolize -cvfi
%configure --docdir=%{_docdir}/%{name} --disable-static --with-sdt
# --with-java-jdk
# Java support was disabled in lttng-ust's stable-2.0 branch upstream in
# http://git.lttng.org/?p=lttng-ust.git;a=commit;h=655a0d112540df3001f9823cd3b331b8254eb2aa
# We can revisit enabling this when the next major version is released.

make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
rm -vf %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*
%{_mandir}/man3/lttng-ust.3.gz
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/README


%files -n %{name}-devel
%{_bindir}/lttng-gen-tp
%{_mandir}/man1/lttng-gen-tp.1.gz
%{_prefix}/include/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/lttng-ust*.pc

%dir %{_docdir}/%{name}/examples
%{_docdir}/%{name}/examples/*

%changelog
* Mon Jul 22 2013 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.0.8-1
- New upstream bugfix release

* Tue Oct 23 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.0.5-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.0.4-2
- Add dependency on systemtap-sdt-devel for devel package

* Tue Jun 19 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.0.4-1
- New upstream release
- Updates from review comments
* Thu Jun 14 2012 Yannick Brosseau <yannick.brosseau@gmail.com> - 2.0.3-1
- New package, inspired by the one from OpenSuse

