%define module_name hachoir-subfile

Summary:     	A tool based on hachoir-parser to find subfiles in any binary stream.	
Name: 		python-%{module_name}
Version: 	0.5.2
Release: 	%mkrel 1
Source0: 	%{module_name}-%{version}.tar.bz2
License:	GPL
Group: 		Development/Python
Url: 		http://hachoir.org/wiki/hachoir-metadata
BuildArch:  noarch
Requires:   python-hachoir-core
Requires:   python-hachoir-parser
Requires:   python-hachoir-regex
BuildRequires: python-devel
%description
A tool based on hachoir-parser to find subfiles in any binary stream.

%prep
%setup -q -n %{module_name}-%version

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%dir %py_puresitedir/hachoir_subfile
