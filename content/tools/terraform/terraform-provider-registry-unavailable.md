---
title: "[Solution] Terraform Provider Registry Unavailable"
description: "Fix Terraform provider registry unavailable errors when the registry cannot be reached."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The provider registry unavailable error means Terraform cannot communicate with `registry.terraform.io`:

```
Error: Failed to query available provider packages

Could not retrieve the list of available versions for provider
"hashicorp/aws": could not connect to registry.terraform.io
```

## Common Causes

- Network firewall blocks outbound HTTPS to `registry.terraform.io`.
- Corporate proxy is not configured for Terraform.
- The registry is experiencing downtime.
- DNS resolution failure.

## How to Fix

**Configure proxy settings:**

```bash
export HTTPS_PROXY="http://proxy.example.com:8080"
terraform init
```

**Use a provider mirror:**

```hcl
# ~/.terraformrc
provider_installation {
  network_mirror {
    url     = "https://mirror.company.com/"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
```

## Examples

```bash
# Verify connectivity
curl -I https://registry.terraform.io/v1/providers/hashicorp/aws

# Use filesystem mirror
provider_installation {
  filesystem_mirror {
    path    = "/opt/terraform/mirror"
    include = ["registry.terraform.io/*/*"]
  }
}
```
