---
title: "[Solution] MongoDB msync Failed Error"
description: "Fix MongoDB msync and disk sync failures"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB msync Failed Error

```
WiredTiger error: msync: Input/output error
```

```
WiredTiger error: fsync: Input/output error
```

## Common Causes

- The disk has hardware errors
- The filesystem is corrupted
- The disk is full
- I/O controller errors
- The journal files are corrupted

## How to Fix

### 1. Check disk health

```bash
sudo smartctl -a /dev/sda
dmesg | grep -i error
```

### 2. Check filesystem integrity

```bash
sudo fsck /dev/sda1
```

### 3. Repair the database

```bash
# Stop MongoDB first
sudo systemctl stop mongod

# Run mongod with --repair
sudo mongod --repair --dbpath /var/lib/mongodb

# Start MongoDB
sudo systemctl start mongod
```

### 4. Replace the disk if hardware failure is detected

```bash
# Check for I/O errors
dmesg | tail -50
smartctl -l error /dev/sda
```

## Examples

```bash
# Check disk errors
dmesg | grep -i "error\|fail\|bad"

# Check smart status
sudo smartctl -H /dev/sda

# Check filesystem
sudo fsck -n /dev/sda1
```