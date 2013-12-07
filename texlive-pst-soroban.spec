# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-soroban
# catalog-date 2008-08-23 00:25:16 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pst-soroban
Version:	1.0
Release:	4
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755479
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719397
- texlive-pst-soroban
- texlive-pst-soroban
- texlive-pst-soroban
- texlive-pst-soroban

