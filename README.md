# 🖧 Samba AD DC para RHEL 9.x / Rocky 9.x / AlmaLinux 9.x

**Repositório: `onbittechnology/repo-enterprise`**

Este repositório entrega versões atualizadas do **Samba 4.23.x** com suporte completo ao **Active Directory Domain Controller (AD DC)** para todo o ecossistema baseado em **RHEL 9**.

Compatível com:

* **Rocky Linux 9.x**
* **AlmaLinux 9.x**
* **RHEL 9.x**
* **CentOS Stream 9**
* **Oracle Linux 9.x**

---

## 📦 Sobre

Os pacotes foram construídos seguindo as recomendações oficiais do **bootstrap Samba**, garantindo:

* Ambiente estável e corporativo
* Suporte AD DC completo
* Compatibilidade total com MIT Kerberos
* Dependências 100% alinhadas ao upstream Samba Team

Repositório mantido pela **Onbit Technology**.

---

## 🚀 Pré-requisitos (obrigatórios)

Execute os comandos abaixo **antes** de instalar o Samba.

### 1. Habilitar repositórios necessários

```bash
sudo dnf install -y dnf-plugins-core epel-release
sudo dnf config-manager --set-enabled crb
```

### 2. Habilitar GlusterFS (dependência oficial Samba upstream)

```bash
sudo dnf install -y centos-release-gluster9
```

---

## 🧰 Instalar pacotes obrigatórios

Lista oficial do bootstrap Samba upstream:

```bash
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
```

---

## 🟪 Instalar o Samba da Onbit Technology

```bash
sudo dnf copr enable onbittechnology/repo-enterprise
sudo dnf install samba
```

---

## 📘 Informações

Os pacotes gerados seguem a estrutura padrão:

* `/usr/bin`
* `/usr/sbin`
* `/etc/samba`
* `/var/lib/samba`
* `/usr/lib64/samba` (private libs)

---

## 👤 Maintainer

**Onbit Technology — Infraestrutura & Segurança da Informação**
🌐 [https://onbit.tech](https://onbit.tech)
📧 [suporte@onbit.tech](mailto:suporte@onbit.tech)
