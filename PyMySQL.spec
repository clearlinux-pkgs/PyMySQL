#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyMySQL
Version  : 0.6.7
Release  : 6
URL      : https://pypi.python.org/packages/source/P/PyMySQL/PyMySQL-0.6.7.tar.gz
Source0  : https://pypi.python.org/packages/source/P/PyMySQL/PyMySQL-0.6.7.tar.gz
Summary  : Pure-Python MySQL Driver
Group    : Development/Tools
License  : MIT
Requires: PyMySQL-python
BuildRequires : mariadb-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
=======
PyMySQL
=======
.. image:: https://travis-ci.org/PyMySQL/PyMySQL.svg?branch=master
:target: https://travis-ci.org/PyMySQL/PyMySQL

%package python
Summary: python components for the PyMySQL package.
Group: Default
Provides: pymysql-python

%description python
python components for the PyMySQL package.


%prep
%setup -q -n PyMySQL-0.6.7

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*