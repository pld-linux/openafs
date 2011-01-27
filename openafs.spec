#
# TODO: - unpackaged files
#	- FHS compliance:
#	/afs (-> /mnt/afs?)
#	/var/openafs/cache (-> /var/cache/openafs?)
#
Summary:	OpenAFS distributed filesystem
Summary(pl.UTF-8):	Rozproszony system plików OpenAFS
Name:		openafs
Version:	1.5.78
Release:	0.1
Epoch:		1
License:	IBM Public License
Group:		Networking/Daemons
Source0:	http://www.openafs.org/dl/openafs/%{version}/%{name}-%{version}-src.tar.bz2
# Source0-md5:	d2ad44d1642f25fce6ac2d2944439559
Patch0:		%{name}-autoconf.patch
Patch1:		%{name}-link.patch
URL:		http://www.openafs.org/
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	heimdal-devel
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides common files shared across all the various
OpenAFS packages but are not necessarily tied to a client or server.

%description -l pl.UTF-8
AFS jest rozproszonym systemem plików pozwalającym na dzielenie plików
między wieloma komputerami, także na różnych platformach. AFS pozwala
na kontrolę dostępu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera pliki wspólne dla klienta i serwera AFS.

%package client
Summary:	OpenAFS Filesystem Client
Summary(pl.UTF-8):	Klient systemu plików OpenAFS
Group:		Networking/Daemons
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-kernel = %{epoch}:%{version}-%{release}

%description client
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides basic client support to mount and manipulate
AFS.

%description client -l pl.UTF-8
AFS jest rozproszonym systemem plików pozwalającym na dzielenie plików
między wieloma komputerami, także na różnych platformach. AFS pozwala
na kontrolę dostępu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera klienta do montowania i manipulowania AFS.

%package -n pam-pam_afs
Summary:	OpenAFS Filesystem PAM module
Summary(pl.UTF-8):	Moduł PAM dla klienta systemu plików OpenAFS
Group:		Applications/System
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client = %{epoch}:%{version}-%{release}
Requires:	%{name}-kernel = %{epoch}:%{version}-%{release}
Obsoletes:	pam_afs

%description -n pam-pam_afs
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides PAM client module.

%description -n pam-pam_afs -l pl.UTF-8
AFS jest rozproszonym systemem plików pozwalającym na dzielenie plików
między wieloma komputerami, także na różnych platformach. AFS pozwala
na kontrolę dostępu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera moduł PAM dla klienta.

%package kerberos-client
Summary:	OpenAFS Filesystem Kerberos4 Clients
Summary(pl.UTF-8):	Klient Kerberos4 systemu plików OpenAFS
Group:		Networking/Daemons
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description kerberos-client
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides kerberos4 utilities like kpasswd.

%description kerberos-client -l pl.UTF-8
AFS jest rozproszonym systemem plików pozwalającym na dzielenie plików
między wieloma komputerami, także na różnych platformach. AFS pozwala
na kontrolę dostępu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera narzędzia kerberos4 typu kpasswd.

%package kerberos-server
Summary:	OpenAFS Filesystem Kerberos4 Server
Summary(pl.UTF-8):	Serwer Kerberos4 systemu plików OpenAFS
Group:		Networking/Daemons
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description kerberos-server
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides kerberos4 servers.

%description kerberos-server -l pl.UTF-8
AFS jest rozproszonym systemem plików pozwalającym na dzielenie plików
między wieloma komputerami, także na różnych platformach. AFS pozwala
na kontrolę dostępu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera serwery kerberos4.

%package server
Summary:	OpenAFS Filesystem Server
Summary(pl.UTF-8):	Serwer systemu plików OpenAFS
Group:		Networking/Daemons
Requires(post):	grep
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-kernel = %{epoch}:%{version}-%{release}

%description server
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides basic server support to host files in an AFS
Cell.

%description server -l pl.UTF-8
AFS jest rozproszonym systemem plików pozwalającym na dzielenie plików
między wieloma komputerami, także na różnych platformach. AFS pozwala
na kontrolę dostępu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera serwer do przechowywania plików w AFS.

%package devel
Summary:	OpenAFS Development Libraries and Headers
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteki OpenAFS
Group:		Development/Libraries

%description devel
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides static development libraries and headers needed
to compile AFS applications. Note: AFS currently does not provide
shared libraries.

%description devel -l pl.UTF-8
AFS jest rozproszonym systemem plików pozwalającym na dzielenie plików
między wieloma komputerami, także na różnych platformach. AFS pozwala
na kontrolę dostępu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera biblioteki statyczne i nagłówki potrzebne do
kompilowania aplikacji z AFS. Aktualnie AFS nie dostarcza bibliotek
współdzielonych.

