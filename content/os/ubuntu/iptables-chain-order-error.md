---
title: "[Solution] Ubuntu Server: iptables-chain-order-error"
description: "Fix Ubuntu iptables-chain-order-error. iptables chain order causes rules to be skipped."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Iptables Chain Order Error

iptables rules are in wrong order and get skipped.

## Common Causes
- ACCEPT rule before DROP rule
- Custom chain not referenced from INPUT
- RETURN at end of chain too early
- Jump to wrong chain

## How to Fix
1. Check chain order
```bash
sudo iptables -L -n -v --line-numbers
```
2. Insert rule at correct position
```bash
sudo iptables -I INPUT 1 -s 192.168.1.0/24 -j ACCEPT
```
3. Remove and re-add in correct order
```bash
sudo iptables -D INPUT -j DROP
sudo iptables -I INPUT 5 -j DROP
```

## Examples
```bash
$ sudo iptables -L INPUT -n -v --line-numbers
num   pkts bytes target  prot opt in     out     source         destination
1        0     0 DROP    all  --  *      *       0.0.0.0/0      0.0.0.0/0
2      100  5000 ACCEPT  tcp  --  eth0   *       0.0.0.0/0      0.0.0.0/0  tcp dpt:22
# Rule 2 never reached!
```
