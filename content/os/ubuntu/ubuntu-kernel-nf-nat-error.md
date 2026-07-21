---
title: "[Solution] Ubuntu Server: ubuntu-kernel-nf-nat-error"
description: "Fix Ubuntu ubuntu-kernel-nf-nat-error. Netfilter NAT table errors."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel NF NAT Error

Netfilter NAT table encounters errors.

## Common Causes
- NAT table full
- conntrack entries exhausted
- Masquerade rule missing

## How to Fix
1. Check NAT table
```bash
sudo iptables -t nat -L -n -v
```
2. Check conntrack
```bash
cat /proc/sys/net/netfilter/nf_conntrack_count
cat /proc/sys/net/netfilter/nf_conntrack_max
```
3. Add masquerade rule
```bash
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

## Examples
```bash
$ sudo iptables -t nat -L -n -v
Chain POSTROUTING (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source  destination
    0     0 MASQUERADE  all  --  *      eth0    0.0.0.0/0   0.0.0.0/0
```