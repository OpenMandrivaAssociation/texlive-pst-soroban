# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-soroban
# catalog-date 2008-08-23 00:25:16 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pst-soroban
Version:	1.0
Release:	1
Summary:	Draw a Soroban using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-soroban
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-soroban.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-soroban.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-soroban.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package uses PSTricks to draw a Japanese abacus, or
soroban. The soroban is still used in Japan today.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
