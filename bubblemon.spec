Summary: 	WindowMaker dockapp CPU, memory, swap and load average monitor
Name:		bubblemon
Version:	1.46
Release:	%mkrel 2
License:	GPL
Group:          Graphical desktop/WindowMaker
Source0:	%{name}-dockapp-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://www.ne.jp/asahi/linux/timecop/
BuildRequires:	X11-devel 
BuildRequires:  xpm-devel 
BuildRequires:  gtk+-devel = 1.2.10
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

install -m 755 -d %buildroot%{_menudir}
cat << EOF > %buildroot%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name} -b" icon="%{name}.png"\\
                 needs="X11" section="Applications/Monitoring" title="BubbleMon"\\
                 longtitle="Monitoring-duck-in-a-jar dockapp" xdg="true"
EOF

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

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr (-,root,root)
%doc ChangeLog README SUPPORTED_SYSTEMS doc/Xdefaults.sample
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

