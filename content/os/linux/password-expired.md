---
title: "[Solution] Linux: password-expired — password expired"
description: "Fix Linux password-expired errors. password expired with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["security"]
weight: 4
---
# Linux: Password Expired

A password expired error occurs when a user's password has exceeded its maximum age and must be changed before login.

## Common Causes

- Password age policy requires periodic changes
- chage -M set to a low value forcing frequent changes
- New account with temporary password that must be changed
- System security policy enforcing password rotation
- Inactive account exceeding maximum days between password changes

## How to Fix

### 1. Check Password Status

```bash
sudo chage -l <username>
# Shows: Last change, Min/Max/Inactive/Warn days
```

### 2. Change Expired Password

```bash
# User changes own password
passwd

# Admin sets new password
sudo passwd <username>
```

### 3. Set Password to Never Expire

```bash
sudo chage -M -1 <username>
sudo passwd -x -1 <username>
```

### 4. Set Specific Expiration Policy

```bash
# Set max days to 90
sudo chage -M 90 <username>
# Set warning 7 days before expiry
sudo chage -W 7 <username>
```

## Examples

```bash
$ ssh jdoe@server
WARNING: Your password has expired.
Password change required but no TTY available.

$ sudo chage -l jdoe
Last password change                                    : Jan 01, 2025
Password expires                                        : Jul 01, 2025
Password inactive                                       : never
Account expires                                         : never
Minimum number of days between password change          : 0
Maximum number of days between password change          : 180
Number of days of warning before password expires       : 7

$ sudo passwd jdoe
New password: 
Retype new password: 
passwd: password updated successfully
```
