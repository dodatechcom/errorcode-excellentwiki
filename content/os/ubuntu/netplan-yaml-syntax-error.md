---
title: "[Solution] Ubuntu Server: netplan-yaml-syntax-error"
description: "Fix Ubuntu netplan-yaml-syntax-error. Netplan YAML configuration file has syntax errors."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Netplan YAML Syntax Error

netplan rejects the network configuration due to YAML syntax errors.

## Common Causes
- Incorrect indentation (must use spaces not tabs)
- Missing colon after key name
- Incorrect quoting of values
- Missing required fields

## How to Fix
1. Validate YAML syntax
```bash
sudo netplan generate
```
2. Check with linter
```bash
pip3 install yamllint
yamllint /etc/netplan/*.yaml
```
3. Fix indentation
```bash
sudo nano /etc/netplan/00-installer-config.yaml
# Use 2 spaces for each level
```

## Examples
```bash
$ sudo netplan generate
/etc/netplan/01-network.yaml:5:1: Error in network definition

network:
  version: 2
  ethernets:
    eth0:    <-- missing indent
      dhcp4: true
```
