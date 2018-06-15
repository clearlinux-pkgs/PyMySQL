#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyMySQL
Version  : 0.8.1
Release  : 24
URL      : https://github.com/PyMySQL/PyMySQL/archive/v0.8.1.tar.gz
Source0  : https://github.com/PyMySQL/PyMySQL/archive/v0.8.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: PyMySQL-python3
Requires: PyMySQL-python
BuildRequires : mariadb-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://readthedocs.org/projects/pymysql/badge/?version=latest
:target: http://pymysql.readthedocs.io/en/latest/?badge=latest
:alt: Documentation Status

%package python
Summary: python components for the PyMySQL package.
Group: Default
Requires: PyMySQL-python3
Provides: pymysql-python

%description python
python components for the PyMySQL package.


%package python3
Summary: python3 components for the PyMySQL package.
Group: Default
Requires: python3-core

%description python3
python3 components for the PyMySQL package.


%prep
%setup -q -n PyMySQL-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528569657
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
