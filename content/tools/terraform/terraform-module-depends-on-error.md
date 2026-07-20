---
title: "[Solution] Terraform Module Depends_on Error"
description: "Fix Terraform module depends_on errors when module-level depends_on causes issues."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module depends_on errors occur when module-level dependencies cause problems:

```
Error: Module depends on resource not yet created

Module "compute" depends on module.database which has not
been created yet.
```

## Common Causes

- Implicit dependencies not sufficient.
- depends_on creates hidden dependency chains.

## How to Fix

**Use explicit variable references:**

```hcl
module "compute" {
  source = "../modules/compute"

  # Use variable references instead of depends_on
  db_host = module.database.host
  db_port = module.database.port
}
```

## Examples

```hcl
module "app" {
  source     = "../modules/app"
  db_host    = module.database.endpoint
  db_name    = module.database.name
  subnet_ids = module.vpc.private_subnets
}
```
