---
title: "[Solution] Terraform Provider Checksum Mismatch"
description: "Fix Terraform provider checksum mismatch errors when downloaded provider binary fails verification."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Checksum mismatch errors indicate the downloaded binary does not match expected:

```
Error: Failed to install provider

Error: checksum for registry.terraform.io/hashicorp/aws/5.31.0/linux_amd64
did not match expected value
```

## Common Causes

- Incomplete or corrupted download.
- MITM proxy altering the downloaded binary.
- Network interruption during download.

## How to Fix

**Clear cache and re-download:**

```bash
rm -rf ~/.terraform.d/plugin-cache/registry.terraform.io/hashicorp/
terraform init -upgrade
```

**Check proxy/SSL:**

```bash
unset HTTPS_PROXY
terraform init
```

**Lock provider checksums:**

```bash
terraform providers lock -platform=linux_amd64 -platform=darwin_amd64
```

## Examples

```bash
rm -rf .terraform/
terraform init -upgrade
```
