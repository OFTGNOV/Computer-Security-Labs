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
| **John the Ripper (`john`)** | Lab 2 | High-speed offline password cracking tool. Supports `--single` (seed-based), `--wordlist --rules` (dictionary mangling), and `--incremental` (brute-force) modes. | Pre-installed on Kali (`john`) |
| **`unshadow`** | Lab 2 | Combines Linux `/etc/passwd` and `/etc/shadow` into a unified format for John to crack. | Pre-installed with John the Ripper (`unshadow`) |
| **`zip2john`** | Lab 2 | Extracts cryptographic hash metadata from password-protected ZIP archives (ZipCrypto and AES-256). | Pre-installed with John the Ripper (`zip2john`) |
| **Impacket (`secretsdump`)** | Lab 2 | Extracts local user accounts and NTLM password hashes from offline Windows registry hives (`SAM` and `SYSTEM`). | `sudo apt install python3-impacket` |
| **`rockyou.txt`** | Lab 2 | Standard wordlist of 14+ million leaked passwords used for dictionary attacks. | `gunzip /usr/share/wordlists/rockyou.txt.gz` |
| **Proxychains-NG (`proxychains4`)** | Lab 4 | Dynamic library hooking tool (`LD_PRELOAD`) that forces outgoing TCP connections of any binary through configured proxies. | `sudo apt install proxychains4` |
| **Tor Service (`tor`)** | Lab 4 | Onion routing daemon providing a local SOCKS5 proxy on `127.0.0.1:9050` to route network traffic through multiple encrypted relays. | `sudo apt install tor` |
| **Social Engineering Toolkit (`setoolkit`)** | Lab 5 | Framework for social engineering simulations. Used to clone target web pages and host a credential harvesting listener on port 80. | `sudo apt install set` |
| **Recon Utilities** | Lab 4 | Network diagnostic and query tools (`whois`, `curl`, `nslookup`, `firefox-esr`, `lynx`, `w3m`) to verify IP spoofing and DNS routing. | `sudo apt install whois curl dnsutils lynx` |

---

### 4. Target Platforms & Vulnerable Environments

| Target / System | Lab | Role & Description | Access & Deployment |
| :--- | :---: | :--- | :--- |
| **VirtualBox / VMware** | Labs 2–5 | Type-2 Hypervisor managing isolated virtual machines and host-only subnets. | [virtualbox.org](https://www.virtualbox.org/) |
| **Damn Vulnerable Web App (DVWA)** | Lab 3 | Vulnerable PHP/MySQL web application for hands-on SQL Injection (SQLi) exploitation and database enumeration. | Docker: `sudo docker run --rm -it -p 80:80 vulnerables/web-dvwa` or Metasploitable2 |
| **Windows 10 Target VM** | Lab 2, 5 | Local administrator target for offline SAM/SYSTEM registry export (`reg save`), and client victim browser for phishing simulations. | Microsoft developer evaluation VM |
| **Ubuntu 22.04 LTS VM** | Lab 2 | Linux target machine for creating test accounts and exporting `/etc/passwd` and `/etc/shadow` files. | Ubuntu Server/Desktop ISO |
| **WinSCP / SCP** | Lab 2 | SFTP/SCP file transfer client used to transfer exported registry hives and password shadow files from target VMs to Kali Linux. | [winscp.net](https://winscp.net/) |
