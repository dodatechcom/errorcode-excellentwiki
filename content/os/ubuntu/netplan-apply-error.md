---
title: "[Solution] Ubuntu Server: netplan-apply-error"
description: "Fix Ubuntu netplan-apply-error. netplan apply command fails to activate configuration."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan Apply Error

netplan apply fails to activate the network configuration.

## Common Causes
- YAML syntax error in netplan config
- Renderer service not running
- Permission denied on netplan files
- Conflicting configuration

## How to Fix
1. Check netplan output
```bash
sudo netplan apply 2>&1
```
2. Validate first
```bash
sudo netplan generate
```
3. Try with --debug flag
```bash
sudo netplan --debug apply
```

## Examples
```bash
$ sudo netplan apply
** (process 12345) **: 10:00:00.000: Error in network definition: invalid YAML
failed to apply configuration: exit
