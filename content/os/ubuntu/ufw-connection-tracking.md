---
title: "UFW Connection Tracking Error"
description: "UFW connection tracking table full causing dropped connections"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# UFW Connection Tracking Error

UFW connection tracking table full causing dropped connections

## Common Causes

- nf_conntrack table size too small
- High traffic volume exhausting connection tracking
- Dropped connections due to conntrack timeout
- Multiple services creating many connections

## How to Fix

1. Check conntrack: `sudo conntrack -C`
2. Increase table size: `sysctl -w net.netfilter.nf_conntrack_max=262144`
3. Check timeouts: `sysctl net.netfilter.nf_conntrack_tcp_timeout_established`
4. Monitor: `sudo conntrack -L | wc -l`

## Examples

```bash
# Check conntrack count
sudo conntrack -C

# Increase conntrack table size
sudo sysctl -w net.netfilter.nf_conntrack_max=262144

# Make persistent
echo 'net.netfilter.nf_conntrack_max=262144' | sudo tee -a /etc/sysctl.conf
```
