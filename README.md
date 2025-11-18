# Samba AD DC para Rocky Linux 10  
**Repositório de build do Samba 4.23.3 mantido por Onbit Technology**

Este repositório contém o pacote **Samba Active Directory Domain Controller atualizado para o Rocky Linux 10**, incluindo scripts, arquivos SPEC e fontes utilizadas para compilar o RPM personalizado.

---

## 📦 Description

Este projeto fornece **pacotes atualizados do Samba (4.23.3)** compatíveis com:

- Rocky Linux 10
- RHEL 10 Beta
- CentOS Stream 10

Os pacotes são construídos com foco em:

- Ambiente corporativo  
- Suporte completo ao **AD DC**  
- Compatibilidade com MIT Kerberos  
- Build simples (sem subpacotes complexos)
- Instalação limpa via `/usr`, `/etc/samba`, `/var/lib/samba`, etc.

Este build é mantido pela **Onbit Technology** para uso interno e público.

---

## 🚀 Installation Instructions

Para instalar os pacotes compilados pela Onbit, basta habilitar o repositório COPR:

```bash
sudo dnf install -y dnf-plugins-core
sudo dnf install -y epel-release
sudo dnf config-manager --set-enabled crb
sudo dnf copr enable onbittechnology/onbit-samba
sudo dnf install samba
