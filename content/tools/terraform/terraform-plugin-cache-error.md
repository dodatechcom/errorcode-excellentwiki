---
title: "[Solution] Terraform Plugin Cache Error"
description: "Fix Terraform plugin cache errors when the local provider cache is corrupted or inaccessible."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Plugin cache errors occur when Terraform cannot read or write its plugin cache:

```
Error: Failed to install provider

Error: open /home/user/.terraform.d/plugin-cache/.../linux_amd64:
permission denied
```

## Common Causes

- Permission issues on the cache directory.
- Corrupted cache entries from interrupted downloads.
- Multiple Terraform processes writing to cache simultaneously.

## How to Fix

**Fix permissions:**

```bash
chmod -R u+rw ~/.terraform.d/plugin-cache
```

**Clear and rebuild the cache:**

```bash
rm -rf ~/.terraform.d/plugin-cache
terraform init
```

**Set custom cache directory:**

```bash
export TF_PLUGIN_CACHE_DIR="/opt/terraform/cache"
terraform init
```

## Examples

```bash
ls -la ~/.terraform.d/plugin-cache/
export TF_PLUGIN_CACHE_DIR=""
terraform init
```
