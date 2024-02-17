%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 70 -o "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)

%define oldlibname %mklibname KF6KExiv2
%define olddevname %mklibname KF6KExiv2 -d
%define libname %mklibname KExiv2Qt6
%define devname %mklibname KExiv2Qt6 -d
#define git 20231103

Name: kf6-libkexiv2
Version: 24.01.90
Release: %{?git:0.%{git}.}2
%if 0%{?git:1}
Source0: https://invent.kde.org/graphics/libkexiv2/-/archive/master/libkexiv2-master.tar.bz2#/libkexiv2-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/libkexiv2-%{version}.tar.xz
%endif
Summary: Library for handling exiv2 metadata
URL: https://invent.kde.org/graphics/libkexiv2
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: pkgconfig(exiv2)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6ConfigWidgets)
# Just to prevent pulling in KF5
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%description
Library for handling exiv2 metadata

%package -n %{libname}
Summary: Library for handling exiv2 metadata
Group: System/Libraries
Requires: %{name} = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
Library for handling exiv2 metadata

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Library for handling exiv2 metadata

%prep
%autosetup -p1 -n libkexiv2-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/libkexiv2.*

%files -n %{devname}
%{_includedir}/KExiv2Qt6
%{_libdir}/cmake/KExiv2Qt6

%files -n %{libname}
%{_libdir}/libKExiv2Qt6.so*
