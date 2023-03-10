%global gorepo rapid7-insight-agent

%global _dwz_low_mem_die_limit 0

Name: %{_cross_os}%{gorepo}
Release: 1%{?dist}
Summary: Rapid7 Insight Agent
License: Apache-2.0
Source1000: clarify.toml

BuildRequires: git
BuildRequires: %{_cross_os}glibc-devel

%description
%{summary}.

%build
./agent_installer.sh



%files
%license LICENSE
%{_cross_attribution_file}
%{_cross_attribution_vendor_dir}

%changelog
