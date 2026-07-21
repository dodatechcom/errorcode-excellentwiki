---
title: "[Solution] Linux: locale-utf8-error -- locale UTF-8 encoding error"
description: "Fix Linux locale UTF-8 errors. Locale or UTF-8 encoding configuration failure."
os: ["linux"]
error-types: ["locale-error"]
severities: ["warning"]
---

# Linux: Locale UTF-8 Error

Locale UTF-8 errors cause character encoding issues and broken terminal display.

## Common Causes

- locale-gen not generating required locales
- LANG variable not set to UTF-8 locale
- Missing locale definition files
- SSH session inheriting non-UTF-8 locale
- Application requiring specific LC_CTYPE setting

## How to Fix

### 1. Check Current Locale

```bash
locale
locale -a
echo $LANG
```

### 2. Generate UTF-8 Locale

```bash
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### 3. Fix SSH Locale

```bash
# /etc/ssh/sshd_config
SendEnv LANG LC_*
# ~/.bashrc
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

## Examples

```bash
$ locale
LANG=
LANGUAGE=
LC_CTYPE="POSIX"
$ locale -a | grep en_US
en_US
en_US.iso88591
$ sudo locale-gen en_US.UTF-8
Generating locales...
  en_US.UTF-8... done
```
