%define upstream_name    Sys-Info
%define upstream_version 0.73

Summary:	Fetch information from the host system
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SYS/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl-Test-Sys-Info
BuildRequires:	perl-Sys-Info-Base
BuildRequires:	perl-Sys-Info-Driver-Linux
Requires:	perl-Sys-Info-Driver-Linux
Requires:	perl-Sys-Info-Base
BuildArch:	noarch

%description
Perl for fetch system information from the host.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Require ifconfig access etc
#make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Thu Jan 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.730.0-1mdv2010.1
+ Revision: 491169
- update to 0.73

* Sat Jan 02 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.720.0-1mdv2010.1
+ Revision: 484930
- import perl-Sys-Info


