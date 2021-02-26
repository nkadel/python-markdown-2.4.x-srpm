%global srcname Markdown
%global pkgname markdown

Name:           python-%{pkgname}
Version:        2.4.1
#Release:        4%{?dist}
Release:        0%{?dist}
Summary:        Markdown implementation in Python
Group:          Development/Languages
License:        BSD
URL:            https://python-%{pkgname}.github.io/
Source0:        https://pypi.python.org/packages/source/M/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description
This is a Python implementation of Markdown by John Gruber. It is
almost completely compliant with the reference implementation, though
there are a few known issues.


%package -n python2-%{pkgname}
Summary:        Markdown implementation in Python
Group:          Development/Languages
BuildRequires:  python2-devel
BuildRequires:  python2-nose
Requires:       python2
%{?python_provide:%python_provide python2-%{pkgname}}

%description -n python2-%{pkgname}
This is a Python implementation of Markdown by John Gruber. It is
almost completely compliant with the reference implementation, though
there are a few known issues.


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        Markdown implementation in Python
Group:          Development/Languages
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose
Requires:       python%{python3_pkgversion}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}

%description -n python%{python3_pkgversion}-%{pkgname}
This is a Python implementation of Markdown by John Gruber. It is
almost completely compliant with the reference implementation, though
there are a few known issues.

%prep
%setup -q -n %{srcname}-%{version}

# remove shebangs
find %{pkgname} -type f -name '*.py' \
  -exec sed -i -e '/^#!/{1D}' {} \;

# fix line-ending
find bin docs -type f \
  -exec sed -i 's/\r//' {} \;


%build
%py2_build

%py3_build

%install
%py2_install

# rename binary
mv %{buildroot}%{_bindir}/%{pkgname}_py{,-%{python_version}}

%py3_install

# rename binary
mv %{buildroot}%{_bindir}/%{pkgname}_py{,-%{python3_version}}

# 2.X binary is called by default for now
ln -s %{pkgname}_py-%{python_version} %{buildroot}%{_bindir}/markdown_py

%check
%{__python2} run-tests.py -v

%{__python3} run-tests.py -v || :

%files -n python2-%{pkgname}
%license LICENSE.md
%doc build/docs/*
%{python_sitelib}/*
%{_bindir}/%{pkgname}_py
%{_bindir}/%{pkgname}_py-%{python_version}

%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE.md
%doc build/docs/*
%{python3_sitelib}/*
%{_bindir}/%{pkgname}_py-%{python3_version}

%changelog
* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 2.4.1-4
- Rebuilt to change main python from 3.4 to 3.6

* Sat Nov 24 2018 Orion Poplawski <orion@nwra.com> - 2.4.1-3
- Ship python2-markdown and python3_other-markdown
- Modernize spec

* Wed Aug 30 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.4.1-2
- Enable python3 subpackage on EPEL7.

* Wed Jun  4 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.4.1-1
- Update to 2.4.1.

* Tue Apr 15 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.4-1
- Update to 2.4.
- Spec file cleanups.

* Thu Jan 09 2014 Dennis Gilmore <dennis@ausil.us> - 2.2.1-3
- no python3 in RHEL 7

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.1-1
- Update to 2.2.1.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 2.2.0-3
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.0-1
- Update to 2.2.0.
- Update url.
- Add patch from upstream git for failing test.

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.1-1
- Update to 2.1.1.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.0-1
- Update to 2.1.0.
- Fix rhel conditional.
- Binary has been renamed.
- Build python3 subpackage.
- Include documentation in HTML instead of Markdown format.
- Run tests.

* Wed Sep 07 2011 Jesse Keating <jkeating@redhat.com> - 2.0.3-4
- Set a version in the rhel macro

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Oct  8 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.3-1
- Update to 2.0.3.

* Thu Aug 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.1-3
- Add requirement on python-elementtree, which was a separate package
  before Python 2.5.
- Re-add changelog entries accidentally removed earlier.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.1-1
- Update to 2.0.1.
- Upstream stripped .py of the cmdline script.

* Sat Apr 25 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.0-1
- Update to 2.0.
- Adjusted source URL.
- License changed to BSD only.
- Upstream now provides a script to run markdown from the cmdline.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.7-2
- Rebuild for Python 2.6

* Mon Aug  4 2008 Thomas Moschny <thomas.moschny@gmx.de> - 1.7-1
- New package.
