#
# Conditional build:
%bcond_without	SDL_mixer	# build without SDL_mixer
#
Summary:	Addictive puzzle game to kill time
Summary(pl):	Uzale¿niaj±ca gra logiczna, która pomaga zabiæ czas
Name:		scalar
Version:	1.02
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scalar/%{name}-%{version}-src.tar.bz2
# Source0-md5:	85526f8abf84ed4f5fa4cda67c75b47d
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-images_dir.patch
URL:		http://scalar.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
%{?with_SDL_mixer:BuildRequires:        SDL_mixer-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of the game is to assemble the picture from pieces. Each
picture is divided into pieces which are shuffled. You need to get
each piece back to its original position.

%description -l pl
Celem gry jest u³o¿enie obrazka z kawa³ków. Ka¿dy obrazek zosta³
podzielony na kawa³ki, które zosta³y pomieszane. Twoim zadaniem jest
przywrócenie oryginalnego wygl±du obrazka.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
sed -i 's@data@%{_datadir}/%{name}/data@' %{name}.cpp

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -r data/ $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r images/ $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
