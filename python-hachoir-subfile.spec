%define module_name hachoir-subfile

Summary:	A tool based on hachoir-parser to find subfiles in any binary stream
Name:		python-%{module_name}
Version:	0.5.3
Release:	%mkrel 3
Source0:	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://hachoir.org/wiki/hachoir-metadata
BuildArch:	noarch
Requires:	python-hachoir-core
Requires:	python-hachoir-parser
Requires:	python-hachoir-regex
BuildRequires:	python-setuptools

%description
A tool based on hachoir-parser to find subfiles in any binary stream.

%prep
%setup -q -n %{module_name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/*
%{py_puresitedir}/*
