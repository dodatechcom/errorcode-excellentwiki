---
title: "[Solution] Linux: network-conntrack-full -- conntrack table full"
description: "Fix Linux connection tracking errors. Netfilter conntrack table full dropping packets."
os: ["linux"]
error-types: ["network-error"]
severities: ["error"]
---

# Linux: Connection Tracking Full

Connection tracking table overflow causes the kernel to drop new connection attempts.

## Common Causes

- conntrack_max too low for connection volume
- conntrack_tcp_timeout Established too long
- High connection rate from proxy or load balancer
- UDP timeout keeping entries too long
- DDoS or SYN flood exhausting conntrack

## How to Fix

### 1. Check Conntrack Usage

```bash
cat /proc/sys/net/netfilter/nf_conntrack_count
cat /proc/sys/net/netfilter/nf_conntrack_max
dmesg | grep "nf_conntrack: table full"
```

### 2. Increase Conntrack Limit

```bash
sudo sysctl -w net.netfilter.nf_conntrack_max=524288
echo "net.netfilter.nf_conntrack_max = 524288" | sudo tee /etc/sysctl.d/conntrack.conf
```

### 3. Reduce Timeouts

```bash
sudo sysctl -w net.netfilter.nf_conntrack_tcp_timeout_established=3600
sudo sysctl -w net.netfilter.nf_conntrack_udp_timeout=30
sudo sysctl -w net.netfilter.nf_conntrack_udp_timeout_stream=60
```

## Examples

```bash
$ cat /proc/sys/net/netfilter/nf_conntrack_count
262144
$ cat /proc/sys/net/netfilter/nf_conntrack_max
262144
# At 100% - connections will be dropped
$ dmesg | grep conntrack
[12345.678] nf_conntrack: table full, dropping packet
```
