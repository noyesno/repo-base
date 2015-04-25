%define ...

Name:
Version:
Release:
Copyright: ...
Srouce: ...
URL:
Requires:
BuildPrereq: ...
Prereq: tcl

%description

%prep

%build
cd src/unix
/usr/bin/autoconf
./configure
make

%install
cd src/unix
make install

%clean
cd src/unix
make clean

%files
%doc doc
/usr/bin/

%changelog