%package static
Summary:	Static OpenAFS libraries
Summary(pl.UTF-8):	Statyczne biblioteki OpenAFS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenAFS libraries.

%description static -l pl.UTF-8
Statyczne biblioteki OpenAFS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure \
	--with-krb5-conf=%{_bindir}/krb5-config \
%ifarch %{ix86}
	--with-afs-sysname=i386_linux26 \
%endif
%ifarch %{x8664}
	--with-afs-sysname=amd64_linux26 \
%endif
%ifarch ppc
	--with-afs-sysname=ppc_linux26 \
%endif
	--disable-kernel-module

%{__make} -j1 \
	CC="%{__cc}" \
	CCOBJ="%{__cc}" \
	MT_CC="%{__cc}" \
	OPTMZ="%{rpmcflags} -I/usr/include/ncurses -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_lib}/security
install -d $RPM_BUILD_ROOT%{_sysconfdir}/openafs
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install -d $RPM_BUILD_ROOT/etc/sysconfig
install -d $RPM_BUILD_ROOT/var/openafs/cache
install -d $RPM_BUILD_ROOT/var/log/openafs
install -d $RPM_BUILD_ROOT/afs

mv $RPM_BUILD_ROOT%{_libdir}/*pam* $RPM_BUILD_ROOT/%{_lib}/security

touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{CellServDB,SuidCells,ThisCell,cacheinfo}
install src/afsd/afs.rc.linux $RPM_BUILD_ROOT/etc/rc.d/init.d/afs
echo "AFS_SERVER=on" > $RPM_BUILD_ROOT/etc/sysconfig/afs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add afs
if [ -f /var/lock/subsys/afs ]; then
	/etc/rc.d/init.d/afs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/afs start\" to start AFS server." >&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/afs ]; then
		/etc/rc.d/init.d/afs stop
	fi
	/sbin/chkconfig --del afs
fi

%postun	-p /sbin/ldconfig

%post client
echo
echo The AFS cache is configured for 100 MB. Edit the
echo /etc/openafs/cacheinfo file to change this before
echo running AFS for the first time. You should also
echo set your home cell in /etc/openafs/ThisCell.
echo
echo Also, you may want to INSTALL the PAM module (package: pam-pam_afs)
echo and then EDIT /etc/pam.d/login and echo possibly others there
echo to get an AFS token on login.
echo

%post -n pam-pam_afs
echo You may want to edit /etc/pam.d/login and echo possibly others there
echo to get an AFS token on login. Put the line:
echo
echo    auth	   sufficient   /lib/security/pam_afs.so try_first_pass ignore_root
echo
echo before the one for pwdb/unix.
echo

%post server
if [ -f /etc/sysconfig/afs ]; then
	srv=`grep ^AFS_SERVER /etc/sysconfig/afs | sed 's/^AFS_SERVER[\s]*=[\s]*//'`
	if [ "$srv" = "on" ]; then
		exit 0
	fi
fi

