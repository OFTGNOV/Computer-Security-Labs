# Lab 2 — Lab Notes, Timings & Deliverables Log

> **Student ID**: 2301563  
> **Module**: Computer Security — Lab 2: Password Cracking (Windows, Linux & ZIP)  
> **Environment**: Isolated VirtualBox `LabNet` (`192.168.100.0/24`)

---

## 1. Lab Environment & Network Record

| Machine | OS / Role | Assigned IP (`LabNet`) | Pre-Lab Snapshot Taken? |
| :--- | :--- | :--- | :---: |
| **Attacker VM** | Kali Linux (`kali-linux-2026.3-virtualbox-amd64`) | `192.168.100.3` | [x] |
| **Windows Target VM** | Windows 10 (`tamai-win10-compsec-lab`) | `192.168.100.4` | [x] |
| **Linux Target VM** | Ubuntu 22.04 LTS (`tamai-ubu-compsec-lab`) | `192.168.100.6` *(Server pre-test: `.5`)* | [x] |

---

## 2. Cracking Execution Log & Timings

### Section 1: Windows Passwords (`--format=NT`)

| Mode | Command Run | Speed (`p/s` / `c/s`) | Duration | Accounts Cracked & Passwords |
| :--- | :--- | :--- | :--- | :--- |
| **Hive Dump** | `impacket-secretsdump -sam SAM.save -system SYSTEM.save LOCAL > winhashes.txt` | N/A | < 1 s | BootKey: `0xeeeefc3a964a019132ce8712db1eb14a` (`SAM.save` 48K, `SYSTEM.save` 10M; 8 local accounts dumped) |
| **1. Single** | `john --single --format=NT --pot=nt_single.pot winhashes.txt` | `75,150 p/s` (`376,650 C/s`) | `0:00:00:00` (< 1 s) | `Administrator` (`tamai`), `tamai` (`tamai`), `jsmith` (`jsmith1`) — 3 hashes cracked |
| **2. Wordlist + Rules** | `john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt --rules --pot=nt_wordlist.pot winhashes.txt` | AVX2 MD4 high-speed | < 2 s | `cyberx` (`123456`), `hacker` (`Password`), `Guest` (`""` empty), `jsmith` (`jsmith1`), `Administrator` (`tamai`), `tamai` (`tamai`) |
| **3. Incremental** | `john --format=NT --incremental --pot=nt_inc.pot winhashes.txt` | Millions `p/s` | Short run | Cracks short/simple passwords (`Guest`, `123456`, `tamai`) rapidly |

### Section 2: Linux Shadow Passwords (`linux.hashes`)

- **Observed Hash Prefix in `linux.hashes`**: `$y$` (`yescrypt`, `Cost 1 = 10`, `Cost 2 = 1`, 4 OpenMP threads)

| Mode | Command Run | Speed (`p/s` / `c/s`) | Duration | Accounts Cracked & Result |
| :--- | :--- | :--- | :--- | :--- |
| **Unshadow** | `unshadow ubuntu-passwd.copy ubuntu-shadow.copy > linux.hashes` | N/A | < 1 s | Merged `ubuntu-passwd.copy` (`3.0K`) & `ubuntu-shadow.copy` (`1.8K`) — 4 salted hashes |
| **1. Single** | `john --single --pot=linux_single.pot linux.hashes` | `440.4 p/s` (`455.2 c/s`) | `0:00:00:05` (5 s) | `tamai` (`tamai`), `root` (`tamai`) — 2 username-derived hashes cracked |
| **2. Wordlist + Rules** | `john --wordlist=/usr/share/wordlists/rockyou.txt --rules linux.hashes` | `151.1 p/s` (`459.2 c/s`) | Stopped at `0:00:04:26` (`ETA: 2036-02-06`) | `alice`: Cracked (`password123`) / `bob`: **Uncracked** (5+ word passphrase resisted) |
| **3. Incremental** | `john --incremental linux.hashes` | `152.9 p/s` (`458.7 c/s`) | Stopped at `0:00:02:11` | `0g` — Unfeasible against `bob`'s passphrase under `yescrypt` |

### Section 3: ZIP Archives (`ZipCrypto` vs `AES-256`)

| Archive | Cipher / Hash Format | Crack Command | Speed (`p/s`) | Outcome & Notes |
| :--- | :--- | :--- | :--- | :--- |
| `secrets-legacy.zip` | PKZIP 2.0 (`$pkzip$`, 32/64) | `john --wordlist=/usr/share/wordlists/rockyou.txt --rules zip-legacy.hash` | `390,095 p/s` | **Cracked in `0:00:00:00`** (< 1 s) — Password: `kalikali` |
| `secrets-aes.zip` | WinZip AES-256 (`$zip2$`, PBKDF2-SHA1 256/256 AVX2 8x) | `john --wordlist=/usr/share/wordlists/rockyou.txt --rules zip-aes.hash` | `157,199 p/s` | **Resisted cracking** (`0 password hashes cracked, 1 left` after `0:00:04:26`, `0.14%`) |

---

## 3. Screenshots Checklist

All deliverable screenshots verified in `Labs/Lab2/Deliverables/`:

- [x] `0.1-pre-lab2.png` — VirtualBox `LabNet` (`192.168.100.0/24`) pre-lab setup across Kali (`.3`), Windows 10 (`.4`), and Ubuntu (`.5`/`.6`).
- [x] `01_win10_reg_save_winscp.png` — Kali tool verification + WinSCP SFTP session transferring `SAM.save` & `SYSTEM.save` to Kali.
- [x] `02_kali_impacket_winhashes.png` — `impacket-secretsdump` decrypting `SAM.save` (`48K`) with `SYSTEM.save` (`10M`, BootKey `0xeeeefc3a964a019132ce8712db1eb14a`).
- [x] `03_kali_john_ntlm_cracked.png.png` — John cracking Windows NTLM hashes in `--single` and `--wordlist --rules` modes (`tamai`, `jsmith1`, `123456`, `Password`).
- [x] `04_ubuntu_shadow_and_scp.png` — Ubuntu `adduser alice` & `bob`, copying `/etc/passwd` + `/etc/shadow`, and `scp` transfer to Kali.
- [x] `05_kali_unshadow_and_linux_john.png` — John running `--single`, `--wordlist --rules`, and `--incremental` on `$y$` (`yescrypt`) hashes; `alice` cracked (`password123`), `bob` intact (`ETA: 2036`).
- [x] `06_kali_zipcrypto_cracked.png` — `zip -e`, `zip2john` (`$pkzip$`), and John instantly cracking `secrets-legacy.zip` (`kalikali`).
- [x] `07_kali_aes256_resisted.png` — `7z a -tzip -p -mem=AES256`, `zip2john` (`$zip2$`), and `secrets-aes.zip` resisting offline cracking (`0 cracked`).

---

## 4. Report Link

- Google Doc / Report URL: https://docs.google.com/document/d/1I2j0EfYx_rW0aKvvP0kh_gTs6wtJKzr0Pv1I8ByhYsM/edit?usp=sharing
