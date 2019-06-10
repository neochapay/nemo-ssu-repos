Name: nemo-ssu-repos
Version: 0.1.1
Release: 1
Summary: Nemo SSU repositories
URL: https://github.com/nemomobile/nemo-ssu-repos
Group: System/Base
BuildArch: noarch
License: GPLv2
Source0: %{name}-%{version}.tar.gz

%description
%{summary}.

%package -n ssu-vendor-data-nemo
Summary: Sample vendor configuration data
Group: System/Base
Requires: ssu >= 0.31
Requires: oneshot

Provides: ssu-vendor-data

Obsoletes: nemo-ssu-repos-release
Obsoletes: nemo-ssu-repos-mer-tools-release
Obsoletes: nemo-ssu-repos-adaptation-release
Obsoletes: nemo-ssu-repos-adaptation-common-release
Obsoletes: nemo-ssu-repos-rnd
Obsoletes: nemo-ssu-repos-mer-tools-rnd
Obsoletes: nemo-ssu-repos-adaptation-rnd
Obsoletes: nemo-ssu-repos-adaptation-common-rnd

%description -n ssu-vendor-data-nemo
%{summary}. A vendor (including Nemo) is supposed to put those configuration on device.

%files -n ssu-vendor-data-nemo
%defattr(-,root,root,-)
%attr(0664, root, ssu) %config(noreplace) %{_sysconfdir}/ssu/ssu.ini
%{_datadir}/ssu/*.ini

%post -n ssu-vendor-data-nemo
%{_bindir}/add-oneshot --now ssu-update-repos

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p $RPM_BUILD_ROOT

%install
install -D -m 644 ssu/ssu.ini $RPM_BUILD_ROOT%{_sysconfdir}/ssu/ssu.ini
install -D -m 644 ssu/repos.ini $RPM_BUILD_ROOT%{_datadir}/ssu/repos.ini
install -D -m 644 ssu/ssu-defaults.ini $RPM_BUILD_ROOT%{_datadir}/ssu/ssu-defaults.ini
install -D -m 644 ssu/board-mappings.ini $RPM_BUILD_ROOT%{_datadir}/ssu/board-mappings.ini

