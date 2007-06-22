%define	module	Crypt-CAST5_PP
%define name	perl-%{module}
%define	modprefix Crypt

%define version 1.04

%define	rel	1
%define release %mkrel %{rel}

Summary:	CAST5 block cipher in pure Perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root


%description
This module provides a pure Perl implementation of the CAST5 block cipher.
CAST5 is also known as CAST-128. It is a product of the CAST design procedure
developed by C. Adams and S. Tavares.

The CAST5 cipher is available royalty-free.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/%{modprefix}/*
%{perl_vendorlib}/auto/%{modprefix}/*
%{_mandir}/*/*
