---
title: "[Solution] macOS iCloud Sync Error — Data Not Updating Between Devices"
description: "Fix macOS iCloud sync failure: data not updating between Mac and iPhone, contacts or calendars out of sync, iCloud data stale."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 117
---

# iCloud Sync Error — Data Not Updating Between Devices

Fix macOS iCloud sync failure: data not updating between Mac and iPhone, contacts or calendars out of sync, iCloud data stale.

## Common Causes

- iCloud sync daemon (cloudd) experiencing authentication issue
- Network firewall or proxy blocking iCloud sync connections
- Corrupted local database for synced data like contacts
- Apple ID requiring re-authentication due to security event

## How to Fix

### 1. Check iCloud Sync Services

```bash
defaults read MobileMeAccounts | grep -A 20 'EnabledServices'
ps aux | grep -i 'cloudd\|bird\|nsurlsessiond'
log show --predicate 'process == "cloudd"' --last 5m | head -20
```

### 2. Toggle iCloud Services Off and On

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
 
o
f
f
 
a
f
f
e
c
t
e
d
 
s
e
r
v
i
c
e
 
→
 
T
o
g
g
l
e
 
o
n
```

### 3. Reset CloudKit and Sync Databases

```bash
rm -rf ~/Library/Caches/CloudKit/*
killall cloudd
killall nsurlsessiond
# Restart Mac and sign back into iCloud
```

### 4. Verify Network and Firewall Settings

```bash
curl -I https://setup.icloud.com
networksetup -getwebproxy Wi-Fi
networksetup -getsecurewebproxy Wi-Fi
```

## Common Scenarios

This error commonly occurs when:

- Contacts updated on iPhone do not appear on Mac after hours
- Calendar events created on Mac are missing from iPhone
- Safari bookmarks and reading list are different across devices
- iCloud Photos not uploading new pictures from iPhone to Mac

## Prevent It

- Sign out and back into iCloud annually to refresh authentication tokens
- Keep stable internet connection when syncing important data
- Ensure all devices are signed into the same Apple ID
- Update macOS and iOS to maintain iCloud service compatibility
