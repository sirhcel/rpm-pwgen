%global VERSION 2.07

Name:           pwgen
Summary:        Password Generator (pwgen)
# The most appropriate RPM group has been chosen from
# /usr/share/doc/rpm-4.9.1.2/GROUPS from the phone and PackageKit maps this
# group to its own scheme.
Group:          Applications/System
License:        GPLv2

Version:        %{VERSION}
Release:        1

Url:            http://pwgen.sourceforge.net/
Source0:        http://sourceforge.net/projects/pwgen/files/pwgen/%{VERSION}/pwgen-%{VERSION}.tar.gz
# TODO: What about applying the fdleak patch from
# http://download.opensuse.org/ports/aarch64/source/factory/repo/oss/suse/src/pwgen-2.07-1.1.src.rpm?
# It seems to originate from
# https://bugzilla.novell.com/show_bug.cgi?id=529521.


%description
Pwgen is a small, GPL'ed password generator which creates passwords which can
be easily memorized by a human.


%prep
%setup


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/pwgen
# Do not package any documentation beyond the manpage because I expect it not
# to be read on a mobile device.
%doc %{_mandir}/man1/pwgen.1*


%changelog
* Mon Apr 06 2015 Christian Meusel <lechris@posteo.de>
- Initial packaging.
