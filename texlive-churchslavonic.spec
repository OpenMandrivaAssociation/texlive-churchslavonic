%global tl_name churchslavonic
%global tl_revision 67474

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.4
Release:	%{tl_revision}.1
Summary:	Typeset documents in Church Slavonic language using Unicode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/churchslavonic
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/churchslavonic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/churchslavonic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(etoolbox)
Requires:	texlive(fonts-churchslavonic)
Requires:	texlive(hyphen-churchslavonic)
Requires:	texlive(oberdiek)
Requires:	texlive(xcolor)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides fonts, hyphenation patterns, and supporting macros
to typeset Church Slavonic texts. It depends on the following other
packages: fonts-churchslavonic, hyph-utf8, intcalc, etoolbox, and
xcolor.

