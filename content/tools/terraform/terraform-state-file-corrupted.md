---
title: "[Solution] Terraform State File Corrupted"
description: "Fix Terraform state file corrupted errors when the state file is unreadable or malformed."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State corruption errors indicate the state file is damaged:

```
Error: Error reading state

Error: unexpected end of JSON input
```

## Common Causes

- Write interrupted by process crash.
- State file manually edited incorrectly.
- Concurrent writes corrupted the file.

## How to Fix

**Restore from S3 versioning:**

```bash
aws s3api list-object-versions --bucket my-bucket --prefix terraform.tfstate
aws s3api get-object --bucket my-bucket --key terraform.tfstate   --version-id abc123 terraform.tfstate.restored
```

**Pull and fix state:**

```bash
terraform state pull > current-state.json
# Edit carefully
terraform state push current-state.json
```

## Examples

```bash
cat terraform.tfstate | python3 -m json.tool
```
