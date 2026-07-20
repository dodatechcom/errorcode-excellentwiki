---
title: "[Solution] Terraform Output Cross-workspace Reference"
description: "Fix Terraform output cross-workspace reference errors when referencing outputs across workspaces."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cross-workspace reference errors occur when trying to access outputs from a different workspace:

```
Error: Cross-workspace references are not supported

Cannot reference output "vpc_id" from workspace "staging"
in workspace "production".
```

## Common Causes

- Terraform doesn't support cross-workspace references.

## How to Fix

**Use `terraform_remote_state`:**

```hcl
data "terraform_remote_state" "staging" {
  backend = "s3"
  config = {
    bucket = "my-terraform-state"
    key    = "staging/terraform.tfstate"
    region = "us-east-1"
  }
}

output "staging_vpc_id" {
  value = data.terraform_remote_state.staging.outputs.vpc_id
}
```

## Examples

```hcl
data "terraform_remote_state" "staging" {
  backend = "s3"
  config = {
    bucket = "my-state-bucket"
    key    = "staging/terraform.tfstate"
    region = "us-east-1"
  }
}
```
