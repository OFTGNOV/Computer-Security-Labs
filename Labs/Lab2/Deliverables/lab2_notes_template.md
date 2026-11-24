# Lab 2 — Lab Notes, Timings & Deliverables Log

> **Student ID**: 2301563  
> **Module**: Computer Security — Lab 2: Password Cracking (Windows, Linux & ZIP)  
> **Environment**: Isolated VirtualBox `LabNet` (`192.168.100.0/24`)

---

## 1. Lab Environment & Network Record

| Machine | OS / Role | Assigned IP (`LabNet`) | Pre-Lab Snapshot Taken? |
| :--- | :--- | :--- | :---: |
| **Attacker VM** | Kali Linux (`kali-linux-2026.3`) | `192.168.100.3` | [x] |
| **Windows Target VM** | Windows 10 (`tamai-win10-compsec-lab`) | `192.168.100.4` | [x] |
| **Linux Target VM** | Ubuntu 22.04 LTS (`tamai-ubuserv-compsec-lab`) | `192.168.100.5` | [x] |

---

## 2. Cracking Execution Log & Timings

Record exact commands, hash formats, speeds (`p/s` or `c/s` — press `Space` while John runs), elapsed times, and cracked accounts below:

### Section 1: Windows Passwords (`--format=NT`)

| Mode | Command Run | Speed (`p/s`) | Duration | Accounts Cracked & Passwords |
| :--- | :--- | :--- | :--- | :--- |
| **Hive Dump** | `impacket-secretsdump -sam SAM.save -system SYSTEM.save LOCAL > winhashes.txt` | N/A | ___ s | BootKey: `0x...` |
| **1. Single** | `john --single --format=NT --pot=nt_single.pot winhashes.txt` | ___ | ___ s | |
| **2. Wordlist + Rules** | `john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt --rules --pot=nt_wordlist.pot winhashes.txt` | ___ | ___ s | |
| **3. Incremental** | `john --format=NT --incremental --pot=nt_inc.pot winhashes.txt` | ___ | ___ s | |

### Section 2: Linux Shadow Passwords (`linux.hashes`)

- **Observed Hash Prefix in `linux.hashes`**: `$___$` (e.g., `$y$` = `yescrypt`)

| Mode | Command Run | Speed (`c/s`) | Duration | Accounts Cracked & Result |
| :--- | :--- | :--- | :--- | :--- |
| **Unshadow** | `unshadow ubuntu-passwd.copy ubuntu-shadow.copy > linux.hashes` | N/A | ___ s | Merged `alice` & `bob` |
| **1. Single** | `john --single linux.hashes` | ___ | ___ s | |
| **2. Wordlist + Rules** | `john --wordlist=/usr/share/wordlists/rockyou.txt --rules linux.hashes` | ___ | ___ m ___ s | `alice`: Cracked (`___`) / `bob`: Uncracked |
| **3. Incremental** | `john --incremental linux.hashes` | ___ | Stopped at ___ m | Unfeasible for `bob` passphrase |

### Section 3: ZIP Archives (`ZipCrypto` vs `AES-256`)

| Archive | Cipher / Hash Format | Crack Command | Speed (`p/s`) | Outcome & Notes |
| :--- | :--- | :--- | :--- | :--- |
| `secrets-legacy.zip` | PKZIP 2.0 (`$pkzip$`) | `john --wordlist=/usr/share/wordlists/rockyou.txt --rules zip-legacy.hash` | ___ | Cracked in ___ s (`___`) |
| `secrets-aes.zip` | WinZip AES-256 (`$zip2$`) | `john --wordlist=/usr/share/wordlists/rockyou.txt --rules zip-aes.hash` | ___ | Resisted cracking (stopped after ___ min) |

---

## 3. Screenshots Checklist

Save all screenshots into `Labs/Lab2/Deliverables/` as you complete each stage:

- [ ] `01_win10_reg_save_and_winscp.png` — Windows 10 Admin CMD (`reg save` SAM & SYSTEM) + WinSCP SFTP transfer to Kali.
- [ ] `02_kali_impacket_winhashes.png` — `impacket-secretsdump` and `cat winhashes.txt` showing `bootKey` and NTLM hashes.
- [ ] `03_kali_john_ntlm_cracked.png` — John cracking Windows NTLM hashes across modes + `john --show --format=NT winhashes.txt`.
- [ ] `04_ubuntu_shadow_and_scp.png` — Ubuntu `adduser alice` & `bob`, copying `/etc/passwd` + `/etc/shadow`, and `scp` to Kali.
- [ ] `05_kali_unshadow_and_linux_john.png` — `unshadow` (`$y$` prefix visible) + `john --show linux.hashes` (`alice` cracked, `bob` intact).
- [ ] `06_kali_zipcrypto_cracked.png` — `zip -e`, `zip2john`, and `john --show zip-legacy.hash` cracking the legacy archive.
- [ ] `07_kali_aes256_resisted.png` — `7z a -tzip -p -mem=AES256`, `zip2john`, and John failing to crack the strong AES-256 passphrase.

---

## 4. Report Link (Once Submitted)

- Google Doc / Report URL: *(paste link here once drafted, matching Lab 1 convention)*
