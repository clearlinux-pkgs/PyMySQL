#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyMySQL
Version  : 0.9.3
Release  : 43
URL      : https://github.com/PyMySQL/PyMySQL/archive/v0.9.3/PyMySQL-0.9.3.tar.gz
Source0  : https://github.com/PyMySQL/PyMySQL/archive/v0.9.3/PyMySQL-0.9.3.tar.gz
Summary  : Pure Python MySQL Driver
Group    : Development/Tools
License  : MIT
Requires: PyMySQL-license = %{version}-%{release}
Requires: PyMySQL-python = %{version}-%{release}
Requires: PyMySQL-python3 = %{version}-%{release}
Requires: cryptography
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : mariadb-dev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://readthedocs.org/projects/pymysql/badge/?version=latest
:target: https://pymysql.readthedocs.io/
:alt: Documentation Status

%package license
Summary: license components for the PyMySQL package.
Group: Default

%description license
license components for the PyMySQL package.


%package python
Summary: python components for the PyMySQL package.
Group: Default
Requires: PyMySQL-python3 = %{version}-%{release}
Provides: pymysql-python

%description python
python components for the PyMySQL package.


%package python3
Summary: python3 components for the PyMySQL package.
Group: Default
Requires: python3-core
Provides: pypi(pymysql)

%description python3
python3 components for the PyMySQL package.


%prep
%setup -q -n PyMySQL-0.9.3
cd %{_builddir}/PyMySQL-0.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583520650
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PyMySQL
cp %{_builddir}/PyMySQL-0.9.3/LICENSE %{buildroot}/usr/share/package-licenses/PyMySQL/a3ba1a249c942e693e09d101a88cba21c82e9479
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyMySQL/a3ba1a249c942e693e09d101a88cba21c82e9479

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
