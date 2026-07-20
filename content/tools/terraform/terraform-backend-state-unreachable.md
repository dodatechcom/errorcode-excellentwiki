---
title: "[Solution] Terraform Backend State Unreachable"
description: "Fix Terraform backend state unreachable errors when the remote state endpoint is inaccessible."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Backend unreachable errors prevent Terraform from connecting to state:

```
Error: Error loading state

Error: timeout connecting to remote state backend
```

## Common Causes

- VPN or firewall blocking access.
- Backend service is down.
- Authentication token expired.

## How to Fix

**Check network connectivity:**

```bash
curl -I https://app.terraform.io
```

**Refresh authentication:**

```bash
export TFE_TOKEN="valid-token"
terraform init
```

**Use a local fallback:**

```hcl
terraform {
  backend "local" {
    path = "fallback.tfstate"
  }
}
```

## Examples

```bash
terraform init 2>&1 | head -20
terraform init -backend=false
```
