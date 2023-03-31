Name:		texlive-churchslavonic
Version:	42751
Release:	2
Summary:	Typeset documents in Church Slavonic language using Unicode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/churchslavonic
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/churchslavonic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/churchslavonic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides fonts, hyphenation patterns, and
supporting macros to typeset Church Slavonic texts. It depends
on the following other packages: fonts-churchslavonic,
hyph-utf8, intcalc, etoolbox, and xcolor.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/churchslavonic
%doc %{_texmfdistdir}/doc/latex/churchslavonic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
