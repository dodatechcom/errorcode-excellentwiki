---
title: "[Solution] Linux: locale-gen-error -- locale generation failure"
description: "Fix Linux locale-gen errors. Locale generation or compilation failure on Debian."
os: ["linux"]
error-types: ["locale-error"]
severities: ["warning"]
---

# Linux: Locale Generation Error

Locale-gen errors occur when the system fails to generate or compile locale data.

## Common Causes

- Missing locale source files in /etc/locale.gen
- Insufficient disk space in /usr/lib/locale
- locales package not installed
- locale.gen contains duplicate or invalid entries
- Post-install script failing to regenerate

## How to Fix

### 1. Check Current Locales

```bash
locale -a
cat /etc/locale.gen | grep -v "^#" | head -20
```

### 2. Enable and Generate

```bash
sudo sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
sudo locale-gen
sudo update-locale LANG=en_US.UTF-8
```

### 3. Reinstall Locales

```bash
sudo apt install --reinstall locales
sudo dpkg-reconfigure locales
```

## Examples

```bash
$ locale -a
C
POSIX
C.UTF-8
$ grep "en_US.UTF-8" /etc/locale.gen
# en_US.UTF-8 UTF-8
$ sudo sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
$ sudo locale-gen
Generating locales...
  en_US.UTF-8... done
```
