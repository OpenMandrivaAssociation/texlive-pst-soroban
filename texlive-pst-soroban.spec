Name:		texlive-pst-soroban
Version:	15878
Release:	1
Summary:	Draw a Soroban using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-soroban
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-soroban.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-soroban.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-soroban.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses PSTricks to draw a Japanese abacus, or
soroban. The soroban is still used in Japan today.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-soroban/pst-soroban.sty
%doc %{_texmfdistdir}/doc/generic/pst-soroban/Changes
%doc %{_texmfdistdir}/doc/generic/pst-soroban/README
%doc %{_texmfdistdir}/doc/generic/pst-soroban/pst-soroban-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-soroban/pst-soroban-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-soroban/pst-soroban-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-soroban/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
