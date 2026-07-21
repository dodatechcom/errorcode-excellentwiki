---
title: "Ubuntu APT Translation Error"
description: "APT fails to download package translations or language packs"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu APT Translation Error

APT fails to download package translations or language packs

## Common Causes

- Translation file (Translation-en) missing from repository
- Proxy blocking translation downloads
- Disk full preventing translation cache update
- Translation mirror out of sync

## How to Fix

1. Check languages: `apt-cache policy apt-translation-en`
2. Skip translations: `Acquire::Languages "none";` in apt.conf
3. Update: `sudo apt-get update`
4. Check disk: `df -h /var/lib/apt/lists/`

## Examples

```bash
# Disable translation downloads
echo 'Acquire::Languages "none";' | sudo tee /etc/apt/apt.conf.d/99no-languages

# Update package list
sudo apt-get update
```
