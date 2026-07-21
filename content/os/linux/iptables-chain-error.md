---
title: "[Solution] Linux: iptables-chain-error -- chain reference error"
description: "Fix Linux iptables chain errors. Custom chain reference or jump target error in iptables."
os: ["linux"]
error-types: ["firewall-error"]
severities: ["error"]
---

# Linux: Iptables Chain Error

Iptables chain errors occur when custom chains are referenced before creation.

## Common Causes

- Jump to custom chain that does not exist
- Chain name exceeding 29 character limit
- Nested chain depth exceeding kernel limit
- RETURN target used in built-in chain incorrectly
- Chain flush while packets being processed

## How to Fix

### 1. Check Existing Chains

```bash
sudo iptables -L -n --line-numbers
sudo iptables -S | grep "^:"
```

### 2. Create Missing Chain

```bash
sudo iptables -N MYCHAIN
sudo iptables -A INPUT -j MYCHAIN
sudo iptables -A MYCHAIN -s 10.0.0.0/8 -j ACCEPT
```

### 3. Fix Chain References

```bash
sudo iptables -D INPUT -j NONEXISTENT
sudo iptables -N NONEXISTENT
sudo iptables -A NONEXISTENT -j RETURN
```

## Examples

```bash
$ sudo iptables -A INPUT -j MYCHAIN
iptables: No chain/target/match by that name.
$ sudo iptables -N MYCHAIN
$ sudo iptables -A INPUT -j MYCHAIN
```
