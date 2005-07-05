%define		modname img_assist
Summary:	Drupal Img_assist Module
Summary(pl):	Modu³ Img_assist dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.6
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	4b1c6d159005fee95ed40b6fd17085d4
URL:		http://drupal.org/project/img_assist
Requires:	drupal >= 4.6.0
Requires:	drupal-mod-image
Requires:	drupal-mod-upload
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_moddir		%{_datadir}/drupal/modules

%description
This module generates an image icon next to the textarea fields of you
choice. Clicking the icon opens an image browsing window, displaying
all images that have been uploaded through image module, upload module
or img_assist. Images can be filtered by ownership or taxonomic terms
(categories). 

Img_assist can also be used when adding images from a rich-text
editor. This feature currently exists for TinyMCE. Support for
Htmlarea is also planned.

%description -l pl
Ten modu³ generuje ikony przy wybranych polach tekstowych. Klikniêcie
ikony otwiera okno przegl±dania obrazków, wy¶wietlaj±c wszystkie
obrazki umieszczone poprzez modu³ image, modu³ upload albo img_assist.
Obrazki mog± byæ filtrowane po w³a¶cicielu lub warunkach
systematycznych (kategoriach).

Img_assist mo¿na tak¿e u¿ywaæ do dodawania obrazków z edytora
rich-tekstu. Ta opcja aktualnie istnieje dla TinyMCE. Planowana jest
tak¿e obs³uga Htmlarea.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # pure GPL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}
# FIXME directory
install *.css *.js *.jpg $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt img_assist.{mysql,pgsql}
%{_moddir}/*.module
# TODO
%{_moddir}/*.js
%{_moddir}/*.css
%{_moddir}/*.jpg
