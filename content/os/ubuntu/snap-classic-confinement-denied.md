---
title: "[Solution] Ubuntu Server: snap-classic-confinement-denied"
description: "Fix Ubuntu snap-classic-confinement-denied. Classic confinement denied during snap install."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Snap Classic Confinement Denied

snap install fails because classic confinement is not allowed.

## Common Causes
- Snap does not support classic confinement
- snapd configuration blocks classic
- AppArmor not configured for classic snaps
- PolicyKit denying classic install

## How to Fix
1. Check if snap supports classic
```bash
snap info <package> | grep confinement
```
2. Override confinement if needed
```bash
sudo snap install <package> --classic --dangerous
```
3. Configure snapd for classic
```bash
sudo nano /etc/snapd/snapd.conf
# Add: classic-snaps: true
sudo systemctl restart snapd
```

## Examples
```bash
$ sudo snap install --classic code
error: This snap requires classic confinement

$ snap info code
confinement: classic
```
