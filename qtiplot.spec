Summary:	Data analysis and scientific plotting
Summary(pl):	Analiza danych i naukowe rysowanie
Name:		qtiplot
Version:	0.7.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://soft.proindependent.com/src/%{name}-%{version}.zip
# Source0-md5:	3b519a88eb6b1c90b5bbe9b4a1d7b3ea
Source1:	%{name}.desktop
Source2:	http://soft.proindependent.com/doc/manual-en.zip
# Source2-md5:	380d33a8381911feb53a73a067932b60
URL:		http://soft.proindependent.com/qtiplot.html
BuildRequires:	gsl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.0
BuildRequires:	qwt-devel >= 4.2.0
BuildRequires:	qwtplot3d-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free, platform independent clone of Origin.

%description -l pl
Wolny, niezale¿ny od platformy klon Origina.

%prep
%setup -q -a 2

%build
export QTDIR="%{_prefix}"
export INSTALL_ROOT=$RPM_BUILD_ROOT

cd %{name}-%{version}

sed -i -e 's@-L../3rdparty/qwt/lib@@g' qtiplot-%{version}.pro
sed -i -e 's@../3rdparty/qwt/include@%{_includedir}/qwt@g' qtiplot-%{version}.pro
sed -i -e 's@\$\${QTIPLOT_PATH}/qt/qwtplot3d/include@%{_includedir}/qwtplot3d@g' qtiplot-%{version}.pro
sed -i -e 's@ debug@@g' qtiplot-%{version}.pro
sed -i -e 's@/usr/share/doc/qtiplot/index.html@%{_docdir}/%{name}-%{version}/index.html@g' src/application.cpp

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
%doc manual-en/*.html README.html
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
