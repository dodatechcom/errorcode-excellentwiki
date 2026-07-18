---
title: "[Solution] macOS iCloud Keychain Error — Password Sync Failure"
description: "Fix macOS iCloud Keychain sync error: passwords and certificates not syncing between Apple devices, keychain locked or inaccessible."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 119
---

# iCloud Keychain Error — Password Sync Failure

Fix macOS iCloud Keychain sync error: passwords and certificates not syncing between Apple devices, keychain locked or inaccessible.

## Common Causes

- iCloud Keychain not enabled on one or more devices
- Keychain authentication token expired or corrupted
- Two-factor authentication preventing keychain sync
- Keychain database corruption on local device

## How to Fix

### 1. Check iCloud Keychain Status

```bash
defaults read com.apple.security | grep -i keychain
security dump-keychain -d login
log show --predicate 'process == "securityd"' --last 1h | head -20
```

### 2. Reset iCloud Keychain

```bash
#
 
S
y
s
t
e
m
 
S
e
t
t
i
n
g
s
 
→
 
A
p
p
l
e
 
I
D
 
→
 
i
C
l
o
u
d
 
→
 
T
o
g
g
l
e
 
K
e
y
c
h
a
i
n
 
o
f
f
/
o
n
```

### 3. Approve Keychain on All Devices

```bash
security find-identity -v -p codesigning
security find-certificate -a -c 'iCloud' -Z
```

### 4. Rebuild Local Keychain Database

```bash
security default-keychain -s login.keychain-db
# System Settings → Apple ID → iCloud → Keychain → Toggle off then on
```

## Common Scenarios

This error commonly occurs when:

- Passwords saved on iPhone do not appear in Safari on Mac
- Keychain shows 'locked' message when trying to access saved passwords
- iCloud Keychain keeps asking for approval on previously approved devices
- Certificate-based keychain items not syncing between Mac and iPhone

## Prevent It

- Keep all Apple devices signed into the same Apple ID for keychain sync
- Approve keychain sync prompts promptly on new or updated devices
- Use two-factor authentication for Apple ID security with keychain
- Regularly back up keychain items using Keychain Access export feature
