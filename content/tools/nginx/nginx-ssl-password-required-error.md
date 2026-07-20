---
title: "[Solution] Nginx SSL Password Required Error"
description: "The SSL private key file is encrypted and Nginx cannot read it without the passphrase."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The SSL private key file is encrypted and Nginx cannot read it without the passphrase.

## Common Causes

- **Key generated with passphrase** (e.g., `openssl genrsa -aes256`)
- **Key not decrypted** before placing in Nginx path
- **Wrong key file** that is still encrypted

## How to Fix

1. Remove passphrase: `openssl rsa -in encrypted.key -out decrypted.key`
2. Place decrypted key: `sudo mv decrypted.key /etc/ssl/private/server.key`
3. Restrict permissions: `sudo chmod 600 /etc/ssl/private/server.key`

## Examples

**Decrypt:**
```bash
cp server.key server.key.bak
openssl rsa -in server.key.bak -out server.key
chmod 600 server.key
```
**Verify not encrypted:**
```bash
head -1 server.key
# Should be: -----BEGIN PRIVATE KEY-----
```