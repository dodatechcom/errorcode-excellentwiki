---
title: "[Solution] Ubuntu Server: apache-modsecurity-error"
description: "Fix Ubuntu apache-modsecurity-error. Apache ModSecurity WAF blocks legitimate requests."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apache ModSecurity Error

ModSecurity WAF blocks legitimate requests.

## Common Causes
- Rule too strict
- CRS false positives
- SecRuleEngine set to On
- Missing SecRequestBodyAccess

## How to Fix
1. Check ModSecurity status
```bash
sudo apache2ctl -M | grep security
```
2. Set detection only mode
```bash
sudo nano /etc/modsecurity/modsecurity.conf
SecRuleEngine DetectionOnly
```
3. Disable specific rule
```bash
# Add to modsecurity config:
SecRuleRemoveById 941100
```

## Examples
```bash
$ sudo apache2ctl -M | grep security
 security2_module (shared)
```