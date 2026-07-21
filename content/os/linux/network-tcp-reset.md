---
title: "[Solution] Linux: network-tcp-reset -- unexpected TCP RST"
description: "Fix Linux network TCP reset errors. Unexpected TCP RST packet causing connection drops."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Network TCP Reset

Unexpected TCP RST packets cause connections to terminate abruptly.

## Common Causes

- Firewall rules sending RST for blocked ports
- Service crashing and closing socket without FIN
- Connection tracking table full in netfilter
- NAT translation timing out incorrectly
- Load balancer rejecting new connections

## How to Fix

### 1. Capture RST Packets

```bash
sudo tcpdump -i eth0 "tcp[tcpflags] & (tcp-rst) != 0" -c 20
sudo ss -tlnp
```

### 2. Check Firewall Rules

```bash
sudo iptables -L -n -v | grep -i reject
sudo nft list ruleset | grep -i reject
```

### 3. Adjust Connection Tracking

```bash
sudo sysctl net.netfilter.nf_conntrack_max=262144
sudo sysctl net.netfilter.nf_conntrack_tcp_timeout_time_wait=30
```

## Examples

```bash
$ sudo tcpdump -i eth0 "tcp[tcpflags] & (tcp-rst) != 0" -c 5
14:00:01 IP 192.168.1.50.443 > 192.168.1.100.54321: Flags [R], seq 0, win 0
$ sudo iptables -L INPUT -n | grep REJECT
REJECT  tcp  --  0.0.0.0/0  0.0.0.0/0  tcp dpt:80 reject-with tcp-reset
```
