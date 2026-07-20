---
title: "[Solution] Terraform File Provisioner Not Found"
description: "Fix Terraform file provisioner not found errors when the source file doesn't exist."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

File provisioner errors occur when the source file is missing:

```
Error: File source not found

Source file "scripts/deploy.sh" does not exist.
```

## Common Causes

- File path is incorrect.
- File was deleted or not committed.

## How to Fix

**Verify source file exists:**

```bash
ls -la scripts/deploy.sh
```

**Use file function for templates:**

```hcl
provisioner "file" {
  content     = templatefile("scripts/deploy.sh.tpl", { env = "prod" })
  destination = "/tmp/deploy.sh"
}
```

## Examples

```hcl
provisioner "file" {
  source      = "scripts/setup.sh"
  destination = "/tmp/setup.sh"
}
```
