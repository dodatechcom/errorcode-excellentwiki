---
title: "[Solution] Linux: firewall-error — firewall configuration error"
description: "Fix Linux firewall-error errors. firewall configuration error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 8
---
# Linux: Firewall Error

Firewall errors occur when iptables, nftables, firewalld, or ufw rules block legitimate network traffic.

## Common Causes

- Firewall rule blocking incoming connections on the required port
- Rule ordering issue (deny before allow)
- Stateful firewall not tracking connection state correctly
- Firewall service (firewalld/ufw) not running or misconfigured
- Rate limiting causing legitimate traffic to be dropped

## How to Fix

### 1. Check Current Rules

```bash
# iptables
sudo iptables -L -n -v
sudo iptables -t nat -L -n -v

# nftables
sudo nft list ruleset

# firewalld
sudo firewall-cmd --list-all

# ufw
sudo ufw status verbose
```

### 2. Check Firewall Logs

```bash
sudo dmesg | grep -i "DROP\|REJECT\|IN="
sudo journalctl -k | grep -i "DROP\|REJECT"
```

### 3. Allow a Port

```bash
# ufw
sudo ufw allow 8080/tcp

# firewalld
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload

# iptables
sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
```

### 4. Save Rules

```bash
# iptables-persistent
sudo netfilter-persistent save

# firewalld rules are auto-saved
```

## Examples

```bash
$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
443/tcp                    ALLOW       Anywhere
8080                       DENY        Anywhere

$ sudo ufw allow 8080/tcp
Rule added
Rule added (v6)
```
