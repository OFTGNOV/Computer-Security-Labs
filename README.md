# Computer Security Labs — Master Repository & Delivery Guide

Welcome to the **Computer Security Labs** master repository. This repository contains the code, data, installation artifacts, configuration guides, and converted laboratory manuals for all six computer security labs.

---

## 🧭 Repository Lab Navigator

| Lab Directory                                                                      | Topic & Title                                | Primary Target / Environment          | Key Tools & Dependencies                                                         | Status |
|:---------------------------------------------------------------------------------- |:-------------------------------------------- |:------------------------------------- |:-------------------------------------------------------------------------------- |:------:|
| [`Labs/Lab1/`](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab1/README.md) | **Digital Self-Defense (The Citadel)**       | Windows 10/11 Host                    | Sandboxie-Plus, KeePass, VeraCrypt, Privacy Badger, Python                       | ✓      |
| [`Labs/Lab2/`](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab2/README.md) | **Password Cracking (Win, Linux & ZIP)**     | Kali Linux, Windows 10, Ubuntu VMs    | John the Ripper, Impacket (`secretsdump`), `unshadow`, `zip2john`, `rockyou.txt` | ◧      |
| [`Labs/Lab3/`](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab3/README.md) | **SQL Injection (SQLi) with DVWA**           | VirtualBox / Docker (DVWA Low)        | Web Browser, MySQL / MariaDB, Information Schema, PHP                            | ▢      |
| [`Labs/Lab4/`](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab4/README.md) | **Proxychains for Anonymous Hacking**        | Kali Linux VM                         | `proxychains4`, `tor`, `whois`, `curl`, `firefox-esr`                            | ▢      |
| [`Labs/Lab5/`](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab5/README.md) | **Social Engineering & Phishing Simulation** | Kali Linux VM & Client VM (Host-Only) | Social Engineering Toolkit (`setoolkit`), Apache, Browser                        | ▢      |
| [`Labs/Lab6/`](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab6/README.md) | **Asymmetric Encryption using RSA**          | Host / `.venv` Python 3               | Python 3, `pycryptodome` (PKCS1_OAEP, SHA-256, PKCS1_v1.5)                       | ▢      |

---

## ⚙️ Global Dependencies & Machine Requirements

### 1. Host Machine Environment

- **Operating System**: Windows 10 or 11 (Host)

