---
title: "[Solution] macOS Handoff Error — Cannot Continue Activities Between Devices"
description: "Fix macOS Handoff not working: cannot start activity on iPhone and continue on Mac, Handoff icon missing from Dock."
platforms: ["macos"]
severities: ["error"]
error_types: ["runtime-error"]
weight: 121
---

# Handoff Error — Cannot Continue Activities Between Devices

Fix macOS Handoff not working: cannot start activity on iPhone and continue on Mac, Handoff icon missing from Dock.

## Common Causes

- Handoff not enabled on one or both Apple devices
- Bluetooth or Wi-Fi disabled preventing device discovery
- Both devices not signed into same Apple ID with iCloud
- Handoff feature not supported on older device or macOS version

## How to Fix

### 1. Enable Handoff on Mac and iOS Device

```bash
# Mac: System Settings → General → AirDrop & Handoff → Allow Handoff ON
# iPhone: Settings → General → AirPlay & Handoff → Handoff ON
defaults read com.apple.NetworkBrowser DisableHandoff
```

### 2. Ensure Bluetooth and Wi-Fi Are Active

```bash
networksetup -getairportnetwork en0
system_profiler SPBluetoothDataType | grep 'State'
networksetup -setairportpower en0 on
```

### 3. Sign Out and Back Into iCloud

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
```

### 4. Reset Bluetooth and Network Settings

```bash
sudo rm -f /Library/Preferences/com.apple.Bluetooth.plist
sudo rm -f /Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist
sudo shutdown -r now
```

## Common Scenarios

This error commonly occurs when:

- Handoff icon does not appear in Dock when browsing on iPhone
- Handoff works one direction but not the other
- Handoff stopped working after macOS or iOS update
- Handoff works for Safari but not for other apps like Mail or Notes

## Prevent It

- Keep both Mac and iOS devices signed into same Apple ID
- Ensure Bluetooth and Wi-Fi are always enabled on both devices
- Keep macOS and iOS updated to maintain Handoff compatibility
- Restart both devices periodically to refresh Handoff connection
