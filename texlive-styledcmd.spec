%global tl_name styledcmd
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.1
Release:	%{tl_revision}.1
Summary:	Handling multiple versions of user-defined macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/styledcmd
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/styledcmd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/styledcmd.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/styledcmd.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows creating and maintaining different versions of the
same command, in order to choose the best option for every document.
This includes expandable and protected commands.

