---
title: "[Solution] Linux: firewall-rule-conflict -- rule conflict"
description: "Fix Linux firewall rule conflict errors. Conflicting iptables or nftables rules blocking traffic."
os: ["linux"]
error-types: ["firewall-error"]
severities: ["error"]
---

# Linux: Firewall Rule Conflict

Firewall rule conflicts occur when overlapping or contradictory rules block traffic.

## Common Causes

- iptables and nftables running simultaneously
- firewalld and iptables conflicting rules
- ACCEPT rule after DROP rule never reached
- NAT and filter rules in wrong table
- Rule ordering causing unexpected behavior

## How to Fix

### 1. Check Active Rulesets

```bash
sudo iptables -L -n -v --line-numbers
sudo nft list ruleset
sudo firewall-cmd --list-all-zones
```

### 2. Identify Conflicts

```bash
sudo iptables -L INPUT -n -v --line-numbers
sudo iptables -S | grep -E "DROP|REJECT" | head -20
```

### 3. Fix Rule Order

```bash
sudo iptables -D INPUT 3
sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT
```

## Examples

```bash
$ sudo iptables -L INPUT -n --line-numbers
num  target     prot opt source     destination
1    ACCEPT     tcp  --  0.0.0.0/0  0.0.0.0/0  tcp dpt:22
2    DROP       all  --  0.0.0.0/0  0.0.0.0/0
3    ACCEPT     tcp  --  0.0.0.0/0  0.0.0.0/0  tcp dpt:443
# Rule 3 unreachable due to rule 2 DROP
```
