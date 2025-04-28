Name: obs-tools-mockbuild
Version: 2
Release: 0
Summary: obs tools mockbuild
License: LGPL
URL: https://example.com
Requires: obs-tools-pkg-checkaval
Requires: obs-tools-pkg
Requires: obs-tools
Requires: pam
Requires: rpm-build
Requires: sudo
Requires: bash
BuildArch: noarch
Source0:  obs_mockbuild

%description
used to leverage mockbuild sudo

%install
mkdir -pv %{buildroot}%{_sysconfdir}/sudoers.d/
mkdir -pv %{buildroot}%{_bindir}/

cat << EOF > %{buildroot}%{_sysconfdir}/sudoers.d/mockbuild
mockbuild ALL=(ALL) NOPASSWD: ALL
EOF

cp %{SOURCE0} %{buildroot}%{_bindir}/obs_mockbuild

%files
%attr(644, root, root) %{_sysconfdir}/sudoers.d/mockbuild
%attr(755, root, root) %{_bindir}/obs_mockbuild
