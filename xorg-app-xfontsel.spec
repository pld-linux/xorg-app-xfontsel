Summary:	xfontsel application - point and click selection of X11 font names
Summary(pl.UTF-8):	Aplikacja xfontsel - wybór fontów X11 przy użyciu myszki
Name:		xorg-app-xfontsel
Version:	1.1.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xfontsel-%{version}.tar.xz
# Source0-md5:	5fc779e2f68c03c781521944c4c5060b
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xfontsel application provides a simple way to display the fonts
known to your X server, examine samples of each, and retrieve the X
Logical Font Description (XLFD) full name for a font.

%description -l pl.UTF-8
Aplikacja xfontsel udostępnia łatwy sposób wyświetlania fontów
widocznych dla serwera X, oglądanie ich przykładów i odczytywanie
pełnych nazw XLFD (X Logical Font Description) dla fontów.

%prep
%setup -q -n xfontsel-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xfontsel
%{_datadir}/X11/app-defaults/XFontSel
%{_mandir}/man1/xfontsel.1*
