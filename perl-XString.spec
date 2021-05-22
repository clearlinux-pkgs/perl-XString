#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XString
Version  : 0.005
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/XString-0.005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/XString-0.005.tar.gz
Summary  : 'Isolated String helpers from B'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-XString-license = %{version}-%{release}
Requires: perl-XString-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution XString,
version 0.005:
Isolated String helpers from B

%package dev
Summary: dev components for the perl-XString package.
Group: Development
Provides: perl-XString-devel = %{version}-%{release}
Requires: perl-XString = %{version}-%{release}

%description dev
dev components for the perl-XString package.


%package license
Summary: license components for the perl-XString package.
Group: Default

%description license
license components for the perl-XString package.


%package perl
Summary: perl components for the perl-XString package.
Group: Default
Requires: perl-XString = %{version}-%{release}

%description perl
perl components for the perl-XString package.


%prep
%setup -q -n XString-0.005
cd %{_builddir}/XString-0.005

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XString
cp %{_builddir}/XString-0.005/LICENSE %{buildroot}/usr/share/package-licenses/perl-XString/bd01b61740795eaefc30a3d7ce4bc6de6b114892
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XString.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XString/bd01b61740795eaefc30a3d7ce4bc6de6b114892

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/XString.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/XString/XString.so
