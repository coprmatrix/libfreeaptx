#
# spec file for package libfreeaptx
#
# Copyright (c) 2021 Hunter Wardlaw <wardlawhunter@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           libfreeaptx
Version:        0.1.1
Release:        10.3
Summary:        Free implementation of Audio Processing Technology codec (aptX)
License:        LGPL-2.1-or-later
URL:            https://github.com/iamthehorker/libfreeaptx
Source:         https://github.com/iamthehorker/libfreeaptx/releases/download/%{version}/libfreeaptx-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  sed

%description
An Open Source implementation of Audio Processing Technology codec (aptX)
originally derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec
is mainly used in Bluetooth A2DP profile.

%package tools
Summary:    An implementation of Audio Processing Technology codec (aptX)

%description tools
An Open Source implementation of Audio Processing Technology codec (aptX)
originally derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec
is mainly used in Bluetooth A2DP profile.

This package contains the encoder and decoder tool.

%package -n libfreeaptx0
Summary:    An implementation of Audio Processing Technology codec (aptX)

%description -n libfreeaptx0
An Open Source implementation of Audio Processing Technology codec (aptX)
originally derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This codec
is mainly used in Bluetooth A2DP profile.

This package contains the shared library

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

%post -n libfreeaptx0 -p /sbin/ldconfig
%postun -n libfreeaptx0 -p /sbin/ldconfig

%files -n libfreeaptx0
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
