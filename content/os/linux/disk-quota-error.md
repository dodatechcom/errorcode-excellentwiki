---
title: "[Solution] Linux: disk-quota-error — disk quota system error"
description: "Fix Linux disk-quota-error errors. disk quota system error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 6
---
# Linux: Quota Error

Quota errors occur when the disk quota subsystem cannot read or enforce user or group disk usage limits.

## Common Causes

- Quota database (aquota.user, aquota.group) missing or corrupted
- Filesystem mounted without quota support options
- Quota kernel module not loaded
- Quota limits configured incorrectly or inconsistently

## How to Fix

### 1. Check Quota Status

```bash
sudo quota -v
sudo repquota -a
```

### 2. Initialize Quota Files

```bash
sudo touch /aquota.user /aquota.group
sudo quotacheck -cugm /dev/sdX
```

### 3. Remount with Quota Options

```bash
sudo mount -o remount,usrquota,grpquota /dev/sdX
```

### 4. Enable Quotas

```bash
sudo quotaon -v /dev/sdX
```

## Examples

```bash
$ sudo repquota -a
** Reporting quotas for /dev/sda1
User ID  Used   Soft   Hard  Grace   Files  Soft  Hard  Grace
jdoe  123456 100000 120000  7days    1234     0     0
```
