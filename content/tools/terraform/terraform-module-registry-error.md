---
title: "[Solution] Terraform Module Registry Error"
description: "Fix Terraform module registry errors when accessing modules from a private registry."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module registry errors occur when Terraform cannot access the registry:

```
Error: Failed to download module

Error: could not download module from
"registry.terraform.io/my-org/module": 401 Unauthorized
```

## Common Causes

- Invalid or expired authentication token.
- Module doesn't exist in the registry.

## How to Fix

**Configure registry credentials:**

```hcl
# ~/.terraformrc
credentials "app.terraform.io" {
  token = "your-api-token"
}
```

**Use Git source instead:**

```hcl
module "app" {
  source = "git::https://gitlab.com/my-org/module.git?ref=v1.0"
}
```

## Examples

```bash
export TFE_TOKEN="your-api-token"
terraform init
```
