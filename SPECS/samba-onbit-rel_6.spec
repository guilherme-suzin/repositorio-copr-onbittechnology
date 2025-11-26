Name:           samba
Version:        4.23.3
Release:        6%{?dist}
Summary:        Server and client for SMB/CIFS and Active Directory
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.samba.org
Source0:        %{name}-%{version}.tar.gz

# ==== Build feature toggles ===============================================
# habilite/desabilite com:  rpmbuild ... --with/--without ad_dc
%bcond_without ad_dc
%bcond_without cups
%bcond_without pam
%bcond_without snapper
%bcond_with    check

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

# Docbook
BuildRequires:  docbook-style-xsl

# ACL / xattr
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel

# PIDL/IDL, misc
BuildRequires:  glib2-devel

# Bindings Python para libs samba
BuildRequires:  python3-talloc
BuildRequires:  python3-tdb
BuildRequires:  python3-tevent
BuildRequires:  python3-ldb

# Libs C obrigatórias
BuildRequires:  libtalloc
BuildRequires:  libtalloc-devel
BuildRequires:  libtevent
BuildRequires:  libtevent-devel

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

# Snapper (vfs_snapper)
%if %{with snapper}
BuildRequires:  dbus
BuildRequires:  dbus-devel
%endif

# Tools diversos
BuildRequires:  libxslt
BuildRequires:  keyutils-libs-devel
BuildRequires:  libunwind-devel
BuildRequires:  libuuid-devel
BuildRequires:  libpcap-devel
BuildRequires:  lmdb-devel
BuildRequires:  python3-markdown

# Para macros systemd
BuildRequires:  systemd-rpm-macros

# ==== Selftests (opcionais; habilite com --with check) ====================
%if %{with check}
BuildRequires:  bash
BuildRequires:  python3-iso8601
BuildRequires:  python3-cryptography
BuildRequires:  python3-pyasn1
%endif

# ==== Runtime (mínimo coerente para rodar) ================================
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
Requires:       libtalloc
Requires:       libtevent
Requires:       systemd

# NÃO puxar libldb/python3-ldb da base: o pacote já leva sua própria pilha
# NÃO COLOQUE:
# Requires:       libldb >= 2.11.0
# Requires:       python3-ldb >= 2.11.0

# ==== Requisitos extras para instalar tudo via dnf install samba =========
# (como meta-pacote de setup de ambiente)

Requires: glusterfs-api-devel
Requires: glusterfs-devel

Requires: acl
Requires: attr
Requires: autoconf
Requires: avahi-devel
Requires: bind-utils
Requires: binutils
Requires: bison
Requires: cargo
Requires: ccache
Requires: chrpath
Requires: clang-devel
Requires: crypto-policies-scripts
Requires: cups-devel
Requires: dbus-devel
Requires: docbook-dtds
Requires: docbook-style-xsl
Requires: flex
Requires: gawk
Requires: gcc
Requires: gdb
Requires: git
Requires: glib2-devel
Requires: glibc-common
Requires: glibc-langpack-en
Requires: gnutls-devel
Requires: gnutls-utils
Requires: gpgme-devel
Requires: gzip
Requires: hostname
Requires: jansson-devel
Requires: jq
Requires: keyutils-libs-devel
Requires: ldb-tools
Requires: krb5-devel
Requires: krb5-server
Requires: krb5-workstation
Requires: libacl-devel
Requires: libarchive-devel
Requires: libattr-devel
Requires: libblkid-devel
Requires: libbsd-devel
Requires: libcap-devel
Requires: libevent-devel
Requires: libicu-devel
Requires: libpcap-devel
Requires: libtasn1-devel
Requires: libtasn1-tools
Requires: libtirpc-devel
Requires: libunwind-devel
Requires: liburing-devel
Requires: libuuid-devel
Requires: libxslt
Requires: lmdb
Requires: lmdb-devel
Requires: lsb_release
Requires: make
Requires: mingw64-gcc
Requires: ncurses-devel
Requires: openldap-devel
Requires: openssl-devel
Requires: pam-devel
Requires: patch
Requires: perl
Requires: perl-Archive-Tar
Requires: perl-ExtUtils-MakeMaker
Requires: perl-Parse-Yapp
Requires: perl-Test-Simple
Requires: perl-generators
Requires: perl-interpreter
Requires: pkgconfig
Requires: popt-devel
Requires: procps-ng
Requires: psmisc
Requires: python3
Requires: python3-cryptography
Requires: python3-devel
Requires: python3-dns
Requires: python3-gpg
Requires: python3-iso8601
Requires: python3-libsemanage
Requires: python3-markdown
Requires: python3-policycoreutils
Requires: python3-pyasn1
Requires: python3-requests
Requires: python3-setproctitle
Requires: quota-devel
Requires: readline-devel
Requires: rng-tools
Requires: rpcgen
Requires: rpcsvc-proto-devel
Requires: rsync
Requires: sed
Requires: sudo
Requires: systemd-devel
Requires: tar
Requires: tracker-devel
Requires: tree
Requires: utf8proc-devel
Requires: wget
Requires: which
Requires: xfsprogs-devel
Requires: xz
Requires: yum-utils
Requires: zlib-devel

