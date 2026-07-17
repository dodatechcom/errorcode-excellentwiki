---
title: "[Solution] Linux ENOTUNIQ (errno 55) — Name Not Unique on Network Fix"
description: "Fix Linux ENOTUNIQ (errno 55) Name not unique on network error. Solutions for duplicate network name issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENOTUNIQ (errno 55) — Name Not Unique on Network

ENOTUNIQ (errno 55) means the name is not unique on the network. This error occurs when a program tries to register a network name (such as a hostname or service name) that is already in use by another machine on the network. It is distinct from EADDRINUSE (errno 98) because ENOTUNIQ specifically refers to name uniqueness, not address port binding.

## Common Causes

- Duplicate hostname configured on the network
- Attempting to bind to a network service name already in use
- Conflicting NetBIOS or mDNS names
- DHCP server assigned duplicate names

## How to Fix ENOTUNIQ

### 1. Check Current Hostname

Verify the system hostname:

```bash
hostname
hostname -f
cat /etc/hostname
```

### 2. Find Duplicate Names on Network

Scan for duplicate hostnames:

```bash
nmap -sn 192.168.1.0/24 | grep -i "hostname"
```

### 3. Change the Hostname

Set a unique hostname:

```bash
sudo hostnamectl set-hostname unique-hostname
```

### 4. Check mDNS Conflicts

If using Avahi/mDNS, check for name conflicts:

```bash
avahi-browse -a
avahi-daemon --check
```

### 5. Restart Networking

Apply the new hostname:

```bash
sudo systemctl restart networking
sudo systemctl restart avahi-daemon
```

## Verification

After changing the hostname, confirm uniqueness:

```bash
ping unique-hostname
avahi-browse -a | grep unique-hostname
```

## Related Error Codes

- [EADDRINUSE (errno 98)](/os/linux/errno-98/) — Address already in use
- [EHOSTUNREACH (errno 77)](/os/linux/errno-77/) — No route to host
- [ENETUNREACH (errno 65)](/os/linux/errno-65/) — Network is unreachable
