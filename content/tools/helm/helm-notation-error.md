---
title: "[Solution] Helm Secrets Notation Decrypt Failed Error Fix"
description: "Fix helm secrets and notation decrypt failed errors. Resolve chart encryption and decryption issues with Helm secrets."
tools: ["helm"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Helm Secrets Notation Decrypt Failed Error Fix

The helm secrets or notation decrypt failed error occurs when Helm cannot decrypt encrypted values files or chart secrets during deployment.

## What This Error Means

Helm secrets (via helm-secrets plugin) encrypt sensitive values files. When decryption fails due to missing keys, wrong passwords, or corrupted files, the deployment fails.

A typical error:

```
Error: failed decoding secret: failed to decrypt: 
sops failed to decrypt: MAC mismatch
```

## Why It Happens

Common causes include:

- **Wrong decryption key** — GPG age key not available.
- **Corrupted secrets file** — File was modified after encryption.
- **Missing helm-secrets plugin** — Plugin not installed.
- **SOPS configuration wrong** — .sops.yaml misconfigured.
- **File encoding issues** — Secrets file has wrong encoding.
- **Age key mismatch** — Encrypted with different age key.

## How to Fix It

### Fix 1: Install helm-secrets plugin

```bash
# RIGHT: Install the plugin
helm plugin install https://github.com/jkroepke/helm-secrets

# Verify installation
helm plugin list
```

### Fix 2: Decrypt manually first

```bash
# RIGHT: Test decryption
sops -d secrets.yaml

# Or with age
sops --decrypt --age age1xxx secrets.yaml
```

### Fix 3: Check SOPS configuration

```yaml
# .sops.yaml
creation_rules:
  - path_regex: secrets\.yaml$
    age: age1xxx...
    # Or GPG
    pgp: FINGERPRINT
```

### Fix 4: Use helm secrets with template

```bash
# RIGHT: Template with secrets
helm secrets template myrelease mychart/ -f secrets.yaml

# Install with secrets
helm secrets upgrade --install myrelease mychart/ -f secrets.yaml
```

### Fix 5: Re-encrypt secrets file

```bash
# RIGHT: Re-encrypt after key change
sops updatekeys secrets.yaml

# Or re-encrypt entirely
sops -e secrets.yaml > secrets-encrypted.yaml
```

## Common Mistakes

- **Not having sops installed** — Required for encryption/decryption.
- **Using wrong key** — Ensure correct age/GPG key is available.
- **Committing decrypted secrets** — Never commit unencrypted secrets.

## Related Pages

- [Helm Render Error](helm-render-error) — Template rendering issues
- [Helm Schema Error](helm-schema-error) — Values schema issues
- [Helm Push Error](helm-push-error) — OCI push issues
