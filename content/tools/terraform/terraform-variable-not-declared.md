---
title: "[Solution] Terraform Variable Not Declared"
description: "Fix Terraform variable not declared errors when referencing undefined variables."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Variable not declared errors occur when using an undeclared variable:

```
Error: Reference to undeclared variable

A variable "environment" has not been declared.
```

## Common Causes

- Variable definition was deleted.
- Typo in variable name.

## How to Fix

**Declare the variable:**

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"
}
```

**Or pass via CLI:**

```bash
terraform apply -var="environment=production"
```

## Examples

```hcl
variable "environment" {
  type        = string
  description = "Environment name"
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```
