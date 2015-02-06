Summary: 	WindowMaker dockapp CPU, memory, swap and load average monitor
Name:		bubblemon
Version:	1.46
Release:	7
License:	GPLv2+
Group:          Graphical desktop/WindowMaker
Source0:	%{name}-dockapp-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch0:		%{name}-1.46-fix-overlinking.patch
URL:		http://www.ne.jp/asahi/linux/timecop/
BuildRequires:	pkgconfig(x11)
BuildRequires:  xpm-devel 
BuildRequires:  gtk+-devel = 1.2.10

%description
 This is a system monitoring dockapp, visually based on the GNOME "BubbleMon"
 applet. Basically, it displays CPU and memory load as bubbles in a jar of
 water. But that is where similarity ends. New bubblemon-dockapp features
 translucent CPU load meter (for accurate CPU load measurement), yellow duck
 swimming back and forth on the water surface (just for fun), and fading load
 average and memory usage screens. Either of the info screens can be locked to
 stay on top of water/duck/cpu screen, so that you can see both statistics at
 once. Pretty nifty toy for your desktop. Code has been thoroughly optimized
 since version 1.0, and even with all the features compiled in, BubbleMon still
 uses very little CPU time. All the extra "bloated" features can be compiled
 out or disabled on command-line, if you prefer original "BubbleMon" look.

%prep
%setup -q -n %{name}-dockapp-%{version}
%patch0 -p1

%build
make EXTRA="-DENABLE_DUCK -DENABLE_CPU -DENABLE_MEMSCREEN" \
CFLAGS="$RPM_OPT_FLAGS `gtk-config --cflags` \${EXTRA} \${WMAN}"
     
%install
[ -d %buildroot ] && rm -rf %buildroot

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
tar xOjf %SOURCE1 %{name}-16x16.png > %buildroot%{_miconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-32x32.png > %buildroot%{_iconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-48x48.png > %buildroot%{_liconsdir}/%{name}.png

install -m 755 bubblemon -D %buildroot%{_bindir}/bubblemon


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Monitoring-duck-in-a-jar dockapp
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-System-Monitoring;System;Monitor;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr (-,root,root)
%doc ChangeLog README SUPPORTED_SYSTEMS doc/Xdefaults.sample
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 1.46-5mdv2011.0
+ Revision: 571833
- use libx11-devel

* Tue Jun 16 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 1.46-5mdv2010.0
+ Revision: 386385
- fix overlinking
- fix license tag

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.46-4mdv2009.0
+ Revision: 243370
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.46-2mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import bubblemon


* Fri Sep 01 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.46-2mdv2007.0
- XDG

* Fri Jul 22 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.46-1mdk
- New release 1.46

* Sun Dec 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.41-1mdk
- 1.4.1
- drop Prefix tag
- fix buildrequires
- drop explicit library dependency
- quiet setup

* Wed Jul 16 2003 HA Quôc-Viêt <viet@mandrakesoft.com> 1.4-2mdk
- added libgtk+1.2-devel to BuildRequires thanks to
  Michael Scherer <scherer.michael@free.fr>

* Mon Feb 11 2002 HA Quôc-Viêt <viet@mandrakesoft.com> 1.4-1mdk
- new source update.
- icons converted from xpm to png.
- s/Copyright/License/
- compile options are now working.

* Thu May 31 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 1.32-1mdk
- Initial release.
