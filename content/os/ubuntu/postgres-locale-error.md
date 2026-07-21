---
title: "PostgreSQL Locale Configuration Error"
description: "PostgreSQL cannot initialize with specified locale"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PostgreSQL Locale Configuration Error

PostgreSQL cannot initialize with specified locale

## Common Causes

- Locale not installed on the system
- Invalid locale name in initdb
- LC_COLLATE and LC_CTYPE mismatch
- UTF-8 locale not available

## How to Fix

1. Check locales: `locale -a`
2. Install locale: `sudo locale-gen en_US.UTF-8`
3. Use C.UTF-8 as fallback: initdb with --encoding=UTF-8 --locale=C.UTF-8
4. Set default: `sudo update-locale LANG=en_US.UTF-8`

## Examples

```bash
# Check available locales
locale -a | grep en_US

# Generate locale
sudo locale-gen en_US.UTF-8

# Initialize PostgreSQL with specific locale
sudo -u postgres initdb -D /var/lib/postgresql/data --encoding=UTF-8 --locale=en_US.UTF-8
```
