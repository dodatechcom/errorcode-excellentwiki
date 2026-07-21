---
title: "[Solution] Ubuntu Server: ubuntu-kernel-nf-conntrack-error"
description: "Fix Ubuntu ubuntu-kernel-nf-conntrack-error. Netfilter connection tracking table full."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel NF Conntrack Error

Netfilter connection tracking table is full.

## Common Causes
- conntrack_max too low
- Too many concurrent connections
- DDoS or connection flood

## How to Fix
1. Check conntrack usage
```bash
cat /proc/sys/net/netfilter/nf_conntrack_count
cat /proc/sys/net/netfilter/nf_conntrack_max
```
2. Increase max
```bash
echo 262144 | sudo tee /proc/sys/net/netfilter/nf_conntrack_max
```
3. Make persistent
```bash
echo 'net.netfilter.nf_conntrack_max=262144' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

## Examples
```bash
$ cat /proc/sys/net/netfilter/nf_conntrack_count
262140

$ cat /proc/sys/net/netfilter/nf_conntrack_max
262144
```