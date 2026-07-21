---
title: "[Solution] Ubuntu Server: snap-confinement-error"
description: "Fix Ubuntu snap-confinement-error. snap confinement rules block required operations."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Snap Confinement Error

snap package fails because confinement rules block operations.

## Common Causes
- AppArmor profile blocking snap
- Interface not connected
- Classic confinement not supported
- Missing plug/slot connection

## How to Fix
1. Check confinement and interfaces
```bash
snap info <package>
snap interfaces
```
2. Connect required interfaces
```bash
sudo snap connect <package>:<interface>
```
3. Install with --classic if available
```bash
sudo snap install <package> --classic
```

## Examples
```bash
$ snap info docker
confinement: strict

$ sudo snap connect docker:docker-support
```
