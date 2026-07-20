---
title: "[Solution] Terraform Undeclared Variable Used"
description: "Fix Terraform undeclared variable used errors when referencing an undefined variable."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Undeclared variable errors occur when referencing a variable not defined:

```
Error: Reference to undeclared variable

A variable "db_password" has not been declared.
```

## Common Causes

- Variable was deleted from variables.tf.
- Typo in variable name.

## How to Fix

**Declare the variable:**

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

**Or use terraform.tfvars:**

```bash
terraform apply -var="db_password=secret123"
```

## Examples

```hcl
variable "db_password" {
  type      = string
  sensitive = true
  description = "Database password"
}

resource "aws_db_instance" "main" {
  password = var.db_password
}
```
