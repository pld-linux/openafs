#
# TODO: FHS compliance:
#	/afs (-> /mnt/afs?)
#	/var/openafs/cache (-> /var/cache/openafs?)
#
#%%define	kernver	2.2.0
Summary:	OpenAFS distributed filesystem
Summary(pl):	Rozproszony system plików OpenAFS
Name:		openafs
Version:	1.2.9a
Release:	1
License:	IBM Public License
Group:		Networking/Daemons
Source0:	http://www.openafs.org/dl/openafs/%{version}/%{name}-%{version}-src.tar.bz2
Patch0:		%{name}-Makefile.in.fix
Patch1:		http://www.openafs.org/pages/security/xdr-updates-20020731.delta
Patch2:		openafs-uss-fix.patch
URL:		http://www.openafs.org/
BuildRequires:	autoconf
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires(post):	/sbin/ldconfig
Requires:	%{name}-kernel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides common files shared across all the various
OpenAFS packages but are not necessarily tied to a client or server.

%description -l pl
AFS jest rozproszonym systemem plików pozwalaj±cym na dzielenie plików
miêdzy wieloma komputerami, tak¿e na ró¿nych platformach. AFS pozwala
na kontrolê dostêpu, uwierzytalnianie, backup i administrowanie.

Ten pakiet zawiera pliki wspólne dla klienta i serwera AFS.

%package client
Summary:	OpenAFS Filesystem Client
Summary(pl):	Klient systemu plików OpenAFS
Group:		Networking/Daemons
Requires:	%{name} = %{version}
Requires:	%{name}-kernel

%description client
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides basic client support to mount and manipulate
AFS.

%description client -l pl
AFS jest rozproszonym systemem plików pozwalaj±cym na dzielenie plików
miêdzy wieloma komputerami, tak¿e na ró¿nych platformach. AFS pozwala
na kontrolê dostêpu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera klienta do montowania i manipulowania AFS.

%package kerberos-client
Summary:	OpenAFS Filesystem Kerberos4 Clients
Summary(pl):	Klient Kerberos4 systemu plików OpenAFS
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description kerberos-client
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides kerberos4 utilities like kpasswd.

%description kerneros-client -l pl
AFS jest rozproszonym systemem plików pozwalaj±cym na dzielenie plików
miêdzy wieloma komputerami, tak¿e na ró¿nych platformach. AFS pozwala
na kontrolê dostêpu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera narzêdzia kerberos4 typu kpasswd.

%package kerberos-server
Summary:	OpenAFS Filesystem Kerberos4 Server
Summary(pl):	Serwer Kerberos4 systemu plików OpenAFS
Group:		Networking/Daemons
Requires:	%{name} = %{version}

%description kerberos-server
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides kerberos4 servers.

%description  kerberos-server -l pl
AFS jest rozproszonym systemem plików pozwalaj±cym na dzielenie plików
miêdzy wieloma komputerami, tak¿e na ró¿nych platformach. AFS pozwala
na kontrolê dostêpu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera serwery kerberos4.

%package server
Summary:	OpenAFS Filesystem Server
Summary(pl):	Serwer systemu plików OpenAFS
Group:		Networking/Daemons
Requires(post):	grep
Requires:	%{name} = %{version}
Requires:	%{name}-kernel = %{version}

%description server
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides basic server support to host files in an AFS
Cell.

%description server -l pl
AFS jest rozproszonym systemem plików pozwalaj±cym na dzielenie plików
miêdzy wieloma komputerami, tak¿e na ró¿nych platformach. AFS pozwala
na kontrolê dostêpu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera serwer do przechowywania plików w AFS.

%package devel
Summary:	OpenAFS Development Libraries and Headers
Summary(pl):	Pliki nag³ówkowe i biblioteki OpenAFS
Group:		Development/Libraries

%description devel
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides static development libraries and headers needed
to compile AFS applications. Note: AFS currently does not provide
shared libraries.

%description devel -l pl
AFS jest rozproszonym systemem plików pozwalaj±cym na dzielenie plików
miêdzy wieloma komputerami, tak¿e na ró¿nych platformach. AFS pozwala
na kontrolê dostêpu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera biblioteki statyczne i nag³ówki potrzebne do
kompilowania aplikacji z AFS. Aktualnie AFS nie dostarcza bibliotek
wspó³dzielonych.

%package kernel
Summary:	OpenAFS Kernel Module(s)
Summary(pl):	Modu³(y) j±dra OpenAFS
Group:		Networking/Daemons

%description kernel
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides precompiled AFS kernel modules for various
kernels.

%description kernel -l pl
AFS jest rozproszonym systemem plików pozwalaj±cym na dzielenie plików
miêdzy wieloma komputerami, tak¿e na ró¿nych platformach. AFS pozwala
na kontrolê dostêpu, uwierzytelnianie, backup i administrowanie.

Ten pakiet zawiera prekompilowane modu³y j±dra do AFS.

#%package kernel-source
#Summary:	OpenAFS Kernel Module source tree
#Summary(pl):	¬ród³a modu³u j±dra AFS
#Group:		Networking/Daemons

#%description kernel-source
#The AFS distributed filesystem. AFS is a distributed filesystem
#allowing cross-platform sharing of files among multiple computers.
#Facilities are provided for access control, authentication, backup and
#administrative management.

#This package provides the source code to build your own AFS kernel
#module.

#%description kernel-source -l pl
#AFS jest rozproszonym systemem plików pozwalaj±cym na dzielenie plików
#miêdzy wieloma komputerami, tak¿e na ró¿nych platformach. AFS pozwala
#na kontrolê dostêpu, autentykacjê, backup i administrowanie.

