#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v26
# autospec commit: 99a7985
#
Name     : screen
Version  : 5.0.1
Release  : 38
URL      : https://mirrors.kernel.org/gnu/screen/screen-5.0.1.tar.gz
Source0  : https://mirrors.kernel.org/gnu/screen/screen-5.0.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: screen-bin = %{version}-%{release}
Requires: screen-data = %{version}-%{release}
Requires: screen-info = %{version}-%{release}
Requires: screen-license = %{version}-%{release}
Requires: screen-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-configure
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


%package info
Summary: info components for the screen package.
Group: Default

%description info
info components for the screen package.


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
%setup -q -n screen-5.0.1
cd %{_builddir}/screen-5.0.1
pushd ..
cp -a screen-5.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747319266
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1747319266
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/screen
cp %{_builddir}/screen-%{version}/COPYING %{buildroot}/usr/share/package-licenses/screen/0dd432edfab90223f22e49c02e2124f87d6f0a56 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/screen-5.0.1
/usr/bin/screen
/usr/bin/screen-5.0.1

%files data
%defattr(-,root,root,-)
/usr/share/screen/utf8encodings/01
/usr/share/screen/utf8encodings/02
/usr/share/screen/utf8encodings/03
/usr/share/screen/utf8encodings/04
/usr/share/screen/utf8encodings/18
/usr/share/screen/utf8encodings/19
/usr/share/screen/utf8encodings/a1
/usr/share/screen/utf8encodings/a3
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

%files info
%defattr(0644,root,root,0755)
/usr/share/info/screen.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/screen/0dd432edfab90223f22e49c02e2124f87d6f0a56

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/screen.1
