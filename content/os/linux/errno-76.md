---
title: "[Solution] Linux EHOSTDOWN (errno 76) — Host Is Down Fix"
description: "Fix Linux EHOSTDOWN (errno 76) Host is down error. Solutions for unreachable host and availability issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["ehostdown", "host", "errno-76", "down", "unreachable"]
weight: 5
---

# Linux EHOSTDOWN (errno 76) — Host Is Down

EHOSTDOWN (errno 76) means the target host is currently down or unavailable. This error occurs when the system determines that a remote host is not operational, typically because ARP resolution fails or the host is not responding to network probes. It is distinct from EHOSTUNREACH (errno 77) because EHOSTDOWN indicates the host is known but not responding, while EHOSTUNREACH means no route exists to the host.

## Common Causes

- Remote host has been powered off or crashed
- Network interface on the remote host is down
- Host is in a network partition and unreachable
- Virtual machine is suspended or halted

## How to Fix EHOSTDOWN

### 1. Check Host Reachability

Test if the host responds to network probes:

```bash
ping -c 3 host.example.com
arp -n host.example.com
```

### 2. Verify Host Status

Check if the host is operational:

```bash
# Check if it's a VM
virsh list --all
```

### 3. Check ARP Table

Verify the MAC address mapping:

```bash
arp -n | grep host_ip
ip neigh show
```

### 4. Power On the Host

If the host is powered off, power it on:

```bash
# For IPMI/BMC managed hosts
ipmitool -H bmc.example.com -U admin -P password power on
```

### 5. Check Network Path

Verify the network path to the host:

```bash
traceroute host.example.com
mtr host.example.com
```

## Verification

After restoring the host, confirm connectivity:

```bash
ping host.example.com
ssh host.example.com
```

## Related Error Codes

- [EHOSTUNREACH (errno 77)](/os/linux/errno-77/) — No route to host
- [ETIMEDOUT (errno 74)](/os/linux/errno-74/) — Connection timed out
- [ENETUNREACH (errno 65)](/os/linux/errno-65/) — Network is unreachable
