#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
# Source0 file verified with key 0x933AD21886F69FBF (alexander_naumov@opensuse.org)
#
Name     : screen
Version  : 4.9.0
Release  : 30
URL      : https://mirrors.kernel.org/gnu/screen/screen-4.9.0.tar.gz
Source0  : https://mirrors.kernel.org/gnu/screen/screen-4.9.0.tar.gz
Source1  : https://mirrors.kernel.org/gnu/screen/screen-4.9.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: screen-bin = %{version}-%{release}
Requires: screen-data = %{version}-%{release}
Requires: screen-license = %{version}-%{release}
Requires: screen-man = %{version}-%{release}
BuildRequires : ncurses-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[If you just got the screen package, it pays to read the file INSTALL]
[This intro only describes the most common features to get you started]
[A full description of all features is contained in the source package]

%package bin
Summary: bin components for the screen package.
Group: Binaries
Requires: screen-data = %{version}-%{release}
Requires: screen-license = %{version}-%{release}

%description bin
bin components for the screen package.


%package data
Summary: data components for the screen package.
Group: Data

%description data
data components for the screen package.


%package license
Summary: license components for the screen package.
Group: Default

%description license
license components for the screen package.


%package man
Summary: man components for the screen package.
Group: Default

%description man
man components for the screen package.


%prep
%setup -q -n screen-4.9.0
cd %{_builddir}/screen-4.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689811338
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1689811338
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/screen
cp %{_builddir}/screen-%{version}/COPYING %{buildroot}/usr/share/package-licenses/screen/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/screen
/usr/bin/screen-4.9.0

%files data
%defattr(-,root,root,-)
/usr/share/screen/utf8encodings/01
/usr/share/screen/utf8encodings/02
/usr/share/screen/utf8encodings/03
/usr/share/screen/utf8encodings/04
/usr/share/screen/utf8encodings/18
/usr/share/screen/utf8encodings/19
/usr/share/screen/utf8encodings/a1
/usr/share/screen/utf8encodings/bf
/usr/share/screen/utf8encodings/c2
/usr/share/screen/utf8encodings/c3
/usr/share/screen/utf8encodings/c4
/usr/share/screen/utf8encodings/c6
/usr/share/screen/utf8encodings/c7
/usr/share/screen/utf8encodings/c8
/usr/share/screen/utf8encodings/cc
/usr/share/screen/utf8encodings/cd
/usr/share/screen/utf8encodings/d6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/screen/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/screen.1
