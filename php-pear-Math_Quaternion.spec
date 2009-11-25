%define		_class		Math
%define		_subclass	Quaternion
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.7.1
Release:	%mkrel 11
Summary:	Classes that define Quaternions and their operations
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Math_Quaternion/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
