---
title: "[Solution] Terraform API Rate Limit Exceeded"
description: "Fix Terraform API rate limit exceeded errors when cloud provider throttles requests."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

API rate limit errors occur when too many API calls are made:

```
Error: Error creating instance: Throttling

Request limit exceeded (429)
```

## Common Causes

- Bulk resource creation exceeding API limits.
- Multiple Terraform runs in parallel.

## How to Fix

**Add parallelism limits:**

```bash
terraform apply -parallelism=2
```

**Use `-target` to batch:**

```bash
terraform apply -target=module.vpc
terraform apply -target=module.compute
```

## Examples

```hcl
provider "aws" {
  region      = "us-east-1"
  max_retries = 5
}
```
