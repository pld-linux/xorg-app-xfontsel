Summary:	xfontsel application - point and click selection of X11 font names
Summary(pl.UTF-8):   Aplikacja xfontsel - wybór fontów X11 przy użyciu myszki
Name:		xorg-app-xfontsel
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xfontsel-%{version}.tar.bz2
# Source0-md5:	288fe4cf8a990e4e602aac16dd9109fb
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xfontsel
%{_datadir}/X11/app-defaults/XFontSel
%{_mandir}/man1/xfontsel.1x*
