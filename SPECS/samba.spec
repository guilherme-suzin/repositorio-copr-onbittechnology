Name:           samba
Version:        4.23.3
Release:        1%{?dist}
Summary:        Server and client for SMB/CIFS and Active Directory
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.samba.org
Source0:        %{name}-%{version}.tar.gz

# ==== Build feature toggles ===============================================
# habilite com:  rpmbuild … --with ad_dc
%bcond_without ad_dc          # AD DC / MIT krb5 (default: with)
%bcond_without cups           # suporte a impressão CUPS (default: with)
%bcond_without pam            # PAM (default: with)
%bcond_without snapper        # vfs_snapper (dbus) (default: with)
%bcond_with    check          # selftests (default: without)

# ==== Core BuildRequires ==================================================
BuildRequires:  gcc gcc-c++ make
BuildRequires:  python3 python3-devel
BuildRequires:  pkgconf pkgconf-m4 pkgconf-pkg-config
BuildRequires:  redhat-rpm-config
BuildRequires:  zlib-devel
BuildRequires:  gnutls-devel >= 3.4.7
BuildRequires:  libtasn1-devel
BuildRequires:  popt-devel
BuildRequires:  readline-devel
BuildRequires:  jansson-devel
BuildRequires:  libarchive-devel
BuildRequires:  avahi-devel
BuildRequires:  dbus-devel
BuildRequires:  ncurses-devel
BuildRequires:  perl-Parse-Yapp
BuildRequires:  flex
BuildRequires:  bison
# Docbook (nome muda entre EL9/EL10)
%if 0%{?rhel} >= 10
BuildRequires:  docbook-style-xsl
%else
BuildRequires:  docbook-xsl
%endif

# ACL / xattr (AD DC e member servers com ACLs)
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel

# PIDL/IDL, misc
BuildRequires:  glib2-devel

# Samba libs do sistema
BuildRequires:  python3-talloc
BuildRequires:  python3-tdb
BuildRequires:  python3-tevent
BuildRequires:  python3-ldb

# MIT Kerberos (AD DC com MIT; fileserver com MIT)
%if %{with ad_dc}
BuildRequires:  krb5-devel
BuildRequires:  krb5-server
BuildRequires:  krb5-workstation
%endif

# Opcionais úteis
%if %{with cups}
BuildRequires:  cups-devel
%endif
%if %{with pam}
BuildRequires:  pam-devel
%endif
BuildRequires:  gpgme-devel
BuildRequires:  libbsd-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  gnutls-devel

# Snapper (vfs_snapper)
%if %{with snapper}
BuildRequires:  dbus
BuildRequires:  dbus-devel
%endif

# Tools usados em alguns passos/funcionalidades
BuildRequires:  xsltproc
BuildRequires:  keyutils-libs-devel
BuildRequires:  libunwind-devel
BuildRequires:  libuuid-devel
BuildRequires:  libpcap-devel
BuildRequires:  lmdb-devel
BuildRequires:  python3-markdown

# ==== Selftests (opcionais; habilite com --with check) =====================
%if %{with check}
BuildRequires:  bash
BuildRequires:  python3-iso8601
BuildRequires:  python3-cryptography
BuildRequires:  python3-pyasn1
%endif

# ==== Runtime (mínimo coerente; pode ser refinado em subpacotes) ==========
Requires:       gnutls
Requires:       zlib
Requires:       popt
Requires:       readline
Requires:       libarchive
Requires:       avahi-libs
Requires:       dbus-libs
Requires:       jansson
Requires:       pam
Requires:       openldap
Requires:       libbsd
Requires:       lmdb

BuildRequires:  acl attr autoconf avahi-devel bind-utils binutils bison cargo
BuildRequires:  ccache chrpath clang-devel crypto-policies-scripts cups-devel
BuildRequires:  curl dbus-devel docbook-dtds docbook-style-xsl flex gawk gcc gdb git
BuildRequires:  glib2-devel glibc-common glibc-langpack-en 
BuildRequires:  gnutls-devel gnutls-utils gpgme-devel gzip hostname
BuildRequires:  jansson-devel jq keyutils-libs-devel krb5-devel krb5-server krb5-workstation
BuildRequires:  libacl-devel libarchive-devel libattr-devel libblkid-devel libbsd-devel
BuildRequires:  libcap-devel libevent-devel libicu-devel libpcap-devel
BuildRequires:  libtasn1-devel libtasn1-tools libtirpc-devel libunwind-devel libuuid-devel
BuildRequires:  libxslt lmdb lmdb-devel make mingw64-gcc ncurses-devel openldap-devel
BuildRequires:  openssl-devel pam-devel patch perl perl-Archive-Tar perl-ExtUtils-MakeMaker
BuildRequires:  perl-Parse-Yapp perl-Test-Simple perl-generators perl-interpreter pkgconfig
BuildRequires:  popt-devel procps-ng psmisc python3 python3-cryptography python3-devel
BuildRequires:  python3-dns python3-gpg python3-iso8601 python3-libsemanage python3-markdown
BuildRequires:  python3-policycoreutils python3-pyasn1 python3-requests python3-setproctitle
BuildRequires:  quota-devel readline-devel rng-tools rpcgen
BuildRequires:  rpcsvc-proto-devel rsync sed sudo systemd-devel tar tracker-devel
BuildRequires:  utf8proc-devel wget which xfsprogs-devel xz yum-utils zlib-devel


%description
Samba provides SMB/CIFS file and print services and can act as an Active Directory
domain controller. Several utilities (e.g. samba-tool) and the build system are
written in Python 3.x.

%prep
%autosetup -n %{name}-%{version}

%build
# Use SEMPRE o wrapper ./configure (ele prepara PYTHONHASHSEED etc)
./configure \
  --prefix=/usr \
  --exec-prefix=/usr \
  --libdir=%{_libdir} \
  --sbindir=/sbin \
  --sysconfdir=/etc/samba \
  --mandir=/usr/share/man \
  --enable-fhs \
  --bundled-libraries=cmocka

# (Opcional) suavizar warnings deprecados/unused caso seu toolchain trate como erro
# export CFLAGS="%{optflags} -Wno-unused-variable -Wno-unused-but-set-variable -Wno-deprecated-declarations"

make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Manifest exato do que foi instalado (evita check-files)
# Gera caminhos ABSOLUTOS: /usr/bin/..., /etc/samba, etc.
find %{buildroot} -mindepth 1 \( -type f -o -type l -o -type d \) \
  | sed "s|^%{buildroot}||" \
  | grep -vE '^/usr/lib/debug/|^/usr/lib/.build-id/|^%{_mandir}/' \
  | sort -u > %{_builddir}/filelist.manifest

%post
# Cria um smb.conf básico na primeira instalação (não sobrescreve)
if [ ! -f %{_sysconfdir}/samba/smb.conf ]; then
  cat > %{_sysconfdir}/samba/smb.conf <<'EOF'
[global]
   workgroup = WORKGROUP
   server role = standalone server
   disable netbios = yes
   smb ports = 445
EOF
fi

%check
%if %{with check}
# (Opcional) alvo de testes – ajuste conforme seu ambiente CI
# Python-based selftests podem ser longos; deixe desabilitado por padrão
true
%endif

%files -f %{_builddir}/filelist.manifest
%license COPYING
%doc README*
%dir %{_sysconfdir}/samba
%config(noreplace) %ghost %{_sysconfdir}/samba/smb.conf

%changelog
* Sat Nov 15 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-1
- Initial packaging for EL9/EL10 (configure/make, manifest, smb.conf ghost)

