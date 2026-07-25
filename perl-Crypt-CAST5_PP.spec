%define	modname	Crypt-CAST5_PP
%define modver	1.04

Summary:	CAST5 block cipher in pure Perl
Name:		perl-%{modname}
Version:	%{modver}
Release:	18
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/dist/Crypt-CAST5_PP
Source0:	https://cpan.metacpan.org/authors/id/B/BO/BOBMATH/Crypt-CAST5_PP-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
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