- **Virtualization Hypervisor**: [VirtualBox](https://www.virtualbox.org/) (Recommended) or VMware Workstation Player

- **Python Virtual Environment**: Initialized in `.venv/` at the repository root. Always run Python scripts using:
  
  ```powershell
  .\.venv\Scripts\python.exe <script-path>
  ```
  
  *(Packages installed: `pycryptodome`)*

### 2. Virtual Machines (VMs) Needed

To complete all offensive and defensive labs, ensure the following VMs are prepared on your hypervisor:

1. **Kali Linux VM** (Used in Labs 2, 4, 5, and optionally 3):
   
   - Pre-installed with penetration testing suites.
   - Packages to install: `tor`, `proxychains4`, `python3-impacket`, `set` (SET).

2. **Ubuntu Linux VM (22.04 LTS)** (Used in Lab 2):
   
   - Standard user and sudo accounts (`alice`, `bob`) for `/etc/shadow` extraction.

3. **Windows 10 Target VM** (Used in Lab 2 and as client in Lab 5):
   
   - Local administrator privileges for registry SAM/SYSTEM hive extraction.

4. **Vulnerable Web App (DVWA)** (Used in Lab 3):
   
   - Can run as a standalone VM (e.g. Metasploitable2 or Debian DVWA) or inside Docker on Kali:
     
     ```bash
     sudo docker run --rm -it -p 80:80 vulnerables/web-dvwa
     ```

### 3. Security Tools Catalog & Host Utilities

All tools and environment requirements are documented in the [Tools Directory Catalog](file:///d:/Dev/Projects/Computer-Security-Labs/tools/README.MD). Pre-staged installers and tool metadata are stored in [`tools/`](file:///d:/Dev/Projects/Computer-Security-Labs/tools/) (with `.msi`, `.exe`, and `.yaml` files git-ignored):

- `Sandboxie-Plus` (Process sandboxing)
- `KeePass 2` (Encrypted password vault)
- `VeraCrypt` (On-the-fly disk encryption)
- `VeraCrypt_1.26.29_Machine_X64_wix_en-US.msi`

---

## 📋 Comprehensive Lab-by-Lab Summary & Deliverables

### [Lab 1: Operation Digital Self-Defense](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab1/README.md)

- **Core Concept**: Defense in Depth (Moat, Sentries, Gatekeeper, Keep).
- **Execution**: Run `SandboxTest.py` inside Sandboxie `DefaultBox`, configure KeePass with 10M key transformation rounds, create and mount a 20MB VeraCrypt container (`MySecretVault.hc`).
- **Required Deliverables**:
  - One consolidated screenshot showing KeePass with vault password entry and VeraCrypt with mounted drive `Z:`.
  - Answers to the 5 discussion questions.

### [Lab 2: Password Cracking (Windows, Linux & ZIP)](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab2/README.md)

- **Core Concept**: Hashing mechanics, salts, computational cost (rounds), and offline attacks.
- **Execution**: Extract Windows SAM/SYSTEM hives (`reg save`) and dump NTLM hashes with Impacket. Unshadow Linux `/etc/passwd` and `/etc/shadow`. Create and crack ZipCrypto vs AES-256 ZIPs using John the Ripper.
- **Required Deliverables**:
  - Terminal screenshots showing hash extraction, John cracking NTLM, Linux shadow, and ZipCrypto.
  - Answers to discussion questions on salts, rainbow tables, bcrypt/yescrypt vs MD5, and Pass-the-Hash.

### [Lab 3: SQL Injection (SQLi) with DVWA](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab3/README.md)

- **Core Concept**: In-band UNION-based SQLi, database enumeration, password hash dumping.
- **Execution**: Exploit DVWA (Security: Low) through 7 progressive payloads to enumerate DB version, user, `information_schema.tables`, and dump accounts/hashes from `users`.
- **Required Deliverables**:
  - Screenshots of each successful injection stage.
  - Dumped credential tables and hashes.
  - Secure remediation code (PDO parameterized queries).

### [Lab 4: Using Proxychains for Anonymous Hacking](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab4/README.md)

- **Core Concept**: Network anonymization, TCP socket hooking via `LD_PRELOAD`, Tor SOCKS5 chaining, DNS leaks, browser fingerprinting.
- **Execution**: Configure `/etc/proxychains4.conf` (`dynamic_chain`, `proxy_dns`, `socks5 127.0.0.1 9050`). Start Tor daemon. Verify IP spoofing with `dnsleaktest.com` and run anonymous `whois`.
- **Required Deliverables**:
  - Screenshots of Proxychains config, IP comparison (direct vs proxied), DNS leak test, and WHOIS lookup.
  - Full answers to the 9 lab questions in Section 6.

### [Lab 5: Social Engineering Simulation & Phishing Detection](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab5/README.md)

- **Core Concept**: Human psychological vectors, credential harvesting, URL/TLS inspection, phishing-resistant authentication (FIDO2).
- **Execution**: Configure SET (`setoolkit`) on Kali to clone a mock login portal on host-only network. Submit disposable credentials (`student01@example.test` / `LabOnly-Example-482!`) from client VM. Capture telemetry.
- **Required Deliverables**:
  - Lab network architecture diagram.
  - Screenshots of client visiting raw IP and SET intercepting dummy credentials.
  - Lab report containing scope confirmation, evidence analysis, and answers to the 8 evaluation questions.

### [Lab 6: Asymmetric Encryption using RSA](file:///d:/Dev/Projects/Computer-Security-Labs/Labs/Lab6/README.md)

- **Core Concept**: Trapdoor functions, key pairs, PKCS1_OAEP padding, digital signatures, non-repudiation.
- **Execution**: Run `.\.venv\Scripts\python.exe Labs\Lab6\rsa_lab.py` to generate 2048-bit keys, encrypt/decrypt plaintext, and generate/verify SHA-256 digital signatures with tampering detection.
- **Required Deliverables**:
  - Generated keys: `private_key.pem`, `public_key.pem`.
  - Executable script: `rsa_lab.py`.
  - Terminal output / screenshot showing all tests passing.
  - Written answers to the 3 discussion questions.

---

## 🚀 Quick Execution Test (Lab 6)

To test the Python virtual environment and run the Lab 6 cryptographic verification right now:

```powershell
.\.venv\Scripts\python.exe Labs\Lab6\rsa_lab.py
```
