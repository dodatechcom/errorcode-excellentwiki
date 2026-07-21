---
title: "[Solution] Ubuntu Server: snap-snap-conflict"
description: "Fix Ubuntu snap-snap-conflict. Two snap packages conflict and cannot coexist."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Snap Snap Conflict

Two snap packages have conflicting configurations or files.

## Common Causes
- Both snaps trying to use same port
- Conflicting AppArmor profiles
- Shared mount namespace conflict
- Both snaps binding same socket

## How to Fix
1. Check snap connections
```bash
snap connections <snap1>
snap connections <snap2>
```
2. Remove conflicting snap
```bash
sudo snap remove <conflicting-snap>
```
3. Reconfigure to use different ports
```bash
sudo snap set <snap1> port=8080
sudo snap set <snap2> port=8081
```

## Examples
```bash
$ sudo snap install nextcloud
error: snap "nextcloud" has conflicts with "apache2"

$ snap connections nextcloud
Interface  Slot    Notes
network    :network -
```