echo
echo Be sure to edit /etc/sysconfig/afs and turn AFS_SERVER on
echo

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/afs
%attr(754,root,root) /etc/rc.d/init.d/afs
%attr(755,root,root) %{_bindir}/bos
%attr(755,root,root) %{_bindir}/fs
%attr(755,root,root) %{_bindir}/klog
%attr(755,root,root) %{_bindir}/klog.krb
%attr(755,root,root) %{_bindir}/pts
%attr(744,root,root) %{_bindir}/restorevol
%attr(755,root,root) %{_bindir}/sys
%attr(755,root,root) %{_bindir}/tokens
%attr(755,root,root) %{_bindir}/tokens.krb
%attr(755,root,root) %{_bindir}/udebug
%attr(755,root,root) %{_bindir}/unlog
%attr(755,root,root) %{_sbindir}/backup
%attr(755,root,root) %{_sbindir}/butc
%attr(755,root,root) %{_sbindir}/fstrace
%attr(755,root,root) %{_sbindir}/kas
%attr(755,root,root) %{_sbindir}/vos
%attr(755,root,root) %{_bindir}/afsmonitor
%attr(755,root,root) %{_bindir}/aklog
%attr(755,root,root) %{_bindir}/asetkey
%attr(755,root,root) %{_bindir}/knfs
%attr(755,root,root) %{_bindir}/kpwvalid
%attr(755,root,root) %{_bindir}/livesys
%attr(755,root,root) %{_bindir}/pagsh.krb
%attr(755,root,root) %{_bindir}/scout
%attr(755,root,root) %{_bindir}/translate_et
%attr(755,root,root) %{_bindir}/up
%attr(755,root,root) %{_bindir}/xstat_cm_test
%attr(755,root,root) %{_bindir}/xstat_fs_test
%attr(755,root,root) %{_sbindir}/bos_util
%attr(755,root,root) %{_sbindir}/fms
%attr(755,root,root) %{_sbindir}/kadb_check
%attr(755,root,root) %{_sbindir}/kdb
%attr(755,root,root) %{_sbindir}/voldump
%attr(755,root,root) %{_sbindir}/pt_util
%attr(755,root,root) %{_sbindir}/read_tape
%attr(755,root,root) %{_sbindir}/rmtsysd
%attr(755,root,root) %{_sbindir}/rxdebug
%attr(755,root,root) %{_sbindir}/uss
%attr(755,root,root) %{_sbindir}/vsys
%attr(755,root,root) %{_sbindir}/state_analyzer
%attr(755,root,root) %{_sbindir}/ka-forwarder
%attr(755,root,root) %{_sbindir}/fssync-debug
%attr(755,root,root) %{_libdir}/libafsauthent.so.1.1
%attr(755,root,root) %ghost %{_libdir}/libafsauthent.so.1
%attr(755,root,root) %{_libdir}/libafsrpc.so.1.2
%attr(755,root,root) %ghost %{_libdir}/libafsrpc.so.1
%attr(755,root,root) %{_libdir}/libkopenafs.so.1.1
%attr(755,root,root) %ghost %{_libdir}/libkopenafs.so.1
%dir %{_libdir}/%{name}

%files kerberos-client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/pagsh

%files kerberos-server
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/kaserver
%attr(755,root,root) %{_bindir}/afs_compile_et

%files client
%defattr(644,root,root,755)
%dir /afs
%dir /var/openafs/cache
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/CellServDB
%config %{_sysconfdir}/%{name}/SuidCells
%config %{_sysconfdir}/%{name}/ThisCell
%config %{_sysconfdir}/%{name}/cacheinfo
%attr(755,root,root) %{_bindir}/cmdebug
%attr(755,root,root) %{_sbindir}/afsd

%files -n pam-pam_afs
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/*

%files server
%defattr(644,root,root,755)
%dir /var/log/openafs
%attr(755,root,root) %{_sbindir}/bosserver
%attr(755,root,root) %{_libdir}/%{name}/buserver
%attr(755,root,root) %{_libdir}/%{name}/fileserver
%attr(755,root,root) %{_sbindir}/kpwvalid
%attr(755,root,root) %{_libdir}/%{name}/ptserver
%attr(755,root,root) %{_libdir}/%{name}/salvager
%attr(755,root,root) %{_libdir}/%{name}/upclient
%attr(755,root,root) %{_libdir}/%{name}/upserver
%attr(755,root,root) %{_libdir}/%{name}/vlserver
%attr(755,root,root) %{_sbindir}/volinfo
%attr(755,root,root) %{_libdir}/%{name}/volserver
%attr(755,root,root) %{_sbindir}/prdb_check
%attr(755,root,root) %{_sbindir}/vldb_check
%attr(755,root,root) %{_sbindir}/vldb_convert

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rxgen
%{_includedir}/afs
%{_includedir}/des_conf.h
%{_includedir}/des.h
%{_includedir}/des_odd.h
%{_includedir}/des_prototypes.h
%{_includedir}/kopenafs.h
%{_includedir}/lock.h
%{_includedir}/lwp.h
%{_includedir}/mit-cpyright.h
%{_includedir}/preempt.h
%{_includedir}/rx
%{_includedir}/timer.h
%{_includedir}/ubik.h
%{_includedir}/ubik_int.h
%{_libdir}/afs
%{_libdir}/libafsauthent.so
%{_libdir}/libafsauthent_pic.a
%{_libdir}/libafsrpc.so
%{_libdir}/libafsrpc_pic.a
%{_libdir}/libkopenafs.so
%{_libdir}/libdes.a
%{_libdir}/libjuafs.a
%{_libdir}/liblwp.a
%{_libdir}/libkopenafs.a
%{_libdir}/librx.a
%{_libdir}/librxkad.a
%{_libdir}/librxstat.a
%{_libdir}/libubik.a
%{_libdir}/libuafs.a

%files static
%defattr(644,root,root,755)
%{_libdir}/libafsauthent.a
%{_libdir}/libafsrpc.a
%{_libdir}/libkopenafs.a
