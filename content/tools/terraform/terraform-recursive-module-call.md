---
title: "[Solution] Terraform Recursive Module Call"
description: "Fix Terraform recursive module call errors when a module calls itself."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Recursive module call errors occur when modules form circular references:

```
Error: Module "a" calls module "b" which calls module "a"

Cycle detected: module.a -> module.b -> module.a
```

## Common Causes

- Module A references Module B and vice versa.
- Self-referencing module.

## How to Fix

**Break the cycle:**

```hcl
module "shared" {
  source = "../modules/shared"
}

module "a" {
  source    = "../modules/a"
  shared_id = module.shared.id
}

module "b" {
  source    = "../modules/b"
  shared_id = module.shared.id
}
```

## Examples

```bash
terraform graph -type=module | dot -Tpng > modules.png
```
