%define		modname img_assist
Summary:	Drupal Img_assist Module
Summary(pl.UTF-8):   Moduł Img_assist dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.17
License:	GPL
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	4a38eb192ea4e1276ee6043067271003
URL:		http://drupal.org/project/img_assist
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	drupal >= 4.6.0
Requires:	drupal-mod-image
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules
%define		_htdocs		%{_drupaldir}/htdocs
%define		_htmlmoddir	%{_htdocs}/modules

%description
This module generates an image icon next to the textarea fields of you
choice. Clicking the icon opens an image browsing window, displaying
all images that have been uploaded through image module, upload module
or img_assist. Images can be filtered by ownership or taxonomic terms
(categories). 

Img_assist can also be used when adding images from a rich-text
editor. This feature currently exists for TinyMCE. Support for
Htmlarea is also planned.

%description -l pl.UTF-8
Ten moduł generuje ikony przy wybranych polach tekstowych. Kliknięcie
ikony otwiera okno przeglądania obrazków, wyświetlając wszystkie
obrazki umieszczone poprzez moduł image, moduł upload albo img_assist.
Obrazki mogą być filtrowane po właścicielu lub warunkach
systematycznych (kategoriach).

Img_assist można także używać do dodawania obrazków z edytora
rich-tekstu. Ta opcja aktualnie istnieje dla TinyMCE. Planowana jest
także obsługa Htmlarea.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # pure GPL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_moddir},%{_htmlmoddir}}

install *.module $RPM_BUILD_ROOT%{_moddir}
install *.css *.js *.jpg $RPM_BUILD_ROOT%{_htmlmoddir}
ln -s ../htdocs/modules/directory.js $RPM_BUILD_ROOT%{_moddir}
ln -s ../htdocs/modules/properties.js $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
To create tables needed for Drupal Img Assist module, issue these commands:
zcat %{_docdir}/%{name}-%{version}/%{modname}.mysql.gz | mysql drupal
EOF
fi

%files
%defattr(644,root,root,755)
%doc *.txt img_assist.{mysql,pgsql}
%{_moddir}/*.module
%{_moddir}/*.js
%{_htmlmoddir}/*.*
