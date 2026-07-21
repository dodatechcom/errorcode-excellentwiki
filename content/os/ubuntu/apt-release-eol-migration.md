---
title: "[Solution] Ubuntu Server: apt-release-eol-migration"
description: "Fix Ubuntu apt-release-eol-migration. Ubuntu release has reached end of life and needs migration."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Release EOL Migration

The Ubuntu release has reached end of life and packages can no longer be fetched from main mirrors.

## Common Causes
- Running an Ubuntu version past its support date
- LTS support expired for the release
- Mirror no longer serving the release
- Upgraded past supported version

## How to Fix
1. Check current release
```bash
lsb_release -a
```
2. Migrate to old-releases mirrors
```bash
sudo sed -i s
