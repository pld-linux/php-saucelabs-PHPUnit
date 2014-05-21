%define		_status		stable
%define		_pearname PHPUnit
%define		php_min_version 5.2.7
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - regression testing framework for unit tests
Summary(pl.UTF-8):	%{_pearname} - zestaw testów regresyjnych
Name:		php-saucelabs-%{_pearname}
Version:	3.5.24
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://saucelabs.github.com/pear/get/PHPUnit-%{version}.tgz
# Source0-md5:	1feb243062a70292b9707b992dee5d85
URL:		http://www.phpunit.de/
BuildRequires:	php-channel(components.ez.no)
BuildRequires:	php-channel(pear.symfony-project.com)
BuildRequires:	php-channel(saucelabs.github.com/pear)
BuildRequires:	php-pear >= 4:1.1-2
BuildRequires:	php-pear-PEAR >= 1:1.9.2
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.473
Requires:	php(core) >= %{php_min_version}
Requires:	php(dom)
Requires:	php(pcre)
Requires:	php(reflection)
Requires:	php(spl)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear >= 4:1.1-2
Requires:	php-pear-XML_RPC2
Requires:	php-phpunit-DbUnit >= 1.0.0
Requires:	php-phpunit-File_Iterator >= 1.2.3
Requires:	php-phpunit-PHPUnit_MockObject >= 1.0.3
Requires:	php-phpunit-PHPUnit_Selenium >= 1.0.1
Requires:	php-phpunit-PHP_CodeCoverage >= 1.0.2
Requires:	php-phpunit-PHP_Timer >= 1.0.0
Requires:	php-phpunit-Text_Template >= 1.0.0
Requires:	php-symfony-YAML >= 1.0.2
Suggests:	php(curl)
Suggests:	php(json)
Suggests:	php(pdo)
Suggests:	php(simplexml)
Suggests:	php(soap)
Suggests:	php(tokenizer)
Suggests:	php-dbus
Provides:	php-PHPUnit = %{version}
Obsoletes:	php-PHPUnit < 3.5
Obsoletes:	php-PHPUnit-tests
Obsoletes:	php-pear-PHPUnit
Obsoletes:	php-pear-PHPUnit2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		dep_optional	pear(Image/GraphViz.*) pear(Log.*) pear(SymfonyComponents/.*) pear(XML/RPC2/Client.php)

# put it together for rpmbuild
%define		_noautoreq	%{?dep_optional} %{?dep_missing}

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

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
install -d $RPM_BUILD_ROOT%{_bindir}
install -p usr/bin/phpunit $RPM_BUILD_ROOT%{_bindir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/.channel.saucelabs.github.com_pear/phpunit.reg
%attr(755,root,root) %{_bindir}/phpunit
%{php_pear_dir}/PHPUnit
