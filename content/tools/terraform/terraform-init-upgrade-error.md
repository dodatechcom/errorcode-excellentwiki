---
title: "[Solution] Terraform Init Upgrade Error"
description: "Fix Terraform init upgrade errors when upgrading providers or modules fails."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Init upgrade errors occur when upgrading dependencies during init:

```
Error: Failed to install provider

Error: could not download provider hashicorp/aws version 5.0.0
```

## Common Causes

- Network issues during download.
- Provider version no longer available.
- Corrupted cache.

## How to Fix

**Clear cache and retry:**

```bash
rm -rf .terraform/
terraform init -upgrade
```

**Force re-download:**

```bash
terraform init -upgrade -force-copy
```

**Check provider availability:**

```bash
curl -s "https://registry.terraform.io/v1/providers/hashicorp/aws/versions" | jq '.versions[].version' | head -5
```

## Examples

```bash
# Clean init
rm -rf .terraform .terraform.lock.hcl
terraform init -upgrade

# Verify providers installed
terraform providers
```
