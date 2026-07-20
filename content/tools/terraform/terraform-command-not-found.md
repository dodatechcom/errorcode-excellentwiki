---
title: "[Solution] Terraform Command Not Found"
description: "Fix Terraform command not found errors when the terraform binary is not in PATH."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Command not found errors occur when the `terraform` binary is not accessible:

```
bash: terraform: command not found
```

## Common Causes

- Terraform not installed.
- Binary not in PATH.

## How to Fix

**Install Terraform:**

```bash
# Using tfenv
git clone https://github.com/tfutils/tfenv.git ~/.tfenv
ln -s ~/.tfenv/bin/* /usr/local/bin/
tfenv install latest
tfenv use latest
```

**Verify PATH:**

```bash
which terraform
echo $PATH
```

**Add to PATH:**

```bash
export PATH="$PATH:/opt/terraform"
echo 'export PATH="$PATH:/opt/terraform"' >> ~/.bashrc
```

## Examples

```bash
terraform version
find / -name terraform -type f 2>/dev/null
```
