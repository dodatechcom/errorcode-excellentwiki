---
title: "[Solution] Ubuntu Server: lxd-images-error"
description: "Fix Ubuntu lxd-images-error. LXD image download or import fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# LXD Images Error

LXD image download or import operations fail.

## Common Causes
- Image server unreachable
- Image alias does not exist
- Disk space insufficient for image

## How to Fix
1. Check available images
```bash
lxc image list ubuntu: jammy
```
2. Download image
```bash
lxc image copy ubuntu:22.04 local: --alias myimage
```
3. Check image storage
```bash
lxc storage info default
```

## Examples
```bash
$ lxc image copy ubuntu:22.04 local: --alias myimage
Retrieving image: 100%
```