---
title: "[Solution] Terraform Provider Lock File Error"
description: "Fix Terraform provider lock file errors that prevent deterministic provider installation."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Provider lock errors occur when `.terraform.lock.hcl` is out of sync:

```
Error: Missing dependency lock entry

The dependency lock file .terraform.lock.hcl does not include an
entry for provider "registry.terraform.io/hashicorp/azurerm".
```

## Common Causes

- New provider added without running `terraform init`.
- Lock file was deleted or modified manually.
- Platform or OS changed.

## How to Fix

**Reinitialize to update the lock file:**

```bash
terraform init -upgrade
```

**Commit lock file to version control:**

```bash
git add .terraform.lock.hcl
```

**Target a specific platform:**

```bash
terraform init -platform=linux_amd64
```

## Examples

```bash
rm .terraform.lock.hcl
terraform init
```
