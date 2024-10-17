%define		_class		Math
%define		_subclass	Quaternion
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.7.1
Release:	16
Summary:	Classes that define Quaternions and their operations
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Math_Quaternion/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Classes that represent and manipulate quaternions. Contain definitions
for basic arithmetic functions in a static class. Quaternions are an
extension of the idea of complex numbers, and a quaternion is defined as:
q = a + b*i + c*j + d*k
In 1844 Hamilton described a system in which numbers were composed of
a real part and 3 imaginary and independent parts (i,j,k), such that:
i^2 = j^2 = k^2 = -1 and
ij = k, jk = i, ki = j and
ji = -k, kj = -i, ik = -j
The above are known as "Hamilton's rules".

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-14mdv2012.0
+ Revision: 742109
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-13
+ Revision: 679401
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-12mdv2011.0
+ Revision: 613715
- the mass rebuild of 2010.1 packages

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.1-11mdv2010.1
+ Revision: 470159
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-10mdv2010.0
+ Revision: 441345
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-9mdv2009.1
+ Revision: 322366
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-8mdv2009.0
+ Revision: 236958
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.7.1-7mdv2008.1
+ Revision: 136408
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-7mdv2007.0
+ Revision: 82171
- Import php-pear-Math_Quaternion

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-1mdk
- initial Mandriva package (PLD import)

