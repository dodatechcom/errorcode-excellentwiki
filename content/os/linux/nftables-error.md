---
title: "[Solution] Linux: nftables-error — nftables error"
description: "Fix Linux nftables-error errors. nftables error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["network"]
weight: 10
---
# Linux: nftables Error

nftables errors occur when the new-generation Linux firewall fails to parse rules, apply configurations, or filter traffic correctly.

## Common Causes

- Syntax error in nftables ruleset file
- Table/chain/set already exists causing conflict
- Missing base chain hook for the protocol family
- nftables service not restarted after configuration change
- Kernel too old for the nftables features used

## How to Fix

### 1. Check nftables Status

```bash
sudo nft list ruleset
sudo systemctl status nftables
```

### 2. Validate Ruleset

```bash
sudo nft --check -f /etc/nftables.conf
```

### 3. Flush and Reload

```bash
sudo nft flush ruleset
sudo systemctl restart nftables
```

### 4. Add Rule

```bash
sudo nft add rule inet filter input tcp dport 80 accept
```

## Examples

```bash
$ sudo nft list ruleset
table inet filter {
        chain input {
                type filter hook input priority 0; policy drop;
                tcp dport 22 accept
        }
}

$ sudo nft add rule inet filter input tcp dport 80 accept
```
