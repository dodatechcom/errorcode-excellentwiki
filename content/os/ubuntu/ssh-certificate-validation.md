---
title: "SSH Certificate Validation Error"
description: "SSH client rejects host certificate or user certificate validation fails"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# SSH Certificate Validation Error

SSH client rejects host certificate or user certificate validation fails

## Common Causes

- Host certificate not signed by trusted CA
- Certificate has expired
- Certificate principals do not match
- Known hosts file contains conflicting entry

## How to Fix

1. Verify certificate: `ssh-keygen -L -f /path/to/cert`
2. Add CA to trusted certificates: `@cert-authority *.example.com ssh-rsa AAAA...`
3. Remove conflicting known_hosts entry
4. Check certificate validity dates

## Examples

```bash
# Verify a certificate
ssh-keygen -L -f /etc/ssh/ssh_host_rsa_key-cert.pub

# Add CA to known_hosts
echo '@cert-authority *.example.com ssh-rsa AAAA...' >> ~/.ssh/known_hosts
```
