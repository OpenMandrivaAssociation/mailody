# Basic macros
%define name    mailody 
%define version 1.5.0

# Macros for in the menu-file.
%define section Internet 
%define title Mailody


Name:           %{name}
Version:        %{version}
Summary:        IMAP only, Qt4/KDE4 based mail client 
Release:        %mkrel 0.beta1.2
License:        GPL
Group:          Networking/Mail
URL:            http://mailody.net

Source0:        http://prdownloads.sourceforge.net/%{name}/kde4-%{name}-%{version}beta1.tar.bz2

BuildRoot:      %_tmppath/%name-%version-%release-buildroot

BuildRequires: kdelibs4-devel
BuildRequires: libsqlite3-devel
BuildRequires: libqca-devel
BuildRequires: kdeedu4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: boost-devel

%description
Mailody is an IMAP-only mail client. Based on Qt and KDE.

%files  -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/%{name}
%{_kde_appsdir}/%{name}
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_libdir}/kde4/kontact_mailodyplugin.so
%{_kde_libdir}/kde4/mailodypart.so
%{_kde_datadir}/dbus-1/interfaces/net.mailody.mainwindow.xml
%{_kde_datadir}/kde4/services/kontact/mailody_plugin.desktop
%{_kde_datadir}/kde4/services/mailodypart.desktop
%{_kde_docdir}/HTML/en/mailody

#--------------------------------------------------------------------

%prep
%setup -q  -n kde4-%{name}-%{version}beta1

%build

%cmake_kde4
%make


%install
rm -rf %buildroot
cd build
make DESTDIR=%buildroot install
cd ..
%{find_lang} %{name}

%clean
rm -rf %{buildroot}

