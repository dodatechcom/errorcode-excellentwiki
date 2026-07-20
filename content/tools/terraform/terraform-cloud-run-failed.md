---
title: "[Solution] Terraform Cloud Run Failed"
description: "Fix Terraform Cloud run failed errors when a TFC run completes with errors."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

TFC run failed errors occur when a remote run fails:

```
Error: Run failed

The run exited with errors. Check the run details in
Terraform Cloud for more information.
```

## Common Causes

- Configuration errors detected during plan.
- Policy check failures.
- Sentinel policy violations.

## How to Fix

**Check run logs via API:**

```bash
curl -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/runs/run-123 | jq '.data.attributes'
```

**Re-trigger run after fixing issues:**

```bash
curl -X POST   -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/runs/run-123/actions/confirm   -d '{}'
```

## Examples

```bash
curl -H "Authorization: Bearer $TFE_TOKEN"   "https://app.terraform.io/api/v2/workspaces/ws-id/runs" | jq '.data[].id'
```
