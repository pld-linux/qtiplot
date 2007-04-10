Summary:	Data analysis and scientific plotting
Summary(pl.UTF-8):	Analiza danych i naukowe rysowanie
Name:		qtiplot
Version:	0.8.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://soft.proindependent.com/src/%{name}-%{version}.zip
# Source0-md5:	1c99247b5069ec92c3f97b87291b20e7
Source1:	%{name}.desktop
Source2:	http://soft.proindependent.com/doc/manual-en.zip
# Source2-md5:	380d33a8381911feb53a73a067932b60
Source3:	%{name}.png
URL:		http://soft.proindependent.com/qtiplot.html
BuildRequires:	gsl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qmake
BuildRequires:	qt-devel >= 1:3.0
BuildRequires:	qwt-devel >= 4.2.0
BuildRequires:	qwtplot3d-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free, platform independent clone of Origin.

%description -l pl.UTF-8
Wolny, niezależny od platformy klon Origina.

%prep
%setup -q -a 2

%build
export QTDIR="%{_prefix}"
export INSTALL_ROOT=$RPM_BUILD_ROOT

cd %{name}

sed -i -e 's@../3rdparty/qwt/lib/libqwt.a@-lqwt@g' qtiplot.pro
sed -i -e 's@../3rdparty/qwt/include@%{_includedir}/qwt@g' qtiplot.pro
sed -i -e 's@/usr/share/doc/qtiplot/index.html@%{_docdir}/%{name}-%{version}/index.html@g' src/application.cpp

qmake -o Makefile qtiplot.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc manual-en/*.html README.html
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
