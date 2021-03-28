%bcond_with check
%global debug_package %{nil}

%global crate value-bag

Name:           rust-%{crate}
Version:        1.0.0~alpha.6
Release:        1%{?dist}
Summary:        Anonymous structured values

# Upstream license specification: Apache-2.0 OR MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/value-bag
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(ctor/default) >= 0.1.0 with crate(ctor/default) < 0.2.0)
%if %{with check}
BuildRequires:  (crate(serde_json/default) >= 1.0.0 with crate(serde_json/default) < 2.0.0)
BuildRequires:  (crate(serde_test/default) >= 1.0.0 with crate(serde_test/default) < 2.0.0)
BuildRequires:  (crate(sval/default) >= 1.0.0~alpha.5 with crate(sval/default) < 2.0.0)
BuildRequires:  (crate(sval/test) >= 1.0.0~alpha.5 with crate(sval/test) < 2.0.0)
BuildRequires:  (crate(sval_json/default) >= 1.0.0~alpha.5 with crate(sval_json/default) < 2.0.0)
BuildRequires:  (crate(sval_json/std) >= 1.0.0~alpha.5 with crate(sval_json/std) < 2.0.0)
BuildRequires:  (crate(wasm-bindgen-test/default) >= 0.3.0 with crate(wasm-bindgen-test/default) < 0.4.0)
BuildRequires:  (crate(wasm-bindgen/default) >= 0.2.0 with crate(wasm-bindgen/default) < 0.3.0)
%endif
%endif

%global _description %{expand:
Anonymous structured values.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag) = 1.0.0~alpha.6
Requires:       cargo
Requires:       (crate(ctor/default) >= 0.1.0 with crate(ctor/default) < 0.2.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/default) = 1.0.0~alpha.6
Requires:       cargo
Requires:       crate(value-bag) = 1.0.0~alpha.6

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+erased-serde1-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/erased-serde1) = 1.0.0~alpha.6
Requires:       cargo
Requires:       (crate(erased-serde) >= 0.3.0 with crate(erased-serde) < 0.4.0)
Requires:       crate(value-bag) = 1.0.0~alpha.6

%description -n %{name}+erased-serde1-devel %{_description}

This package contains library source intended for building other packages
which use "erased-serde1" feature of "%{crate}" crate.

%files       -n %{name}+erased-serde1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+error-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/error) = 1.0.0~alpha.6
Requires:       cargo
Requires:       (crate(sval/std) >= 1.0.0~alpha.5 with crate(sval/std) < 2.0.0)
Requires:       crate(value-bag) = 1.0.0~alpha.6
Requires:       crate(value-bag/std) = 1.0.0~alpha.6

%description -n %{name}+error-devel %{_description}

This package contains library source intended for building other packages
which use "error" feature of "%{crate}" crate.

%files       -n %{name}+error-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/serde) = 1.0.0~alpha.6
Requires:       cargo
Requires:       crate(value-bag) = 1.0.0~alpha.6
Requires:       crate(value-bag/serde1) = 1.0.0~alpha.6

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde1-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/serde1) = 1.0.0~alpha.6
Requires:       cargo
Requires:       (crate(erased-serde/alloc) >= 0.3.0 with crate(erased-serde/alloc) < 0.4.0)
Requires:       (crate(sval/alloc) >= 1.0.0~alpha.5 with crate(sval/alloc) < 2.0.0)
Requires:       (crate(sval/serde1) >= 1.0.0~alpha.5 with crate(sval/serde1) < 2.0.0)
Requires:       crate(value-bag) = 1.0.0~alpha.6
Requires:       crate(value-bag/serde1_fmt) = 1.0.0~alpha.6
Requires:       crate(value-bag/serde1_lib) = 1.0.0~alpha.6

%description -n %{name}+serde1-devel %{_description}

This package contains library source intended for building other packages
which use "serde1" feature of "%{crate}" crate.

%files       -n %{name}+serde1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde1_fmt-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/serde1_fmt) = 1.0.0~alpha.6
Requires:       cargo
Requires:       (crate(serde_fmt/default) >= 1.0.0 with crate(serde_fmt/default) < 2.0.0)
Requires:       crate(value-bag) = 1.0.0~alpha.6

%description -n %{name}+serde1_fmt-devel %{_description}

This package contains library source intended for building other packages
which use "serde1_fmt" feature of "%{crate}" crate.

%files       -n %{name}+serde1_fmt-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde1_lib-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/serde1_lib) = 1.0.0~alpha.6
Requires:       cargo
Requires:       (crate(serde) >= 1.0.0 with crate(serde) < 2.0.0)
Requires:       crate(value-bag) = 1.0.0~alpha.6

%description -n %{name}+serde1_lib-devel %{_description}

This package contains library source intended for building other packages
which use "serde1_lib" feature of "%{crate}" crate.

%files       -n %{name}+serde1_lib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/std) = 1.0.0~alpha.6
Requires:       cargo
Requires:       crate(value-bag) = 1.0.0~alpha.6

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sval-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/sval) = 1.0.0~alpha.6
Requires:       cargo
Requires:       crate(value-bag) = 1.0.0~alpha.6
Requires:       crate(value-bag/sval1) = 1.0.0~alpha.6

%description -n %{name}+sval-devel %{_description}

This package contains library source intended for building other packages
which use "sval" feature of "%{crate}" crate.

%files       -n %{name}+sval-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sval1-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/sval1) = 1.0.0~alpha.6
Requires:       cargo
Requires:       crate(value-bag) = 1.0.0~alpha.6
Requires:       crate(value-bag/sval1_lib) = 1.0.0~alpha.6

%description -n %{name}+sval1-devel %{_description}

This package contains library source intended for building other packages
which use "sval1" feature of "%{crate}" crate.

%files       -n %{name}+sval1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sval1_lib-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/sval1_lib) = 1.0.0~alpha.6
Requires:       cargo
Requires:       (crate(sval/fmt) >= 1.0.0~alpha.5 with crate(sval/fmt) < 2.0.0)
Requires:       crate(value-bag) = 1.0.0~alpha.6

%description -n %{name}+sval1_lib-devel %{_description}

This package contains library source intended for building other packages
which use "sval1_lib" feature of "%{crate}" crate.

%files       -n %{name}+sval1_lib-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(value-bag/test) = 1.0.0~alpha.6
Requires:       cargo
Requires:       crate(value-bag) = 1.0.0~alpha.6
Requires:       crate(value-bag/std) = 1.0.0~alpha.6

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages
which use "test" feature of "%{crate}" crate.

%files       -n %{name}+test-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Mar 25 2021 Bernhard Rosenkränzer <bero@lindev.ch> - 1.0.0~alpha.6-1
- Initial package