# ====================================================================
# Replacement do stack Samba/libldb da distro
# ====================================================================

# O pacote samba ONBIT leva sua própria pilha completa (libs, ldb, python, etc.)
# e não consegue coexistir com os pacotes da base.
Conflicts: libldb
Conflicts: ldb-tools
Conflicts: python3-ldb
Conflicts: python3-tdb
Conflicts: samba
Conflicts: samba-common
Conflicts: samba-common-libs
Conflicts: samba-client-libs
Conflicts: libwbclient

Obsoletes: libldb < %{version}
Obsoletes: ldb-tools < %{version}
Obsoletes: python3-ldb < %{version}
Obsoletes: python3-tdb < %{version}
Obsoletes: samba < %{version}
Obsoletes: samba-common < %{version}
Obsoletes: samba-common-libs < %{version}
Obsoletes: samba-client-libs < %{version}
Obsoletes: libwbclient < %{version}

Provides: libldb = %{version}-%{release}
Provides: ldb-tools = %{version}-%{release}
Provides: python3-ldb = %{version}-%{release}
Provides: python3-tdb = %{version}-%{release}
Provides: samba-common = %{version}-%{release}
Provides: samba-common-libs = %{version}-%{release}
Provides: samba-client-libs = %{version}-%{release}
Provides: libwbclient = %{version}-%{release}

# systemd scriptlets dependencies
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

# ==== Mega bloco extra de BuildRequires (do .spec de referência) =========
# Mantido para builds mais completos em EPEL9/EPEL10 (CodeReady/CRB habilitado)
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

# ====================================================================
# PRE – validação de repositórios
# ====================================================================
%pre
missing_repo=0

check_repo() {
    repo_id="$1"
    if ! dnf repolist --enabled 2>/dev/null | grep -q "^${repo_id}"; then
        echo "⚠ Repositório obrigatório ausente: ${repo_id}"
        missing_repo=1
    fi
}

echo "🔍 Verificando repositórios obrigatórios (epel, crb, gluster9, dnf-core)..."

check_repo "epel"
check_repo "crb"
check_repo "gluster9"
check_repo "dnf-core"

if [ "$missing_repo" -eq 1 ]; then
    echo
    echo "❌ Não foi possível instalar o pacote Samba ONBIT."
    echo "Para corrigir, ative os repositórios necessários e tente novamente:"
    echo
    echo "   sudo dnf install epel-release"
    echo "   sudo dnf config-manager --set-enabled crb"
    echo "   sudo dnf install centos-release-gluster9"
    echo "   sudo dnf install dnf-plugins-core"
    echo
    echo "Depois rode novamente:"
    echo "   sudo dnf install samba"
    echo
    exit 1
fi

exit 0

%prep
%autosetup -n %{name}-%{version}

%build
./configure \
   --prefix=/usr \
   --exec-prefix=/usr \
   --libdir=%{_libdir} \
   --sbindir=%{_sbindir} \
   --sysconfdir=/etc \
   --mandir=/usr/share/man \
   --enable-fhs \
   --bundled-libraries=cmocka

