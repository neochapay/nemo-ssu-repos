Name: nemo-ssu-repos
Version: 0.1.1
Release: 1
Summary: Nemo SSU repositories
URL: https://github.com/nemomobile/nemo-ssu-repos
Group: System/Base
BuildArch: noarch
License: GPLv2
Source0: %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(QtCore)

%define ssu_requirement ssu >= 0.25

%description
%{summary}.


%package -n ssu-vendor-data-nemo
Summary: Sample vendor configuration data
Group: System/Base
Requires: %{ssu_requirement}
Provides: ssu-vendor-data

%description -n ssu-vendor-data-nemo
%{summary}. A vendor (including Nemo) is supposed to put those configuration on device.

%files -n ssu-vendor-data-nemo
%defattr(-,root,root,-)
%attr(0664, root, ssu) %config(noreplace) %{_sysconfdir}/ssu/ssu.ini
%{_datadir}/ssu/*.ini


%package release
Summary: Release repositories
Group: System/Base
Requires: %{ssu_requirement}

%description release
%{summary}.

%files release
%defattr(-,root,root,-)
%config %{_sysconfdir}/zypp/repos.d/mer-core-release.repo
%config %{_sysconfdir}/zypp/repos.d/nemo-release.repo

%package adaptation-release
Summary: Adaptation repositories
Group: System/Base
Requires: %{ssu_requirement}

%description adaptation-release
This package provides device-specific adaptation for any
device where ssu can determine the correct device type,
as well as the main common adaptation repository. If your
device uses more than one common adaptation you will have
to install adaptation-extra-release, and enable the required
repositories. The repositories here are disabled per default.

%files adaptation-release
%defattr(-,root,root,-)
%config %{_sysconfdir}/zypp/repos.d/adaptation-release.repo


%package adaptation-common-release
Summary: Common adaptation repositories
Group: System/Base
Requires: %{ssu_requirement}

%description adaptation-common-release
This package provides common adaptation repositories for
devices using common adaptation repo in addition to normal
adaptation repository.

%files adaptation-common-release
%defattr(-,root,root,-)
%config %{_sysconfdir}/zypp/repos.d/adaptation-common-release.repo


%package rnd
Summary: RND repositories
Group: System/Base
Requires: %{ssu_requirement}

%description rnd
%{summary}.

%files rnd
%defattr(-,root,root,-)
%config %{_sysconfdir}/zypp/repos.d/mer-core-rnd.repo
%config %{_sysconfdir}/zypp/repos.d/nemo-rnd.repo


%package adaptation-rnd
Summary: RND adaptation repositories, device specific
Group: System/Base
Requires: %{ssu_requirement}

%description adaptation-rnd
This package provides device-specific adaptation for any
any device where ssu can determine the correct device type,
as well as the main common adaptation repository. If your
device uses more than one common adaptation you will have
to install adaptation-extra-rnd, and enable the required
repositories.

%files adaptation-rnd
%defattr(-,root,root,-)
%config %{_sysconfdir}/zypp/repos.d/adaptation-rnd.repo


%package adaptation-common-rnd
Summary: Common adaptation repositories
Group: System/Base
Requires: %{ssu_requirement}

%description adaptation-common-rnd
This package provides common adaptation repositories for
devices using common adaptation repo in addition to normal
adaptation repository.

%files adaptation-common-rnd
%defattr(-,root,root,-)
%config %{_sysconfdir}/zypp/repos.d/adaptation-common-rnd.repo


%prep
%setup -q -n %{name}-%{version}

%build
qmake DEFINES+='TARGET_ARCH=\\\"\"%{_target_cpu}\"\\\"' -recursive
make %{?_smp_mflags}


%install
make INSTALL_ROOT=%{buildroot} install
RND_REPOS="mer-core adaptation adaptation-common"; \
for REPO in $RND_REPOS; do
    sed -r 's/-rnd/-release/;s/\?rnd&?/?/;s/\?$//' %{buildroot}/%{_sysconfdir}/zypp/repos.d/$REPO-rnd.repo \
        > %{buildroot}/%{_sysconfdir}/zypp/repos.d/$REPO-release.repo
done
