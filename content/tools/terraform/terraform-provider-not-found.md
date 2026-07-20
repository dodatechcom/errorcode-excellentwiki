---
title: "[Solution] Terraform Provider Not Found"
description: "Fix Terraform provider not found errors when the provider cannot be located."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The `provider not found` error occurs when Terraform cannot locate the requested provider plugin during `terraform init`.

```
Error: Failed to install provider

Error: Failed to install hashicorp/aws: could not find package
for registry.terraform.io/hashicorp/aws 4.67.0
```

## Common Causes

- The provider name is misspelled in the `required_providers` block.
- The provider source address is incorrect (e.g., missing namespace).
- The requested version does not exist in the registry.
- Network connectivity issues prevent downloading.

## How to Fix

**Verify the provider source address:**

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

**Force re-download:**

```bash
terraform init -upgrade
```

## Examples

```hcl
# Wrong — missing namespace
terraform {
  required_providers {
    aws = {
      source  = "aws"
      version = "~> 5.0"
    }
  }
}

# Correct
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```
