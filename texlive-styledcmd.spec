Name:		texlive-styledcmd
Version:	60430
Release:	1
Summary:	Handling multiple versions of user-defined macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/styledcmd
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/styledcmd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/styledcmd.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/styledcmd.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows creating and maintaining different versions
of the same command, in order to choose the best option for
every document.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/styledcmd
%{_texmfdistdir}/tex/latex/styledcmd
%doc %{_texmfdistdir}/doc/latex/styledcmd

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
