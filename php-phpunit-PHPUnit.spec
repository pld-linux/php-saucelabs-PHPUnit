%include	/usr/lib/rpm/macros.php
%define		_class		PHPUnit
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl.UTF-8):	%{_pearname} - zestaw testów regresyjnych
Name:		php-%{_pearname}
Version:	3.2.21
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/PHPUnit-%{version}.tgz
# Source0-md5:	183b09907e341006e549476efaa18442
Source1:	http://pear.phpunit.de/channel.xml
# Source1-md5:	b8ccb5f4727e7e6d4ee0c0e690f5423b
URL:		http://www.phpunit.de/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.473
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Image/GraphViz.*)' 'pear(Log.*)'

%description
PHPUnit is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at <http://www.junit.org/>.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PHPUnit jest zestawem testów regresyjnych używanych przez developerów,
którzy implementują jednostki testowe w PHP. Jest bazowane na JUnit,
który można znaleźć pod adresem <http://www.junit.org/>.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup -c %{SOURCE1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# also copy channel information
install -d $RPM_BUILD_ROOT%{php_pear_dir}/.channels
cp -a .%{php_pear_dir}/.channels/pear.phpunit.de.reg $RPM_BUILD_ROOT%{php_pear_dir}/.channels

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/.channel.pear.phpunit.de/*.reg
# these should not be in this package
%dir %{php_pear_dir}/.registry/.channel.pear.phpunit.de
%{php_pear_dir}/.channels/pear.phpunit.de.reg

%{php_pear_dir}/%{_class}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}