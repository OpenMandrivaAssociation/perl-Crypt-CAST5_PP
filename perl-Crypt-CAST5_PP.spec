%define	modname	Crypt-CAST5_PP
%define modver	1.04

Summary:	CAST5 block cipher in pure Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module provides a pure Perl implementation of the CAST5 block cipher.
CAST5 is also known as CAST-128. It is a product of the CAST design procedure
developed by C. Adams and S. Tavares.

The CAST5 cipher is available royalty-free.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Crypt/*
%{perl_vendorlib}/auto/Crypt/*
%{_mandir}/man3/*

