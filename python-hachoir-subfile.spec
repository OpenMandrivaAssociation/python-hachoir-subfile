%define module_name hachoir-subfile

Summary:	A tool based on hachoir-parser to find subfiles in any binary stream
Name:		python-%{module_name}
Version:	0.5.3
Release:	4
Source0:	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		https://hachoir.org/wiki/hachoir-metadata
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


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 0.5.3-3mdv2011.0
+ Revision: 598269
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5.3-3mdv2010.0
+ Revision: 442179
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.5.3-2mdv2009.1
+ Revision: 323732
- fix summary
- rebuild

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild with python 2.6
    - clean spec
    - new release 0.5.3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 17 2007 Jérôme Soyer <saispo@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 52873
- Import python-hachoir-subfile

