---
title: "[Solution] Terraform Module Submodule Error"
description: "Fix Terraform module submodule errors when calling nested or child modules."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Submodule errors occur when calling nested modules incorrectly:

```
Error: Module not found

Module "vpc/subnets" was not found in the module directory.
```

## Common Causes

- Submodule directory structure is wrong.
- Module source path incorrect.

## How to Fix

**Verify submodule structure:**

```
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
    subnets/
      main.tf
      variables.tf
```

**Reference submodule correctly:**

```hcl
module "vpc_subnets" {
  source = "../modules/vpc/subnets"
  vpc_id = module.vpc.vpc_id
}
```

## Examples

```hcl
module "database" {
  source = "../../modules/database"
  vpc_id = module.vpc.id
}
```
