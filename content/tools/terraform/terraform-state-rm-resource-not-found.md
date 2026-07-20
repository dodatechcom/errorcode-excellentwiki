---
title: "[Solution] Terraform State Rm Resource Not Found"
description: "Fix Terraform state rm resource not found errors when removing resources from state."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State rm fails when the resource is not found in state:

```
Error: Resource not found

A resource with the address "aws_instance.removed" was not
found in the current state.
```

## Common Causes

- Resource address is incorrect.
- Resource already removed from state.

## How to Fix

**List current state:**

```bash
terraform state list
```

**Remove with correct address:**

```bash
terraform state rm aws_instance.web[0]
```

## Examples

```bash
terraform state list | grep web
terraform state rm 'module.vpc.aws_subnet.public[0]'
```
