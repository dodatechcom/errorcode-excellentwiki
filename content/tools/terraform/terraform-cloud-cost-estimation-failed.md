---
title: "[Solution] Terraform Cloud Cost Estimation Failed"
description: "Fix Terraform Cloud cost estimation failed errors when cost estimation cannot be calculated."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cost estimation failures occur when TFC cannot estimate costs:

```
Error: Cost estimation failed

Unable to estimate costs for the given plan. Some resources
may not be supported.
```

## Common Causes

- Provider not supported for cost estimation.
- Custom resources without pricing data.

## How to Fix

**Check cost estimation settings:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/organizations/my-org/cost-estimation | jq '.data.attributes'
```

**Skip cost estimation for unsupported providers:**

```hcl
cost_estimation_enabled = false
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/runs/run-123/cost-estimate | jq '.data.attributes'
```
