#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Carp
%define		pnam	Assert-More
Summary:	Carp::Assert::More - convenience wrappers around Carp::Assert
Name:		perl-Carp-Assert-More
Version:	1.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e056db5883a4ec7cdd62443046aa7e0a
URL:		http://search.cpan.org/dist/Carp-Assert-More/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Pod-Tests >= 0.18
BuildRequires:	perl-Test-Simple >= 0.40
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Carp::Assert::More is a set of wrappers around the Carp::Assert
functions to make the habit of writing assertions even easier.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%dir %{perl_vendorlib}/Carp/Assert
%{perl_vendorlib}/Carp/Assert/More.pm
%{_mandir}/man3/*
