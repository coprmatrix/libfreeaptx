%global debug_package %{nil}
Name:           libfreeaptx
Version:        0.2.2
Release:        0
Summary:        Free implementation of Audio Processing Technology codec (aptX)
License:        LGPL-2.1-or-later
URL:            https://github.com/iamthehorker/libfreeaptx
Source:         https://github.com/iamthehorker/libfreeaptx/releases/download/%{version}/libfreeaptx-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  sed

%package tools
Summary:    An implementation of Audio Processing Technology codec (aptX)

%description tools
An Open Source implementation of Audio Processing Technology codec (aptX)
originally derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec
is mainly used in Bluetooth A2DP profile.

This package contains the encoder and decoder tool.

%description
An Open Source implementation of Audio Processing Technology codec (aptX)
originally derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec
is mainly used in Bluetooth A2DP profile.

%package devel
Summary:    An implementation of Audio Processing Technology codec (aptX)
Requires:   libfreeaptx0 = %{version}

%description devel
An Open Source implementation of Audio Processing Technology codec (aptX)
originally derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec
is mainly used in Bluetooth A2DP profile.

This package contains the development headers.

%prep
%setup -q

sed -i s/"^PREFIX =.*"/"PREFIX = \/usr"/ Makefile
sed -i s/"^LIBDIR = .*"/"LIBDIR = %{_lib}"/ Makefile

%build
%make_build CC=gcc

%install
%make_install
chmod -x README %{buildroot}%{_includedir}/freeaptx.h

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libfreeaptx.so.*

%files devel
%license COPYING
%doc README
%{_includedir}/freeaptx.h
%{_libdir}/libfreeaptx.so
%{_libdir}/pkgconfig/libfreeaptx.pc

%files tools
%{_bindir}/freeaptxdec
%{_bindir}/freeaptxenc

%changelog
* Thu Jul  8 2021 Hunter Wardlaw <wardlawhunter@gmail.com>
- Update to 0.1.1
  * Removed rpath and static libraries from makefile
  * Fixed readme typo
* Thu Jul  8 2021 Hunter Wardlaw <wardlawhunter@gmail.com>
- Initial release 0.1.0 based on libopenaptx 0.2.0
  * Changed naming from libopenaptx to libfreeaptx
