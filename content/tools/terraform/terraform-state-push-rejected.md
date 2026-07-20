---
title: "[Solution] Terraform State Push Rejected"
description: "Fix Terraform state push rejected errors when the state file is rejected by the backend."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State push rejected errors occur when `terraform state push` fails:

```
Error: Error pushing state

Error: state serial 45 is not newer than current serial 45.
```

## Common Causes

- State serial not incremented.
- State is stale (behind current version).

## How to Fix

**Increment the state serial:**

```bash
terraform state pull > state.json
# Edit the "serial" field to be one higher
terraform state push state.json
```

**Use `-force` to overwrite (dangerous):**

```bash
terraform state push -force state.json
```

## Examples

```bash
terraform state pull | jq '.serial'
cat state.json | jq '.serial += 1' > state-new.json
terraform state push state-new.json
```
