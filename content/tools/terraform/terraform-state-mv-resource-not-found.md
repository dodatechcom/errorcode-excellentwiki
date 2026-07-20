---
title: "[Solution] Terraform State Mv Resource Not Found"
description: "Fix Terraform state mv resource not found errors when moving resources between addresses."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State mv fails when the source resource is not in the state:

```
Error: Resource not found

A resource with the address "aws_instance.old" was not found.
```

## Common Causes

- Resource address typo.
- Resource was already moved.

## How to Fix

**List resources in state:**

```bash
terraform state list
```

**Move with correct address:**

```bash
terraform state mv aws_instance.old[0] aws_instance.new[0]
```

## Examples

```bash
terraform state list
terraform state mv 'module.vpc.aws_subnet.public[0]' 'aws_subnet.public'
```
