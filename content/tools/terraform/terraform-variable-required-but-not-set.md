---
title: "[Solution] Terraform Variable Required But Not Set"
description: "Fix Terraform variable required but not set errors when mandatory variables have no value."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Required variable errors occur when a variable with no default is not provided:

```
Error: Required variable not set

Variable "vpc_cidr" is required but was not provided.
```

## Common Causes

- Variable has no default and wasn't provided.
- tfvars file missing the variable.

## How to Fix

**Provide via tfvars:**

```hcl
# terraform.tfvars
vpc_cidr    = "10.0.0.0/16"
environment = "production"
```

**Provide via CLI:**

```bash
terraform apply -var="vpc_cidr=10.0.0.0/16"
```

**Add a default if appropriate:**

```hcl
variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}
```

## Examples

```bash
terraform apply -var-file="production.tfvars"
```
