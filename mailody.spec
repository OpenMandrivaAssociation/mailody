# Basic macros
%define name    mailody 
%define version 0.5.0

# Macros for in the menu-file.
%define section Internet 
%define title Mailody


Name:           %{name}
Version:        %{version}
Summary:        IMAP only, Qt/KDE based mail client 
Release:        %mkrel 1
License:        GPL
Group:          Networking/Mail
URL:            http://mailody.net

Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:         mailody-fix-smtp-gmail.patch
Patch1:         mailody-imapmanager_removeflagfix.patch


BuildRoot:      %_tmppath/%name-%version-%release-buildroot

BuildRequires: kdelibs-devel
BuildRequires: X11-devel
BuildRequires: libsqlite3-devel
BuildRequires: libqca-devel
BuildRequires: desktop-file-utils

%description
Mailody is an IMAP-only mail client. Based on Qt and KDE.

%prep
%setup -q  -n %{name}-%{version}
(
%patch0 -p0
%patch1 -p1
)

%build
make -f Makefile.cvs
%configure
%make


%install
rm -rf %buildroot
%makeinstall
desktop-file-install --vendor="" \
  --add-category="Network" \
  --add-category="Email" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde %{name}/src/%{name}.desktop


%{find_lang} %{name}

%post
%update_menus

%postun
%clean_menus

%files  -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING AUTHORS ChangeLog INSTALL NEWS
%{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/applications/kde/%{name}.desktop
%{_iconsdir}/*/*/*/*
%{_docdir}/HTML/en/mailody

%clean
rm -rf %{buildroot}

