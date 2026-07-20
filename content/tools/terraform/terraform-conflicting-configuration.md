---
title: "[Solution] Terraform Conflicting Configuration"
description: "Fix Terraform conflicting configuration errors when mutually exclusive settings are used."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Conflicting configuration errors occur when mutually exclusive arguments are set:

```
Error: Conflicting configuration arguments

"cidr_block" and "ipv6_cidr_block" cannot both be set.
```

## Common Causes

- Using both inline and external security group rules.
- Setting count and for_each simultaneously.

## How to Fix

**Use dynamic blocks for conditional config:**

```hcl
resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ingress.value.cidrs
    }
  }
}
```

## Examples

```hcl
resource "aws_subnet" "main" {
  vpc_id          = var.vpc_id
  cidr_block      = var.ipv6_only ? null : var.cidr_block
  ipv6_cidr_block = var.ipv6_only ? var.ipv6_cidr_block : null
}
```