make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# NÃO REMOVER libs privadas do Samba / LDB, pois são necessárias.
# Apenas remover manpage de talloc (conflito com libtalloc-devel do sistema)
rm -f %{buildroot}%{_mandir}/man3/talloc.3* || true

# NÃO remova os bindings Python aqui, porque eles fazem parte da pilha
# que você está fornecendo (python3-ldb, python3-tdb etc).

# Instala unidade systemd para AD DC
install -d %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/samba-ad-dc.service << 'EOF'
[Unit]
Description=Samba Active Directory Domain Controller
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
Environment=PATH=/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin
ExecStart=/usr/sbin/samba -D
PIDFile=/run/samba/samba.pid
ExecReload=/bin/kill -HUP $MAINPID

[Install]
WantedBy=multi-user.target
EOF

# Manifesto: arquivos do pacote principal
find %{buildroot} -mindepth 1 \( -type f -o -type l -o -type d \) \
   | sed "s|^%{buildroot}||" \
   | grep -vE '^/$|^%{_sbindir}$|^/usr$|^/usr/bin$|^/usr/lib$|^/usr/lib64$' \
   | grep -vE '^/usr/lib/debug/|^/usr/lib/.build-id/|^%{_mandir}/' \
   | sort -u > %{_builddir}/filelist.manifest

%post
# Ativa/atualiza serviço systemd
%systemd_post samba-ad-dc.service

# Cria um smb.conf básico na primeira instalação (não sobrescreve)
if [ ! -f %{_sysconfdir}/samba/smb.conf ]; then
   mkdir -p %{_sysconfdir}/samba
   cat > %{_sysconfdir}/samba/smb.conf <<'EOF'
[global]
    workgroup = TESTE
    realm = TESTE.NET
    netbios name = SERVER
    server string = Domain Controller (DC) TESTE.NET - Samba %v
    server role = active directory domain controller
    disable netbios = yes
    smb ports = 445
    dns proxy = no
    server min protocol = SMB3

    # === Configurações de Log e Desempenho (Padrão) ===
    log file = /var/log/samba/log.%m
    max log size = 10000
    log level = 3

    # Otimização de I/O
    use sendfile = yes
    aio read size = 1024
    aio write size = 1024

    # homes = /home/%U
    # read only = no
EOF
fi

%preun
%systemd_preun samba-ad-dc.service

%postun
%systemd_postun_with_restart samba-ad-dc.service

%check
%if %{with check}
# Selftests desabilitados por padrão; habilite com --with check
true
%endif

# ====================================================================
# Pacote principal
# ====================================================================

%files -f %{_builddir}/filelist.manifest
%license COPYING
%doc README*
%dir %{_sysconfdir}/samba
%config(noreplace) %ghost %{_sysconfdir}/smb.conf
%{_unitdir}/samba-ad-dc.service

%changelog
* Wed Nov 19 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-6
- Mantido replacement completo da pilha Samba/libldb/python3 da distro
- Removidos Requires para libldb/python3-ldb (evita puxar pacotes da base e conflito com samba-client-libs)
- Mantidos Conflicts/Obsoletes/Provides para libldb, python3-ldb, python3-tdb, samba*, libwbclient
- Mantido serviço systemd samba-ad-dc.service e checagem de repositórios

* Tue Nov 18 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-3
- Transformado o pacote samba em replacement completo do stack Samba/libldb da distro.
- Removidos Requires de libldb/python3-ldb da base.
- Adicionados Conflicts/Obsoletes/Provides para libldb, ldb-tools, python3-ldb, python3-tdb, samba*, libwbclient.
- Incluídas todas as libs/módulos em {_libdir}/samba/ no pacote principal.

* Mon Nov 17 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-2
- Split private Samba libraries into samba-private-libs subpackage
- Keep libldb-cmdline-private-samba.so to satisfy private LDB symbol
- Adjust BuildRequires for EL9/EL10 (libxslt, libtalloc/libtevent, drop python3-*-devel)
- Fix filelist to not own /usr/sbin (filesystem conflict)

* Sat Nov 15 2025 Guilherme Suzin <suporte@onbit.tech> - 4.23.3-1
- Initial packaging for EL9/EL10 (configure/make, manifest, smb.conf ghost)

