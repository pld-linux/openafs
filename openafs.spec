#
# TODO: FHS compliance (what is /afs, /usr/afs, /usr/vice, /usr/doc???)
#
#%define	kernver	2.2.0
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
Requires:	openafs-kernel
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
na kontrolê dostêpu, autentykacjê, backup i administrowanie.

Ten pakiet zawiera pliki wspólne dla klienta i serwera AFS.

%package client
Summary:	OpenAFS Filesystem Client
Summary(pl):	Klient systemu plików OpenAFS
Group:		Networking/Daemons
Requires:	openafs-kernel openafs

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
na kontrolê dostêpu, autentykacjê, backup i administrowanie.

Ten pakiet zawiera klienta do montowania i manipulowania AFS.

%package server
Summary:	OpenAFS Filesystem Server
Summary(pl):	Serwer systemu plików OpenAFS
Group:		Networking/Daemons
Requires:	openafs-kernel openafs

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
na kontrolê dostêpu, autentykacjê, backup i administrowanie.

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
na kontrolê dostêpu, autentykacjê, backup i administrowanie.

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
na kontrolê dostêpu, autentykacjê, backup i administrowanie.

Ten pakiet zawiera prekompilowane modu³y j±dra do AFS.

%package kernel-source
Summary:	OpenAFS Kernel Module source tree
Summary(pl):	¬ród³a modu³u j±dra AFS
Group:		Networking/Daemons

%description kernel-source
The AFS distributed filesystem. AFS is a distributed filesystem
allowing cross-platform sharing of files among multiple computers.
Facilities are provided for access control, authentication, backup and
administrative management.

This package provides the source code to build your own AFS kernel
module.

%description kernel-source -l pl
AFS jest rozproszonym systemem plików pozwalaj±cym na dzielenie plików
miêdzy wieloma komputerami, tak¿e na ró¿nych platformach. AFS pozwala
na kontrolê dostêpu, autentykacjê, backup i administrowanie.

Ten pakiet zawiera ¼ród³a do samodzielnego skompilowania modu³u AFS.

%prep
%setup -q
%patch0 -p0
#%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure --with-linux-kernel-headers=%{_kernelsrcdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/asf,,/etc/{sysconfig,rc.d/init.d}} \
	$RPM_BUILD_ROOT{%{_sysconfdir}/openafs,/lib/security} \
	$RPM_BUILD_ROOT%{_prefix}/{afs/logs,/vice/{etc,cache}}

# Copy files from dest to the appropriate places in BuildRoot
tar cf - -C dest bin include lib | tar xf - -C $RPM_BUILD_ROOT%{_prefix}
tar cf - -C dest%{_sysconfdir} . | tar xf - -C $RPM_BUILD_ROOT%{_sbindir}
tar cf - -C dest/root.server%{_prefix}/afs bin | tar xf - -C $RPM_BUILD_ROOT%{_prefix}/afs
tar cf - -C dest/root.client%{_prefix}/vice%{_sysconfdir} afsd modload | tar xf - -C $RPM_BUILD_ROOT%{_prefix}/vice%{_sysconfdir}

# Copy root.client config files
install dest/root.client%{_prefix}/vice%{_sysconfdir}/afs.conf $RPM_BUILD_ROOT/etc/sysconfig/afs
install dest/root.client%{_prefix}/vice%{_sysconfdir}/afs.rc $RPM_BUILD_ROOT/etc/rc.d/init.d/afs

# Copy PAM modules
install dest/lib/pam* $RPM_BUILD_ROOT/lib/security

# Populate %{_prefix}/vice%{_sysconfdir}
tar cf - -C redhat%{_prefix}_vice_etc . | tar xf - -C $RPM_BUILD_ROOT%{_prefix}/vice%{_sysconfdir}

#
# install kernel-source
#

# Install the kernel module source tree
install -d $RPM_BUILD_ROOT%{_prefix}/src/openafs-kernel-%{afsvers}/src
tar cf - -C obj/libafs Makefile afs afsint rx | tar xf - -C $RPM_BUILD_ROOT%{_prefix}/src/openafs-kernel-%{afsvers}/src

# Copy Makefile.common, by hand (it's usually a symlink)
install obj/libafs/Makefile.common $RPM_BUILD_ROOT%{_prefix}/src/openafs-kernel-%{afsvers}/src

