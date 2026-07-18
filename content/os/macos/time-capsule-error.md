---
title: "[Solution] macOS Time Capsule Error — Wireless Backup Device Not Found"
description: "Fix macOS Time Capsule connection error: Mac cannot find or connect to Time Capsule for wireless backup, AirPort Utility fails."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 114
---

# Time Capsule Error — Wireless Backup Device Not Found

Fix macOS Time Capsule connection error: Mac cannot find or connect to Time Capsule for wireless backup, AirPort Utility fails.

## Common Causes

- Time Capsule firmware outdated or incompatible with macOS version
- Wi-Fi network issue preventing discovery of Time Capsule
- Time Capsule hard drive failure preventing backup storage
- Bonjour service issue preventing device discovery on network

## How to Fix

### 1. Check Time Capsule Connection

```bash
ping 10.0.1.1
dns-sd -B _airport._tcp local.
open -a 'AirPort Utility'
```

### 2. Update Time Capsule Firmware

```bash
open -a 'AirPort Utility'
# Select Time Capsule → Check for firmware updates
# After update, restart Time Capsule by unplugging for 30s
```

### 3. Reset Network and Reconnect

```bash
s
u
d
o
 
r
m
 
-
f
 
/
L
i
b
r
a
r
y
/
P
r
e
f
e
r
e
n
c
e
s
/
S
y
s
t
e
m
C
o
n
f
i
g
u
r
a
t
i
o
n
/
c
o
m
.
a
p
p
l
e
.
a
i
r
p
o
r
t
.
p
r
e
f
e
r
e
n
c
e
s
.
p
l
i
s
t
```

### 4. Test Time Capsule Disk Health

```bash
# Open AirPort Utility → Select Time Capsule → Disks tab
# Check disk status and available space
```

## Common Scenarios

This error commonly occurs when:

- AirPort Utility cannot find Time Capsule on the network
- Time Machine backup to Time Capsule fails with 'disk not available'
- Time Capsule status light is amber indicating a problem
- Wireless backup speed is extremely slow or times out

## Prevent It

- Keep Time Capsule firmware updated through AirPort Utility
- Place Time Capsule centrally with good Wi-Fi signal to Mac
- Monitor Time Capsule disk space and clear old backups regularly
- Consider migrating to a NAS-based backup as Time Capsule is discontinued
