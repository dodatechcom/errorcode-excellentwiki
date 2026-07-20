---
title: "[Solution] Terraform Provider Initialization Failed"
description: "Fix Terraform provider initialization failed errors during terraform init."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Provider initialization fails when Terraform downloads the provider but cannot set it up:

```
Error: Failed to install provider

Error: failed to verify package signature for
"registry.terraform.io/hashicorp/aws": openpgp: signature verification failed
```

## Common Causes

- Corrupted provider download cache.
- Checksum verification failure.
- Insufficient disk space in the plugin directory.
- Antivirus software quarantining the binary.

## How to Fix

**Clear the provider cache and reinitialize:**

```bash
rm -rf .terraform/
terraform init
```

**Force re-download:**

```bash
terraform init -upgrade -force-copy
```

**Check disk space:**

```bash
df -h ~/.terraform.d/plugin-cache
```

## Examples

```bash
rm -rf .terraform .terraform.lock.hcl
terraform init -upgrade
terraform providers
```
