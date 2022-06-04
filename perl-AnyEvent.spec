#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-AnyEvent
Version  : 7.17
Release  : 33
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-7.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/AnyEvent-7.17.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-AnyEvent-license = %{version}-%{release}
Requires: perl-AnyEvent-perl = %{version}-%{release}
Requires: perl(AnyEvent::AIO)
Requires: perl(IO::AIO)
Requires: perl(Net::SSLeay)
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
Requires: perl-AnyEvent = %{version}-%{release}

%description dev
dev components for the perl-AnyEvent package.


%package license
Summary: license components for the perl-AnyEvent package.
Group: Default

%description license
license components for the perl-AnyEvent package.


%package perl
Summary: perl components for the perl-AnyEvent package.
Group: Default
Requires: perl-AnyEvent = %{version}-%{release}

%description perl
perl components for the perl-AnyEvent package.


%prep
%setup -q -n AnyEvent-7.17
cd %{_builddir}/AnyEvent-7.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
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
cp %{_builddir}/AnyEvent-7.17/COPYING %{buildroot}/usr/share/package-licenses/perl-AnyEvent/9a56f3b919dfc8fced3803e165a2e38de62646e5
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
## Remove excluded files
rm -f %{buildroot}*/usr/lib/perl5/vendor_perl/*/x86_64-linux-thread-multi/AnyEvent/Impl/Cocoa.pm
rm -f %{buildroot}*/usr/share/man/man3/AnyEvent::Impl::Cocoa.3
rm -f %{buildroot}*/usr/lib/perl5/vendor_perl/*/x86_64-linux-thread-multi/AnyEvent/Impl/FLTK.pm
rm -f %{buildroot}*/usr/share/man/man3/AnyEvent::Impl::FLTK.3
rm -f %{buildroot}*/usr/lib/perl5/vendor_perl/*/x86_64-linux-thread-multi/AnyEvent/Impl/Qt.pm
rm -f %{buildroot}*/usr/share/man/man3/AnyEvent::Impl::Qt.3
rm -f %{buildroot}*/usr/lib/perl5/vendor_perl/*/x86_64-linux-thread-multi/AnyEvent/Impl/UV.pm
rm -f %{buildroot}*/usr/share/man/man3/AnyEvent::Impl::UV.3

%files
%defattr(-,root,root,-)

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
/usr/share/man/man3/AnyEvent::Impl::EV.3
/usr/share/man/man3/AnyEvent::Impl::Event.3
/usr/share/man/man3/AnyEvent::Impl::EventLib.3
/usr/share/man/man3/AnyEvent::Impl::Glib.3
/usr/share/man/man3/AnyEvent::Impl::IOAsync.3
/usr/share/man/man3/AnyEvent::Impl::Irssi.3
/usr/share/man/man3/AnyEvent::Impl::POE.3
/usr/share/man/man3/AnyEvent::Impl::Perl.3
/usr/share/man/man3/AnyEvent::Impl::Tk.3
/usr/share/man/man3/AnyEvent::Intro.3
/usr/share/man/man3/AnyEvent::Log.3
/usr/share/man/man3/AnyEvent::Loop.3
/usr/share/man/man3/AnyEvent::Socket.3
/usr/share/man/man3/AnyEvent::Strict.3
/usr/share/man/man3/AnyEvent::TLS.3
/usr/share/man/man3/AnyEvent::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-AnyEvent/9a56f3b919dfc8fced3803e165a2e38de62646e5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
