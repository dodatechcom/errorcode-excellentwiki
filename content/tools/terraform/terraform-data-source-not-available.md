---
title: "[Solution] Terraform Data Source Not Available"
description: "Fix Terraform data source not available errors when a data source cannot find matching resources."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Data source not available errors occur when a data source query returns no results:

```
Error: DataSource "aws_ami" not found

No AMI matching filters was found in the specified region.
```

## Common Causes

- Resource doesn't exist in the target region/account.
- Filter criteria are too restrictive.
- Wrong region or account configured.

## How to Fix

**Use `try()` for optional data sources:**

```hcl
locals {
  ami_id = try(data.aws_ami.selected.id, null)
}
```

**Relax filter criteria:**

```hcl
data "aws_ami" "latest" {
  most_recent = true
  owners      = ["self"]

  filter {
    name   = "name"
    values = ["my-ami-*"]
  }
}
```

## Examples

```hcl
data "aws_caller_identity" "current" {}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}
```
