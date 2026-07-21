---
title: "[Solution] Linux: firewalld-zone-error -- zone assignment error"
description: "Fix Linux firewalld zone errors. Zone assignment conflict in firewalld configuration."
os: ["linux"]
error-types: ["firewall-error"]
severities: ["error"]
---

# Linux: Firewalld Zone Error

Firewalld zone errors occur when interfaces cannot be assigned to zones.

## Common Causes

- Interface already assigned to different zone
- Default zone changed but interface not reassigned
- Source address conflicting with zone assignment
- Zone services not properly enabled
- Backend switching between iptables and nftables

## How to Fix

### 1. Check Zone Assignments

```bash
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --list-all
sudo firewall-cmd --list-all-zones
```

### 2. Fix Zone Assignment

```bash
sudo firewall-cmd --zone=public --change-interface=eth0 --permanent
sudo firewall-cmd --zone=trusted --add-source=192.168.1.0/24 --permanent
sudo firewall-cmd --reload
```

### 3. Verify Configuration

```bash
sudo firewall-cmd --get-zone-of-interface=eth0
sudo firewall-cmd --info-zone=public
```

## Examples

```bash
$ sudo firewall-cmd --get-active-zones
public
  interfaces: eth0
$ sudo firewall-cmd --zone=internal --change-interface=eth0
Error: ALREADY_ENABLED: eth0
```
