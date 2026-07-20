---
title: "[Solution] Terraform Module Directory Not Found"
description: "Fix Terraform module directory not found errors when local module path is invalid."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Module directory not found errors occur when a local path doesn't exist:

```
Error: Module directory not found

Module directory "../modules/vpc" does not exist.
```

## Common Causes

- Directory path is wrong.
- Directory was deleted or moved.

## How to Fix

**Verify directory exists:**

```bash
ls -la ../modules/vpc/
```

**Use absolute path:**

```hcl
module "vpc" {
  source = "/opt/terraform/modules/vpc"
}
```

## Examples

```bash
find . -name "*.tf" -path "*/modules/*" | head -20
```
