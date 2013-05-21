%define	upstream_name	 Crypt-CAST5_PP
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	CAST5 block cipher in pure Perl
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides a pure Perl implementation of the CAST5 block cipher.
CAST5 is also known as CAST-128. It is a product of the CAST design procedure
developed by C. Adams and S. Tavares.

The CAST5 cipher is available royalty-free.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Crypt/*
%{perl_vendorlib}/auto/Crypt/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-4mdv2012.0
+ Revision: 765121
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-3
+ Revision: 763618
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-2
+ Revision: 676565
- rebuild

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 408944
- rebuild using %%perl_convert_version

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.04-1mdv2008.1
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 22 2007 Buchan Milne <bgmilne@mandriva.org> 1.04-1mdv2008.0
+ Revision: 42904
- Import perl-Crypt-CAST5_PP



* Thu Jun 21 2007 Buchan Milne <bgmilne@mandriva.org> 1.04-1mdv2007.1
- initial package
