---
title: "[Solution] Terraform Local-exec Command Failed"
description: "Fix Terraform local-exec command failed errors when local commands fail."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Local-exec command failures occur when the locally executed command fails:

```
Error: local-exec provisioner error

Error running command: exit status 127
Output: bash: my-script.sh: command not found
```

## Common Causes

- Command or script not in PATH.
- Script not executable.
- Missing dependencies on local machine.

## How to Fix

**Use absolute paths:**

```hcl
provisioner "local-exec" {
  command = "/bin/bash ${path.module}/scripts/setup.sh"
}
```

**Make script executable:**

```bash
chmod +x scripts/setup.sh
```

## Examples

```hcl
provisioner "local-exec" {
  command     = "./scripts/deploy.sh"
  working_dir = "${path.module}"
  environment = {
    INSTANCE_ID = self.id
  }
}
```
