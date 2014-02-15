Summary:	Knife plugin for Opscode Reporting
Name:		knife-reporting
Version:	0.3.2
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	b9b45c9f76de8b478b6e20a8b49edc98
URL:		http://www.opscode.com/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	chef
Requires:	knife
Requires:	ruby-mixlib-cli >= 1.2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Knife plugin for Opscode Reporting.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{ruby_vendorlibdir}/chef/knife/runs_list.rb
%{ruby_vendorlibdir}/chef/knife/runs_show.rb
%{ruby_vendorlibdir}/chef/reporting/knife_helpers.rb
