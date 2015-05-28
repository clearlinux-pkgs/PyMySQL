#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyMySQL
Version  : 0.6.6
Release  : 3
URL      : https://pypi.python.org/packages/source/P/PyMySQL/PyMySQL-0.6.6.tar.gz
Source0  : https://pypi.python.org/packages/source/P/PyMySQL/PyMySQL-0.6.6.tar.gz
Summary  : Pure-Python MySQL Driver
Group    : Development/Tools
License  : MIT
Requires: PyMySQL-python
BuildRequires : mariadb-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

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
%setup -q -n PyMySQL-0.6.6

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
