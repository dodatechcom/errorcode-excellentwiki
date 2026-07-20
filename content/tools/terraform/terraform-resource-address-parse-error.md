---
title: "[Solution] Terraform Resource Address Parse Error"
description: "Fix Terraform resource address parse errors when referencing resources with invalid syntax."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Resource address parse errors occur when an address string is not valid:

```
Error: Invalid resource address

"aws_instance.web[0" is not a valid resource address syntax.
```

## Common Causes

- Typo in resource reference.
- Invalid characters in resource names.
- Incorrect index syntax.

## How to Fix

**Verify address syntax:**

```hcl
# Correct formats
aws_instance.web           # single resource
aws_instance.web[0]        # indexed resource
module.vpc.aws_instance.web  # module-scoped
```

## Examples

```hcl
aws_instance.web[count.index]
aws_instance.web["primary"]
```
