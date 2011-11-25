%define git 8c9856b
Name:		daemonize
Version:	1.7.3
Release:	%mkrel 1
Summary:	Run a command as a Unix daemon
# $UPSTREAM no longer supplies hand made .tar.gz-Files for releases 
# so a github tarball it is:
# https://github.com/bmc/daemonize/tarball/release-1.7.3
Source: %name-%version.tar.gz
URL:		http://www.clapper.org/software/daemonize/
License:	BSD
Group:		System/Servers
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
daemonize runs a command as a Unix daemon. As defined in W. Richard
Stevens' 1990 book, Unix Network Programming (Addison-Wesley, 1990), a
daemon is "a process that executes 'in the background' (i.e., without
an associated terminal or login shell) either waiting for some event to
occur, or waiting to perform some specified task on a periodic basis."

Upon startup, a typical daemon program will:
- Close all open file descriptors (especially standard input, standard
  output and standard error)
- Change its working directory to the root filesystem, to ensure that
  it doesn't tie up another filesystem and prevent it from being unmounted
- Reset its umask value
- Run in the background (i.e., fork)
- Disassociate from its process group (usually a shell), to insulate
  itself from signals (such as HUP) sent to the process group
- Ignore all terminal I/O signals
- Disassociate from the control terminal (and take steps not to
  reacquire one)
- Handle any SIGCLD signals

Most programs that are designed to be run as daemons do that work for
themselves. However, you'll occasionally run across one that does not.
When you must run a daemon program that does not properly make itself
into a true Unix daemon, you can use daemonize to force it to run as a
true daemon.

%prep
%setup -q -n bmc-%name-%git

%build
%configure2_5x
%make

%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -m 0755 %{name} %{buildroot}%{_sbindir}
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__install} -m 0755 %{name}.1 %{buildroot}%{_mandir}/man1

%files
%doc README.md CHANGELOG.md LICENSE.md
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*
