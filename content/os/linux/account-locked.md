---
title: "[Solution] Linux: account-locked — account locked error"
description: "Fix Linux account-locked errors. account locked error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["security"]
weight: 4
---

# Linux: Account Locked

Account locked errors prevent login after too many failed attempts or administrative action.

## Common Causes

- Too many failed login attempts (pam_tally2, faillock)
- Administrator manually locked the account
- Password expiration with expired account
- Account disabled in /etc/shadow
- SSH AllowUsers/DenyUsers restriction

## How to Fix

### 1. Check Account Status

```bash
sudo passwd -S <username>
sudo pam_tally2 -u <username> 2>/dev/null || sudo faillock --user <username>
```

### 2. Unlock Account

```bash
sudo passwd -u <username>
sudo pam_tally2 -r -u <username> 2>/dev/null || sudo faillock --user <username> --reset
```

### 3. Check Shadow File

```bash
sudo grep <username> /etc/shadow
# If password field starts with !, account is locked
sudo passwd -u <username>
```

## Examples

```bash
$ sudo passwd -S john
john L 07/20/2026 0 99999 7 -1
# L = locked
$ sudo pam_tally2 -u john
Login Failures Latest failure From
john    5      07/20/26 14:30:45  sshd
$ sudo pam_tally2 -r -u john
$ sudo passwd -u john
passwd: password expiry information changed.
```
