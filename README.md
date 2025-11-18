🖧 Samba AD DC para RHEL 9.x / Rocky Linux 9.x / AlmaLinux 9.x

Repositório oficial de build do Samba 4.23.x mantido pela Onbit Technology

Este repositório disponibiliza o Samba 4.23.x com suporte completo a Active Directory Domain Controller (AD DC) para todas as distribuições baseadas em RHEL 9.x.

Compatível com:

Rocky Linux 9.x

AlmaLinux 9.x

RHEL 9.x

CentOS Stream 9

Oracle Linux 9.x

O pacote é construído seguindo o bootstrap oficial do Samba, garantindo todas as dependências necessárias para AD DC com MIT Kerberos.

🚀 Instalação (RHEL 9 / Rocky 9 / Alma 9)
1. Habilite os repositórios necessários do sistema
sudo dnf install -y dnf-plugins-core epel-release
sudo dnf config-manager --set-enabled crb

2. Habilite o repositório GlusterFS 9 (dependência usada pelo Samba)
sudo dnf install -y centos-release-gluster9

📦 Instalação dos Pré-Requisitos (bootstrap oficial do Samba)

Antes de instalar o Samba do repositório da Onbit, instale todos os pacotes obrigatórios utilizados pelo build oficial do Samba:

sudo dnf install -y \
    --setopt=install_weak_deps=False \
    "@Development Tools" \
    acl attr autoconf avahi-devel bind-utils binutils bison \
    cargo ccache chrpath clang-devel crypto-policies-scripts cups-devel \
    dbus-devel docbook-dtds docbook-style-xsl flex gawk gcc gdb git \
    glib2-devel glibc-common glibc-langpack-en \
    glusterfs-api-devel glusterfs-devel \
    gnutls-devel gnutls-utils gpgme-devel gzip hostname \
    jansson-devel jq keyutils-libs-devel \
    krb5-devel krb5-server krb5-workstation \
    libacl-devel libarchive-devel libattr-devel libblkid-devel libbsd-devel \
    libcap-devel libevent-devel libicu-devel libpcap-devel \
    libtasn1-devel libtasn1-tools libtirpc-devel libunwind-devel \
    liburing-devel libuuid-devel libxslt lmdb lmdb-devel \
    lsb_release make mingw64-gcc ncurses-devel \
    openldap-devel openssl-devel pam-devel patch perl \
    perl-Archive-Tar perl-ExtUtils-MakeMaker perl-Parse-Yapp perl-Test-Simple \
    perl-generators perl-interpreter pkgconfig popt-devel \
    procps-ng psmisc python3 python3-cryptography python3-devel \
    python3-dns python3-gpg python3-iso8601 python3-libsemanage \
    python3-markdown python3-policycoreutils python3-pyasn1 \
    python3-requests python3-setproctitle \
    quota-devel readline-devel rng-tools rpcgen \
    rpcsvc-proto-devel rsync sed sudo systemd-devel \
    tar tracker-devel tree utf8proc-devel wget which \
    xfsprogs-devel xz yum-utils zlib-devel


Esses pacotes são exatamente os utilizados pela equipe do Samba nos bootstrap scripts oficiais.

🔧 Instalar o Samba do repositório Onbit
sudo dnf copr enable onbittechnology/repo-enterprise
sudo dnf install samba

🧩 Sobre

Este projeto é mantido pela:

Onbit Technology – Infraestrutura, Segurança, Linux & Active Directory
📧 suporte@onbit.tech

🌐 https://onbit.tech