# Next, copy the LICENSE, README, and top-level Makefile
install src/LICENSE $RPM_BUILD_ROOT%{_prefix}/src/openafs-kernel-%{afsvers}/LICENSE.IBM
install redhat/LICENSE.Sun $RPM_BUILD_ROOT%{_prefix}/src/openafs-kernel-%{afsvers}
install redhat/README $RPM_BUILD_ROOT%{_prefix}/src/openafs-kernel-%{afsvers}
install redhat/Makefile $RPM_BUILD_ROOT%{_prefix}/src/openafs-kernel-%{afsvers}

# Patch the Makefile
cat redhat/Makefile.libafs.patch | (cd $RPM_BUILD_ROOT%{_prefix}/src/openafs-kernel-%{afsvers}/src; patch)

#
# Install DOCUMENTATION
#

# Build the DOC directory
install -d $RPM_BUILD_ROOT%{_prefix}/doc/openafs-%{afsvers}
install src/LICENSE $RPM_BUILD_ROOT%{_prefix}/doc/openafs-%{afsvers}

###
### clean
###
%clean
rm -rf $RPM_BUILD_ROOT

###
### scripts
###
%post
/sbin/chkconfig --add afs
if [ -f /var/lock/subsys/afs ]; then
	/etc/rc.d/init.d/afs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/afs start\" to start AFS server." >&2
fi

%post client
echo
echo The AFS cache is configured for 100 MB. Edit the
echo /usr/vice/etc/cachinfo file to change this before
echo running AFS for the first time. You should also
echo set your home cell in /usr/vice/etc/ThisCell.
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

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/afs ]; then
		/etc/rc.d/init.d/afs stop
	fi
	/sbin/chkconfig --del afs
fi

###
### file lists
###
%files
%defattr(644,root,root,755)
%dir %{_prefix}/vice%{_sysconfdir}/modload
%config /etc/sysconfig/afs
%doc %{_prefix}/doc/openafs-%{afsvers}
/etc/rc.d/init.d/afs
%attr(755,root,root) %{_bindir}/bos
%attr(755,root,root) %{_bindir}/fs
%attr(755,root,root) %{_bindir}/klog
%attr(755,root,root) %{_bindir}/klog.krb
%attr(755,root,root) %{_bindir}/pagsh
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

%files client
%defattr(644,root,root,755)
%dir /afs
%dir %{_prefix}/vice/cache
%config %{_prefix}/vice%{_sysconfdir}/CellServDB
%config %{_prefix}/vice%{_sysconfdir}/SuidCells
%config %{_prefix}/vice%{_sysconfdir}/ThisCell
%config %{_prefix}/vice%{_sysconfdir}/cacheinfo
%attr(755,root,root) %{_bindir}/cmdebug
%{_prefix}/vice%{_sysconfdir}/afsd
/lib/security/pam_afs.krb.so.1
/lib/security/pam_afs.so.1

%files server
%defattr(644,root,root,755)
%dir %{_prefix}/afs
%dir %{_prefix}/afs/bin
%dir %{_prefix}/afs/logs
%{_prefix}/afs/bin/bosserver
%{_prefix}/afs/bin/buserver
%{_prefix}/afs/bin/fileserver
# Should we support KAServer?
%{_prefix}/afs/bin/kaserver
%{_prefix}/afs/bin/kpwvalid
%{_prefix}/afs/bin/ptserver
%{_prefix}/afs/bin/salvager
%{_prefix}/afs/bin/upclient
%{_prefix}/afs/bin/upserver
%{_prefix}/afs/bin/vlserver
%{_prefix}/afs/bin/volinfo
%{_prefix}/afs/bin/volserver
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
%{_includedir}/itc.h
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
%{_prefix}/vice%{_sysconfdir}/modload/libafs*.o

%files kernel-source
%defattr(644,root,root,755)
%{_prefix}/src/openafs-kernel-%{afsvers}/LICENSE.IBM
%{_prefix}/src/openafs-kernel-%{afsvers}/LICENSE.Sun
%{_prefix}/src/openafs-kernel-%{afsvers}/README
%{_prefix}/src/openafs-kernel-%{afsvers}/Makefile
%{_prefix}/src/openafs-kernel-%{afsvers}/src
