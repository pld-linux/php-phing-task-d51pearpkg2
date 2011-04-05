%define		pearname	Phing_d51PearPkg2Task
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	An alternative pearpkg2 task
Name:		php-phing-task-d51pearpkg2
Version:	0.6.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.domain51.com//get/Phing_d51PearPkg2Task-%{version}.tgz
# Source0-md5:	9d078e639b57a4bfe4b51f28da0f2011
Source1:	http://pear.domain51.com/channel.xml
# Source1-md5:	fb770e47fd1714347e5a7ab7c7bb3f58
URL:		https://github.com/domain51/Phing_d51PearPkg2Task
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.593
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-phing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		phingdir	%{php_data_dir}/phing
%define		tasksdir	%{phingdir}/tasks/ext

# self deps
%define		_noautoreq	pear(phing/tasks/ext/d51PearPkg2Task/.*.php)

%description
This package provides an alternative to Phing bundled pearpkg2,
allowing for a build script that more closely resemble a real
package.xml 2.0 file or using the API that is available by using
PEAR_PackageFileManager2.

%prep
%pear_package_setup -c %{SOURCE1}

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a ./%{php_pear_dir}/* $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{tasksdir}/d51PearPkg2Task.php
%{tasksdir}/d51PearPkg2Task
