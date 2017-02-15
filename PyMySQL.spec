#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyMySQL
Version  : 0.7.10
Release  : 20
URL      : http://pypi.debian.net/PyMySQL/PyMySQL-0.7.10.tar.gz
Source0  : http://pypi.debian.net/PyMySQL/PyMySQL-0.7.10.tar.gz
Summary  : Pure Python MySQL Driver
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
.. image:: https://readthedocs.org/projects/pymysql/badge/?version=latest
:target: http://pymysql.readthedocs.io/en/latest/?badge=latest
:alt: Documentation Status

%package python
Summary: python components for the PyMySQL package.
Group: Default
Provides: pymysql-python

%description python
python components for the PyMySQL package.


%prep
%setup -q -n PyMySQL-0.7.10

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487186016
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487186016
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
