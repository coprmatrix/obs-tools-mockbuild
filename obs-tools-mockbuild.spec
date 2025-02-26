Name: obs-tools-mockbuild
Version: 0
Release: 0
Summary: obs tools mockbuild
License: LGPL
URL: https://example.com
Requires: obs-tools-pkg
Requires: obs-tools
Requires: pam
Requires: sudo
Requires: bash

%description
used to leverage mockbuild sudo

%install
mkdir -pv %{buildroot}%{_sysconfdir}/sudoers.d/
mkdir -pv %{buildroot}%{_bindir}/

cat << EOF > %{buildroot}%{_sysconfdir}/sudoers.d/mockbuild
mockbuild ALL=(ALL) NOPASSWD: ALL
EOF

cat << EOF > %{buildroot}%{_bindir}/obs_mockbuild
#!/bin/bash
pushd "${1:-.}"
sudo obs_pkg_install
obs_service_run
popd
EOF


%files
%attr(644, root, root) %{_sysconfdir}/sudoers.d/mockbuild
%attr(755, root, root) %{_bindir}/obs_mockbuild
