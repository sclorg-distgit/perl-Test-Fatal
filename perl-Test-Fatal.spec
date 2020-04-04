%{?scl:%scl_package perl-Test-Fatal}

%if ! (0%{?rhel}) && ! (0%{?scl:1})
# Run extra test
%bcond_without perl_Test_Fatal_enables_extra_test
# Run optional test
%bcond_without perl_Test_Fatal_enables_optional_test
%else
%bcond_with perl_Test_Fatal_enables_extra_test
%bcond_with perl_Test_Fatal_enables_optional_test
%endif

Summary:	Incredibly simple helpers for testing code with exceptions 
Name:		%{?scl_prefix}perl-Test-Fatal
Version:	0.014
Release:	16%{?dist}
License:	GPL+ or Artistic
Url:		https://metacpan.org/release/Test-Fatal
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Test-Fatal-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	%{?scl_prefix}perl-interpreter
BuildRequires:	%{?scl_prefix}perl-generators
BuildRequires:	%{?scl_prefix}perl(Config)
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(Exporter) >= 5.57
BuildRequires:	%{?scl_prefix}perl(strict)
BuildRequires:	%{?scl_prefix}perl(Test::Builder)
BuildRequires:	%{?scl_prefix}perl(Try::Tiny) >= 0.07
BuildRequires:	%{?scl_prefix}perl(warnings)
# Test Suite
BuildRequires:	%{?scl_prefix}perl(File::Spec)
BuildRequires:	%{?scl_prefix}perl(overload)
BuildRequires:	%{?scl_prefix}perl(Test::Builder::Tester)
BuildRequires:	%{?scl_prefix}perl(Test::More) >= 0.96
%if %{with perl_Test_Fatal_enables_optional_test}
# Optional Tests
BuildRequires:	%{?scl_prefix}perl(CPAN::Meta) >= 2.120900
%endif
%if %{with perl_Test_Fatal_enables_extra_test}
# Extra Tests
BuildRequires:	%{?scl_prefix}perl(Test::Pod) >= 1.41
%endif
# Runtime
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:	%{?scl_prefix}perl(Test::Builder)

%description
Test::Fatal is an alternative to the popular Test::Exception. It does much
less, but should allow greater flexibility in testing exception-throwing code
with about the same amount of typing.

%prep
%setup -q -n Test-Fatal-%{version}

# Avoid doc-file dependencies
chmod -c -x examples/*
%{?scl:scl enable %{scl} '}perl -MConfig -i -pe %{?scl:'"}'%{?scl:"'}s{^#!/usr/bin/perl}{$Config{startperl}}%{?scl:'"}'%{?scl:"'} examples/*%{?scl:'}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}
%if %{with perl_Test_Fatal_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%doc LICENSE
%doc Changes README examples/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Fatal.3*

%changelog
* Tue Mar 17 2020 Petr Pisar <ppisar@redhat.com> - 0.014-16
- Normalize shebangs in a documentation (bug #1813316)

* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-15
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.014-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.014-2
- Perl 5.22 rebuild

* Wed Dec 10 2014 Paul Howarth <paul@city-fan.org> - 0.014-1
- Update to 0.014
  - Avoid assuming that t/todo.t is always called t/todo.t
- Classify buildreqs by usage
- Use %%license

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 24 2013 Paul Howarth <paul@city-fan.org> - 0.013-1
- Update to 0.013
  - Rebuild to get a newer compile test that may work on 5.6.x

* Tue Sep 17 2013 Paul Howarth <paul@city-fan.org> - 0.012-1
- Update to 0.012
  - Go back to auto-detecting the required Test::More, reverting the changes
    made for CPAN RT#62699
- Drop support for all current EL releases (5 and 6) since we need Test::More
  version 0.96 or later for the test suite

* Tue Sep 17 2013 Paul Howarth <paul@city-fan.org> - 0.011-1
- Update to 0.011
  - More clearly (and correctly) document the way NOT to use Test::Fatal
  - Try to fix $TODO not working when the user test uses $T::B::Level
- Explicitly run the extra tests
- Package examples directory as documentation
- Don't need to remove empty directories from the buildroot
- Drop %%defattr, redundant since rpm 4.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.010-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 18 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-4
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.010-2
- Perl 5.16 rebuild

* Thu Feb 16 2012 Paul Howarth <paul@city-fan.org> - 0.010-1
- Update to 0.010
  - Avoid tickling an overloading bug in perl 5.6 during testing
    (CPAN RT#74847)

* Fri Feb 10 2012 Paul Howarth <paul@city-fan.org> - 0.009-1
- Update to 0.009
  - Advise against using isnt(exception{...},undef)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov  7 2011 Paul Howarth <paul@city-fan.org> - 0.008-1
- Update to 0.008
  - Revert the mistake by which 0.004 allowed blocks after "exception" as well
    as "success"
- BR: perl(Carp)
- Update patch for building with ExtUtils::MakeMaker < 6.30

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.006-2
- Perl mass rebuild

* Thu Jun  2 2011 Paul Howarth <paul@city-fan.org> - 0.006-1
- Update to 0.006
  - Crank back the Test::More and Exporter requirements (CPAN RT#62699)
  - Add lives_ok and dies_ok emulation (CPAN RT#67598)
- Versions patch replaced by workaround for old ExtUtils::MakeMaker
- BR: perl(Test::Builder::Tester)

* Tue Apr 26 2011 Paul Howarth <paul@city-fan.org> - 0.005-1
- Update to 0.005
  - Fix the logic that picks tests for 5.13.1+

* Tue Apr 26 2011 Paul Howarth <paul@city-fan.org> - 0.004-1
- Update to 0.004
  - success blocks now allow trailing blocks like finally, catch, etc.
- Remove remaining uses of macros for commands
- Re-order %%install section to conventional position in spec

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 29 2010 Paul Howarth <paul@city-fan.org> - 0.003-1
- Update to 0.003
  - More tests for false exceptions, especially on 5.13
- Update versions patch

* Thu Oct 28 2010 Paul Howarth <paul@city-fan.org> - 0.002-1
- Update to 0.002
  - Add tests for handling of false exceptions
  - Fix precedence error in documentation
- Update versions patch

* Wed Oct 27 2010 Paul Howarth <paul@city-fan.org> - 0.001-2
- Sanitize spec for Fedora submission

* Tue Oct 26 2010 Paul Howarth <paul@city-fan.org> - 0.001-1
- Initial RPM version
