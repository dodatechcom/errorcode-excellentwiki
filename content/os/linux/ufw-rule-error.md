---
title: "[Solution] Linux: ufw-rule-error -- UFW rule error"
description: "Fix Linux UFW rule errors. UFW uncomplicated firewall rule syntax or application error."
os: ["linux"]
error-types: ["firewall-error"]
severities: ["error"]
---

# Linux: UFW Rule Error

UFW rule errors occur when Uncomplicated Firewall cannot parse or apply rules.

## Common Causes

- Invalid rule syntax or port specification
- Rule referring to non-existent application profile
- Rate limiting conflicting with allow rules
- UFW not managing iptables correctly
- Rule limit exceeding tracking entries

## How to Fix

### 1. Check UFW Status

```bash
sudo ufw status verbose
sudo ufw status numbered
```

### 2. Fix or Remove Rules

```bash
sudo ufw delete 3
sudo ufw delete allow 80/tcp
sudo ufw allow 80/tcp
sudo ufw --force reload
```

### 3. Reset and Rebuild

```bash
sudo ufw --force reset
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw enable
```

## Examples

```bash
$ sudo ufw status numbered
     To                         Action      From
[ 1] 22/tcp                     ALLOW IN    Anywhere
[ 2] 80                         ALLOW IN    Anywhere
[ 3] 443/tcp                    ALLOW IN    Anywhere
$ sudo ufw delete 2
Rule deleted
```
