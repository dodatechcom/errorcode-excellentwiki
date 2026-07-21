---
title: "Libvirtd Service Error"
description: "libvirtd service fails to start or respond to requests"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Libvirtd Service Error

libvirtd service fails to start or respond to requests

## Common Causes

- Certificate authentication mismatch
- TLS certificates expired or not generated
- Socket permission denied
- Configuration syntax error in /etc/libvirt/

## How to Fix

1. Check libvirtd status: `systemctl status libvirtd`
2. Verify certificates: `ls -la /etc/pki/libvirt/`
3. Check config syntax: `virsh net-define /dev/null` to test parser
4. Restart with debug: `sudo libvirtd -d --verbose`

## Examples

```bash
# Check libvirtd status
systemctl status libvirtd

# Generate new certificates
sudo virt-pki-validate

# Restart libvirtd
sudo systemctl restart libvirtd
```
