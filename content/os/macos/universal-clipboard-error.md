---
title: "[Solution] macOS Universal Clipboard Error — Copy Paste Between Devices Fails"
description: "Fix macOS Universal Clipboard not working: cannot copy on iPhone and paste on Mac, clipboard sync fails between devices."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 123
---

# Universal Clipboard Error — Copy Paste Between Devices Fails

Fix macOS Universal Clipboard not working: cannot copy on iPhone and paste on Mac, clipboard sync fails between devices.

## Common Causes

- Handoff not enabled which Universal Clipboard depends on
- Bluetooth or Wi-Fi disabled preventing clipboard transfer
- Clipboard daemon not running or crashed on either device
- Both devices not signed into same Apple ID

## How to Fix

### 1. Verify Universal Clipboard Prerequisites

```bash
defaults read com.apple.NetworkBrowser DisableHandoff
defaults read /Library/Preferences/com.apple.Bluetooth BluetoothPower
networksetup -getairportnetwork en0
```

### 2. Restart Clipboard Services

```bash
killall pbcopy
killall pbpaste
sudo killall -HUP bluetoothd
killall sharingd
```

### 3. Reset Bluetooth Connection

```bash
#
 
M
a
c
:
 
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
 
B
l
u
e
t
o
o
t
h
 
→
 
F
o
r
g
e
t
 
T
h
i
s
 
D
e
v
i
c
e
 
f
o
r
 
i
P
h
o
n
e
 
→
 
R
e
-
p
a
i
r
```

### 4. Sign Out and Back Into iCloud

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
 
S
i
g
n
 
O
u
t
 
→
 
K
e
e
p
 
K
e
y
c
h
a
i
n
 
C
o
p
y
 
→
 
S
i
g
n
 
I
n
 
o
n
 
b
o
t
h
 
d
e
v
i
c
e
s
```

## Common Scenarios

This error commonly occurs when:

- Copying text on iPhone shows 'No Pasteboard' when pasting on Mac
- Universal Clipboard works for text but not images or files
- Paste from iPhone appears on Mac but content is empty
- Universal Clipboard stopped working after updating to new macOS version

## Prevent It

- Keep Handoff enabled on all Apple devices you want to copy between
- Ensure Bluetooth and Wi-Fi are always enabled on both devices
- Restart both Mac and iPhone if Universal Clipboard stops working
- Keep macOS and iOS updated for Universal Clipboard improvements
