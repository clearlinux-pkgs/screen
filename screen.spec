#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : screen
Version  : 4.4.0
Release  : 14
URL      : http://mirrors.kernel.org/gnu/screen/screen-4.4.0.tar.gz
Source0  : http://mirrors.kernel.org/gnu/screen/screen-4.4.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: screen-bin
Requires: screen-doc
Requires: screen-data
BuildRequires : ncurses-dev

%description
[If you just got the screen package, it pays to read the file INSTALL]
[This intro only describes the most common features to get you started]
[A full description of all features is contained in the source package]

%package bin
Summary: bin components for the screen package.
Group: Binaries
Requires: screen-data

%description bin
bin components for the screen package.


%package data
Summary: data components for the screen package.
Group: Data

%description data
data components for the screen package.


%package doc
Summary: doc components for the screen package.
Group: Documentation

%description doc
doc components for the screen package.


%prep
%setup -q -n screen-4.4.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/screen
/usr/bin/screen-4.4.0

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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
