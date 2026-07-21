---
title: "[Solution] Ubuntu Server: ubuntu-kernel-panic-uncorrected-error"
description: "Fix Ubuntu ubuntu-kernel-panic-uncorrected-error. Uncorrected MCE causes panic."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel Panic Uncorrected Error

Uncorrected machine check exception causes kernel panic.

## Common Causes
- Uncorrectable memory ECC error
- CPU cache error
- Hardware degradation

## How to Fix
1. Check MCE logs
```bash
sudo mcelog --client
dmesg | grep -i "mce"
```
2. Check memory
```bash
sudo memtester 1G 1
```
3. Check ECC status
```bash
sudo edac-util -s
sudo edac-util -r
```

## Examples
```bash
$ sudo mcelog --client
Hardware Error. This is not a software problem.
```