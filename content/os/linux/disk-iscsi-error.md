---
title: "[Solution] Linux: disk-iscsi-error — iSCSI disk error"
description: "Fix Linux disk-iscsi-error errors. iSCSI disk error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 8
---
# Linux: iSCSI Error

iSCSI errors occur when connecting to or maintaining iSCSI storage targets over TCP/IP networks.

## Common Causes

- iSCSI target portal unreachable or incorrect IP/port
- CHAP authentication credentials incorrect or not configured
- iSCSI initiator name not authorized on the target
- Network issues causing session timeouts or connection drops
- LUN not mapped or accessible to the initiator

## How to Fix

### 1. Check iSCSI Sessions

```bash
sudo iscsiadm -m session
sudo iscsiadm -m session -P 3
```

### 2. Discover Targets

```bash
sudo iscsiadm -m discovery -t sendtargets -p <target_ip>
```

### 3. Login to Target

```bash
sudo iscsiadm -m node --loginall
```

### 4. Configure CHAP

```bash
sudo iscsiadm -m node -T <iqn> -p <target_ip> --op=update -n node.session.auth.authmethod -v CHAP
sudo iscsiadm -m node -T <iqn> -p <target_ip> --op=update -n node.session.auth.username -v <username>
sudo iscsiadm -m node -T <iqn> -p <target_ip> --op=update -n node.session.auth.password -v <password>
```

## Examples

```bash
$ sudo iscsiadm -m discovery -t sendtargets -p 192.168.1.100
192.168.1.100:3260,1 iqn.2024-01.com.example:storage.target01

$ sudo iscsiadm -m node --loginall
Logging in to [iface: default, target: iqn.2024-01.com.example:storage.target01, portal: 192.168.1.100,3260]
Login successful.
```
