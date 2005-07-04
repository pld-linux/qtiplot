# TODO: optflags
Summary:	Data analysis and scientific plotting
Summary(pl):	Analiza danych i naukowe rysowanie
Name:		qtiplot
Version:	0.6.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://soft.proindependent.com/%{name}-%{version}.tar.bz2
# Source0-md5:	0748bb9b58149fd87402cbb7ad254e60
Source1:	%{name}.desktop
URL:		http://soft.proindependent.com/qtiplot.html
BuildRequires:	gsl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.0
BuildRequires:	qwt-devel
BuildRequires:	qwtplot3d-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free, platform independent clone of Origin.

%description -l pl
Wolny, niezale¿ny od platformy klon Origina.

%prep
%setup -q

%build
export QTDIR="%{_prefix}"
export INSTALL_ROOT=$RPM_BUILD_ROOT

sed -i -e 's@debug@@g' qtiplot.pro
sed -i -e 's@/home/ion/qt/qwt/include@%{_includedir}/qwt@g' qtiplot.pro
sed -i -e 's@/home/ion/qt/qwtplot3d/include@%{_includedir}/qwtplot3d@g' qtiplot.pro
sed -i -e 's@%{_datadir}/doc/qtiplot/help.html@%{_docdir}/%{name}-%{version}/help.html@g' src/application.cpp

qmake -o Makefile qtiplot.pro

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
