Summary:	Filesystem benchmark
Name:		filebench
Version:	1.64
Release:	0.1
License:	CDDL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/filebench/%{name}-%{version}-alpha-src.tar.gz
# Source0-md5:	4651a3a75291f2184c5cd39ae38bc19c
URL:		http://www.solarisinternals.com/wiki/index.php/FileBench
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gsl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filebench is quick to set up and use unlike many of the commercial
benchmarks which it can emulate. It is also a handy tool for
micro-benchmarking storage subsystems and studying the relationships
of complex applications such as relational databases with their
storage without having to incur the costs of setting up those
applications, loading data and so forth.

Filebench uses loadable workload personalities in a common framework
to allow easy emulation of complex applications upon file systems. The
workload personalities use a Workload Definition Language to define
the workload's model.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
