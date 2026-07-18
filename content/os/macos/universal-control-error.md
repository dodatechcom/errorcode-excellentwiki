---
title: "[Solution] macOS Universal Control Error — Keyboard/Mouse Sharing Fails"
description: "Fix macOS Universal Control failure: cannot share keyboard and mouse between Mac and iPad, cursor does not move between displays."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 125
---

# Universal Control Error — Keyboard/Mouse Sharing Fails

Fix macOS Universal Control failure: cannot share keyboard and mouse between Mac and iPad, cursor does not move between displays.

## Common Causes

- Universal Control not enabled in System Settings
- Devices too far apart for Bluetooth Low Energy discovery
- iPad or Mac running incompatible software version
- Universal Control requires macOS Monterey 12.3 or later

## How to Fix

### 1. Enable Universal Control on Both Devices

```bash
# Mac: System Settings → Displays → Advanced → Enable all Universal Control options
# iPad: Settings → General → AirPlay & Handoff → Cursor and Keyboard ON
```

### 2. Position Displays Correctly

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
 
D
i
s
p
l
a
y
s
 
→
 
A
r
r
a
n
g
e
 
→
 
P
o
s
i
t
i
o
n
 
i
P
a
d
 
d
i
s
p
l
a
y
 
a
d
j
a
c
e
n
t
 
t
o
 
M
a
c
```

### 3. Fix Connection and Discovery Issues

```bash
# Ensure both devices within 10 feet of each other
# Restart both devices to refresh discovery
```

### 4. Update Software for Compatibility

```bash
softwareupdate -l
softwareupdate -i -a
# Update iPad to iPadOS 15.4 or later
```

## Common Scenarios

This error commonly occurs when:

- Cursor does not move from Mac display to adjacent iPad display
- Keyboard input not received by iPad when using Universal Control
- Universal Control worked initially but stopped after macOS update
- Cannot drag and drop files between Mac and iPad with Universal Control

## Prevent It

- Keep both Mac and iPad updated to latest compatible software versions
- Position Mac and iPad close to each other for reliable Universal Control
- Enable all Universal Control options in System Settings → Displays
- Restart both devices periodically to maintain Universal Control connection
