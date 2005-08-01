# TODO: optflags
Summary:	Data analysis and scientific plotting
Summary(pl):	Analiza danych i naukowe rysowanie
Name:		qtiplot
Version:	0.6.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://soft.proindependent.com/src/%{name}-%{version}.tar.bz2
# Source0-md5:	a8bffbcc776db061a066ed4dbab60b1e
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

cd %{name}-%{version}

sed -i -e 's@-L../3rdparty/qwt/lib@@g' qtiplot-%{version}.pro
sed -i -e 's@../3rdparty/qwt/include@%{_includedir}/qwt@g' qtiplot-%{version}.pro
sed -i -e 's@/home/ion/qt/qwtplot3d/include@%{_includedir}/qwtplot3d@g' qtiplot-%{version}.pro
sed -i -e 's@ debug@@g' qtiplot-%{version}.pro
sed -i -e 's@/usr/share/doc/qtiplot/help.html@%{_docdir}/%{name}-%{version}/help.html@g' src/application.cpp

qmake -o Makefile qtiplot-%{version}.pro

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
%doc %{name}-%{version}/doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
