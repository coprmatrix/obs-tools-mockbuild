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
BuildRequires: coreutils
Requires: bash
BuildArch: noarch

%description
used to leverage mockbuild sudo

%install
mkdir -pv %{buildroot}%{_sysconfdir}/sudoers.d/
mkdir -pv %{buildroot}%{_bindir}/

cat << EOF > %{buildroot}%{_sysconfdir}/sudoers.d/mockbuild
mockbuild ALL=(ALL) NOPASSWD: ALL
EOF

cat << 'EOF' > %{buildroot}%{_bindir}/obs_mockbuild
#!/bin/bash -x
pushd "${1:-.}"

ITERATIONS="${ITERATIONS:-25}"
ITERATIONS="${ITERATIONS:-$2}"

TIMEOUT="${TIMEOUT:-250}"
TIMEOUT="${TIMEOUT:-$3}"

sudo bash -x -c "pkg_check_available ${ITERATIONS} ${TIMEOUT} "'`obs_service_list` ; obs_pkg_install'
obs_service_run

typeset -a variables=()
while IFS= read -r line; do
    variables+=("$line")
done <<< `rpmspec --query --buildrequires .osc.temp/_output_dir/*.spec)`

pkg_check_available "${ITERATIONS}" "${TIMEOUT}" "${variables[@]}"

popd
EOF


%files
%attr(644, root, root) %{_sysconfdir}/sudoers.d/mockbuild
%attr(755, root, root) %{_bindir}/obs_mockbuild
