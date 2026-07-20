---
title: "[Solution] Terraform Module Download Failed"
description: "Fix Terraform module download failed errors when fetching modules from registries or Git."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module download failures prevent Terraform from retrieving required modules:

```
Error: Failed to download module

Error: could not download "git::https://github.com/org/module.git?ref=v1.0"
```

## Common Causes

- Invalid module source URL or Git reference.
- Repository is private without proper authentication.
- Network restrictions blocking Git access.

## How to Fix

**Verify the module source:**

```hcl
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = "~> 3.0"
}
```

**Configure Git credentials:**

```bash
export GIT_CREDENTIAL.helper=store
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

**Check the Git ref:**

```bash
git ls-remote https://github.com/org/module.git refs/tags/v1.0
```

## Examples

```hcl
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = "3.2.1"
}
```
