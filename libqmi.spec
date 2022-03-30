Name:          libqmi
Version:       1.30.4
Release:       1
License:       LGPLv2+ and GPLv2+
Summary:       A glib-based library to use the Qualcomm MSM Interface (QMI) protocol
URL:           http://freedesktop.org/software/libqmi
Source0:       http://freedesktop.org/software/libqmi/libqmi-%{version}.tar.xz

BuildRequires: glib2-devel >= 2.32.0 libgudev-devel >= 147 libmbim-devel >= 1.18.0 python3 gtk-doc gcc
Provides:      libqmi-utils = %{version}-%{release}
Obsoletes:     libqmi-utils < 1.20.0.4

%description
Libqmi is a glib-based library for talking to WWAN modems and devices which
speak the Qualcomm MSM Interface (QMI) protocol.

%package       devel
Summary:       Libraries and header files for libqmi development
Requires:      libqmi = %{version}-%{release} glib2-devel pkgconfig

%description   devel
This package contains the header and pkg-config files for development
applications using QMI functionality from applications that use glib.

%package_help

%prep
%autosetup -p1

%build
%configure --disable-static --enable-gtk-doc --enable-mbim-qmux
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g'         libtool

LD_LIBRARY_PATH="$PWD/src/libqmi-glib/.libs" %make_build V=1

%install
%make_install
find %{buildroot}%{_datadir}/gtk-doc | xargs touch --reference configure.ac

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%license COPYING
%{_bindir}/qmi*
%{_libdir}/libqmi-glib.so.*
%{_datadir}/bash-completion
%{_libexecdir}/qmi-proxy

%files devel
%dir %{_includedir}/libqmi-glib
%dir %{_datadir}/gtk-doc/html/libqmi-glib
%{_includedir}/libqmi-glib/*.h
%{_libdir}/pkgconfig/qmi-glib.pc
%{_libdir}/libqmi-glib.so
%{_datadir}/gtk-doc/html/libqmi-glib/*
%exclude %{_libdir}/libqmi-glib.la

%files help
%doc NEWS AUTHORS README
%{_mandir}/man1/*

%changelog
* Wed Mar 30 2022 YukariChiba <i@0x7f.cc> - 1.30.4-1
- Upgrade version to 1.30.4

* Mon Jun 28 2021 liuyumeng <liuyumeng5@huawei.com> - 1.26.2-3
- update libmbim-devel version from 1.14.0 to 1.18.0

* Tue Jun 08 2021 wulei <wulei80@huawei.com> - 1.26.2-2
- fixes failed: error: no acceptable C compiler found in $PATH

* Tue Jul 28 2020 cuibaobao <cuibaobao1@huawei.com> - 1.26.2-1
- update to 1.26.2

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.20.0-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add patch to modify build err

* Fri Nov 29 2019 Lijin Yang <yanglijin@huawei.com> - 1.20.0-4
- init package


