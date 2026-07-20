---
title: "[Solution] Terraform Failed To Query Provider Registry"
description: "Fix Terraform errors querying the provider registry for available versions."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

This error occurs when Terraform cannot query the provider registry API:

```
Error: Failed to query available provider packages

Could not retrieve the list of available versions for provider
"hashicorp/azurerm": rpc error: code = Unavailable
```

## Common Causes

- Registry API rate limiting.
- Network connectivity issues.
- Registry service degradation.

## How to Fix

**Wait and retry:**

```bash
sleep 30 && terraform init
```

**Use a registry mirror:**

```hcl
# ~/.terraformrc
provider_installation {
  network_mirror {
    url     = "https://mirror.company.com/"
    include = ["registry.terraform.io/*/*"]
  }
}
```

**Test registry API directly:**

```bash
curl "https://registry.terraform.io/v1/providers/hashicorp/aws/versions"
```

## Examples

```bash
terraform providers mirror ./local-mirror
```
