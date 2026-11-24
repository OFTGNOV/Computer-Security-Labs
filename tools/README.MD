# Security Tools & Environment Catalog

This directory serves as the centralized catalog and staging area for tools, installers, and environment utilities required to complete all six Computer Security labs.

> [!NOTE]
> Windows installer binaries (`*.exe`, `*.msi`) and winget manifest metadata (`*.yaml`) stored in this directory are excluded from version control via `.gitignore` to keep the repository lightweight. Download links and package manager commands are provided below.

---

## 🧰 Comprehensive Tool Breakdown by Lab & Environment

### 1. Host Endpoint Security Tools (Windows 10/11)

These tools are installed directly onto the host operating system to build multi-layered endpoint defenses (**Lab 1: Operation Digital Self-Defense**):

| Tool | Lab | Primary Purpose | Installation / Source |
| :--- | :---: | :--- | :--- |
| **Sandboxie-Plus** | Lab 1 | Application process isolation & sandboxing. Runs untrusted executables and browsers in an ephemeral sandbox (`DefaultBox`), isolating file and registry modifications. | [Sandboxie-Plus GitHub](https://github.com/sandboxie-plus/Sandboxie/releases) or `winget install Sandboxie.Plus` |
| **KeePass 2** | Lab 1 | Encrypted offline password vault (`.kdbx`). Generates and securely stores high-entropy master credentials with hardened key transformation rounds (~10M rounds or Argon2d). | [keepass.info](https://keepass.info/) or `winget install DominikReichl.KeePass` |
| **VeraCrypt** | Lab 1 | On-The-Fly Encryption (OTFE) system. Creates encrypted virtual disk containers (AES-256 / SHA-512) mounted as virtual drives (e.g. `Z:`) to protect sensitive files at rest. | [veracrypt.fr](https://www.veracrypt.fr/) or `winget install IDRIX.VeraCrypt` |
| **Privacy Badger** | Lab 1 | Browser privacy extension from the EFF. Automatically blocks invisible third-party tracking domains and behavioral surveillance cookies. | [privacybadger.org](https://privacybadger.org/) (Chrome / Firefox store) |

---

### 2. Python Virtual Environment (`.venv`)

A dedicated Python 3 virtual environment located at the root of the repository (`.venv/`) is used to execute all scripting and cryptographic implementations:

| Tool / Package | Lab | Primary Purpose | Command / Path |
| :--- | :---: | :--- | :--- |
| **Python 3.15 Runtime** | Lab 1, 6 | Executes repository scripts in an isolated Python environment without polluting global host site-packages. | `.\.venv\Scripts\python.exe` |
| **`pycryptodome`** | Lab 6 | Modern cryptography library. Provides 2048-bit RSA key generation, `PKCS1_OAEP` padding cipher, SHA-256 hashing, and `PKCS#1 v1.5` digital signatures. | `.\.venv\Scripts\pip.exe install pycryptodome` |
| **`SandboxTest.py`** | Lab 1 | Isolation verification script. Attempts to create a file on the Desktop and clear the Recycle Bin to prove sandboxing confinement. | `.\.venv\Scripts\python.exe Labs\Lab1\SandboxTest.py` |
| **`rsa_lab.py`** | Lab 6 | Complete RSA encryption, decryption, Base64 encoding, and digital signature test harness. | `.\.venv\Scripts\python.exe Labs\Lab6\rsa_lab.py` |

---

### 3. Offensive Security & Penetration Testing Tools (Kali Linux VM)

These utilities are executed on a Kali Linux virtual machine to simulate attacks, crack credentials, and test network privacy:

| Tool | Lab | Primary Purpose | Installation / Invocation Command |
| :--- | :---: | :--- | :--- |
| **John the Ripper (`john`)** | Lab 2, 3 | High-speed offline password cracking tool. Supports `--single` (seed-based), `--wordlist --rules` (dictionary mangling), `--incremental` (brute-force), and `--format=raw-md5` (DVWA SQLi hash cracking). | Pre-installed on Kali (`john`) |
| **`unshadow`** | Lab 2 | Combines Linux `/etc/passwd` and `/etc/shadow` into a unified format for John to crack. | Pre-installed with John the Ripper (`unshadow`) |
| **`zip2john`** | Lab 2 | Extracts cryptographic hash metadata from password-protected ZIP archives (ZipCrypto and AES-256). | Pre-installed with John the Ripper (`zip2john`) |
| **Impacket (`secretsdump`)** | Lab 2 | Extracts local user accounts and NTLM password hashes from offline Windows registry hives (`SAM` and `SYSTEM`). | `sudo apt install python3-impacket` |
| **`rockyou.txt`** | Lab 2 | Standard wordlist of 14+ million leaked passwords used for dictionary attacks. | `sudo gzip -dk /usr/share/wordlists/rockyou.txt.gz` |
| **Archive Utilities (`zip`, `7z`)** | Lab 2 | Creates legacy PKZIP 2.0 (`ZipCrypto`) and modern `AES-256` encrypted archives for cryptographic comparison. | `sudo apt install zip p7zip-full` (Kali) / `winget install 7zip.7zip` (Host) |
| **OpenSSH (`ssh`, `sshd`, `scp`)** | Lab 2 | Enables encrypted SFTP/SCP file transfers of exported Windows registry hives and Linux shadow copies between VMs. | `sudo apt install openssh-server && sudo systemctl enable --now ssh` |
| **Proxychains-NG (`proxychains4`)** | Lab 4 | Dynamic library hooking tool (`LD_PRELOAD`) that forces outgoing TCP connections of any binary through configured proxies. | `sudo apt install proxychains4` |
| **Tor Service (`tor`)** | Lab 4 | Onion routing daemon providing a local SOCKS5 proxy on `127.0.0.1:9050` to route network traffic through multiple encrypted relays. | `sudo apt install tor` |
| **Social Engineering Toolkit (`setoolkit`)** | Lab 5 | Framework for social engineering simulations. Used to clone target web pages and host a credential harvesting listener on port 80. | `sudo apt install set` |
| **Firefox ESR & DevTools** | Lab 3, 4, 5 | Browser and HTTP inspector (`F12`) used to submit SQLi payloads, inspect URL-encoded `GET` parameters and session cookies (`security=low`), test DNS/IP leaks, and view cloned portals. | `sudo apt install -y firefox-esr` |
| **Recon Utilities** | Lab 4 | Network diagnostic and query tools (`whois`, `curl`, `nslookup`, `lynx`, `w3m`) to verify IP spoofing and DNS routing. | `sudo apt install whois curl dnsutils lynx` |

---

### 4. Target Platforms & Vulnerable Environments

| Target / System | Lab | Role & Description | Access & Deployment |
| :--- | :---: | :--- | :--- |
| **VirtualBox / VMware** | Labs 2–5 | Type-2 Hypervisor managing isolated virtual machines and NAT/host-only subnets (`LabNet` `192.168.100.0/24`). | [virtualbox.org](https://www.virtualbox.org/) |
| **Damn Vulnerable Web App (DVWA)** | Lab 3 | Vulnerable PHP + MariaDB/MySQL web application for hands-on SQL Injection (SQLi) exploitation, `information_schema` enumeration, and PDO remediation. | Kali native: `sudo apt install -y dvwa && sudo dvwa-start` (`:42001`), Ubuntu LAMP (`/var/www/html/dvwa`), or Docker (`vulnerables/web-dvwa`) |
| **Windows 10 Target VM** | Lab 2, 5 | Local administrator target for offline SAM/SYSTEM registry export (`reg save`), and client victim browser for phishing simulations. | Microsoft developer evaluation VM |
| **Ubuntu 22.04 LTS VM** | Lab 2, 3 | Linux target machine for `/etc/passwd` & `/etc/shadow` extraction (Lab 2), and optional Apache2 + MariaDB + PHP host for DVWA at `/dvwa/` (Lab 3). | Ubuntu Server/Desktop ISO |
| **WinSCP / SCP** | Lab 2 | SFTP/SCP file transfer client used to transfer exported registry hives and password shadow files from target VMs to Kali Linux. | [winscp.net](https://winscp.net/) |
