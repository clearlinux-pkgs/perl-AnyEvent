#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-AnyEvent
Version  : 7.14
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-7.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-7.14.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libanyevent-perl/libanyevent-perl_7.140-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-AnyEvent-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
AnyEvent - the DBI of event loop programming
EV, Event, Glib, Tk, UV, Perl, Event::Lib, Irssi, rxvt-unicode,
IO::Async, Qt, FLTK and POE are various supported event
loops/environments.

%package dev
Summary: dev components for the perl-AnyEvent package.
Group: Development
Provides: perl-AnyEvent-devel = %{version}-%{release}

%description dev
dev components for the perl-AnyEvent package.


%package license
Summary: license components for the perl-AnyEvent package.
Group: Default

%description license
license components for the perl-AnyEvent package.


%prep
%setup -q -n AnyEvent-7.14
cd ..
%setup -q -T -D -n AnyEvent-7.14 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/AnyEvent-7.14/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-AnyEvent
cp COPYING %{buildroot}/usr/share/package-licenses/perl-AnyEvent/COPYING
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-AnyEvent/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AE.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/DNS.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Debug.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/FAQ.pod
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Handle.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/IO.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/IO/IOAIO.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/IO/Perl.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/Cocoa.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/EV.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/Event.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/EventLib.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/FLTK.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/Glib.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/IOAsync.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/Irssi.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/POE.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/Perl.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/Qt.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/Tk.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Impl/UV.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Intro.pod
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Log.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Loop.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Socket.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Strict.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/TLS.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Util.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Util/idna.pl
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/Util/uts46data.pl
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/AnyEvent/constants.pl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/AE.3
/usr/share/man/man3/AnyEvent.3
/usr/share/man/man3/AnyEvent::DNS.3
/usr/share/man/man3/AnyEvent::Debug.3
/usr/share/man/man3/AnyEvent::FAQ.3
/usr/share/man/man3/AnyEvent::Handle.3
/usr/share/man/man3/AnyEvent::IO.3
/usr/share/man/man3/AnyEvent::IO::IOAIO.3
/usr/share/man/man3/AnyEvent::IO::Perl.3
/usr/share/man/man3/AnyEvent::Impl::Cocoa.3
/usr/share/man/man3/AnyEvent::Impl::EV.3
/usr/share/man/man3/AnyEvent::Impl::Event.3
/usr/share/man/man3/AnyEvent::Impl::EventLib.3
/usr/share/man/man3/AnyEvent::Impl::FLTK.3
/usr/share/man/man3/AnyEvent::Impl::Glib.3
/usr/share/man/man3/AnyEvent::Impl::IOAsync.3
/usr/share/man/man3/AnyEvent::Impl::Irssi.3
/usr/share/man/man3/AnyEvent::Impl::POE.3
/usr/share/man/man3/AnyEvent::Impl::Perl.3
/usr/share/man/man3/AnyEvent::Impl::Qt.3
/usr/share/man/man3/AnyEvent::Impl::Tk.3
/usr/share/man/man3/AnyEvent::Impl::UV.3
/usr/share/man/man3/AnyEvent::Intro.3
/usr/share/man/man3/AnyEvent::Log.3
/usr/share/man/man3/AnyEvent::Loop.3
/usr/share/man/man3/AnyEvent::Socket.3
/usr/share/man/man3/AnyEvent::Strict.3
/usr/share/man/man3/AnyEvent::TLS.3
/usr/share/man/man3/AnyEvent::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-AnyEvent/COPYING
/usr/share/package-licenses/perl-AnyEvent/deblicense_copyright