#Ten pakiet zawiera ¼ród³a do samodzielnego skompilowania modu³u AFS.

%prep
%setup -q
%patch0 -p0
#%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure \
	--with-linux-kernel-headers=%{_kernelsrcdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/lib/modules/misc
mkdir -p $RPM_BUILD_ROOT/lib/security
mkdir -p $RPM_BUILD_ROOT/etc/openafs
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p $RPM_BUILD_ROOT/var/openafs/cache
mkdir -p $RPM_BUILD_ROOT/var/log/openafs
mkdir -p $RPM_BUILD_ROOT/afs

mv $RPM_BUILD_ROOT%{_libdir}/%{name}/*.o $RPM_BUILD_ROOT/lib/modules/misc
mv $RPM_BUILD_ROOT%{_libdir}/*pam* $RPM_BUILD_ROOT/lib/security

touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{CellServDB,SuidCells,ThisCell,cacheinfo}
install src/afsd/afs.rc.linux $RPM_BUILD_ROOT/etc/rc.d/init.d/afs
echo "AFS_SERVER=on" > $RPM_BUILD_ROOT/etc/sysconfig/afs

###
### clean
###
%clean
rm -rf $RPM_BUILD_ROOT

###
### scripts
###
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
echo Also, you may want to edit /etc/pam.d/login and
echo possibly others there to get an AFS token on login.
echo Put the line:
echo
echo    auth	   sufficient   /lib/security/pam_afs.so try_first_pass ignore_root
echo
echo before the one for pwdb.
echo

%post server
if [ -f /etc/sysconfig/afs ]; then
	srv=`grep ^AFS_SERVER /etc/sysconfig/afs | sed 's/^AFS_SERVER[\s]*=[\s]*//'`
	if [ $srv eq "on"]; then
		exit 0
	fi
fi

echo
echo Be sure to edit /etc/sysconfig/afs and turn AFS_SERVER on
echo

###
### file lists
###
%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/afs
%attr(754,root,root) /etc/rc.d/init.d/afs
%attr(755,root,root) %{_bindir}/bos
%attr(755,root,root) %{_bindir}/fs
%attr(755,root,root) %{_bindir}/klog
%attr(755,root,root) %{_bindir}/klog.krb
%attr(755,root,root) %{_bindir}/pts
%attr(755,root,root) %{_bindir}/sys
%attr(755,root,root) %{_bindir}/tokens
%attr(755,root,root) %{_bindir}/tokens.krb
%attr(755,root,root) %{_bindir}/udebug
%attr(755,root,root) %{_bindir}/unlog
%attr(755,root,root) %{_sbindir}/backup
%attr(755,root,root) %{_sbindir}/butc
%attr(755,root,root) %{_sbindir}/fstrace
%attr(755,root,root) %{_sbindir}/kas
%attr(755,root,root) %{_sbindir}/restorevol
%attr(755,root,root) %{_sbindir}/vos
%attr(755,root,root) %{_bindir}/afsmonitor
%attr(755,root,root) %{_bindir}/dlog
%attr(755,root,root) %{_bindir}/dpass
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
%attr(755,root,root) %{_sbindir}/copyauth
%attr(755,root,root) %{_sbindir}/fms
%attr(755,root,root) %{_sbindir}/kadb_check
%attr(755,root,root) %{_sbindir}/kdb
%attr(755,root,root) %{_sbindir}/kdump-2.4.20
%attr(755,root,root) %{_sbindir}/kseal
%attr(755,root,root) %{_sbindir}/pt_util
%attr(755,root,root) %{_sbindir}/read_tape
%attr(755,root,root) %{_sbindir}/rmtsysd
%attr(755,root,root) %{_sbindir}/rxdebug
%attr(755,root,root) %{_sbindir}/uss
%attr(755,root,root) %{_sbindir}/vsys
%attr(755,root,root) %{_libdir}/libafsauthent.so.1.0
%attr(755,root,root) %{_libdir}/libafsrpc.so.1.0
%{_libdir}/libuafs.a
%dir %{_libdir}/%{name}

%files kerberos-client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/pagsh

%files kerberos-server
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/kaserver
# conflict with e2fsprogs
#%attr(755,root,root) %{_bindir}/compile_et

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
/lib/security/*

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
%{_includedir}/rx
%{_includedir}/ubik.h
%{_includedir}/ubik_int.h
%{_includedir}/lock.h
%{_includedir}/lwp.h
%{_includedir}/preempt.h
%{_includedir}/timer.h
%{_includedir}/des.h
%{_includedir}/des_conf.h
%{_includedir}/des_odd.h
%{_includedir}/mit-cpyright.h
%{_includedir}/potpourri.h
%{_libdir}/afs
%{_libdir}/librxkad.a
%{_libdir}/libafsauthent.a
%{_libdir}/libafsrpc.a
%{_libdir}/libubik.a
%{_libdir}/librxstat.a
%{_libdir}/librx.a
%{_libdir}/liblwp.a
%{_libdir}/libdes.a

%files kernel
%defattr(644,root,root,755)
/lib/modules/misc/libafs*.o*

#%files kernel-source
#%defattr(644,root,root,755)
#%{_prefix}/src/openafs-kernel-%{afsvers}/LICENSE.IBM
#%{_prefix}/src/openafs-kernel-%{afsvers}/LICENSE.Sun
#%{_prefix}/src/openafs-kernel-%{afsvers}/README
#%{_prefix}/src/openafs-kernel-%{afsvers}/Makefile
#%{_prefix}/src/openafs-kernel-%{afsvers}/src
