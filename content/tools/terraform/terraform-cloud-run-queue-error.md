---
title: "[Solution] Terraform Cloud Run Queue Error"
description: "Fix Terraform Cloud run queue errors when runs are stuck or failing in the queue."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Run queue errors occur when TFC runs are stuck in the queue:

```
Error: Run is pending

The run is waiting to be processed. It may be queued behind
other runs.
```

## Common Causes

- Run queue is full.
- Concurrent run limit reached.

## How to Fix

**Check run queue status:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   "https://app.terraform.io/api/v2/runs?filter[status]=pending" | jq '.data[].id'
```

**Cancel stuck runs:**

```bash
curl -X POST   -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/runs/run-123/actions/cancel   -d '{}'
```

**Increase concurrency limit:**

```bash
curl -X PATCH   -H "Authorization: Bearer $TFE_TOKEN"   https://app.terraform.io/api/v2/organizations/my-org   -d '{"data":{"attributes":{"concurrency":10}}}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN"   "https://app.terraform.io/api/v2/workspaces/ws-id/runs" | jq '.data[].attributes.status'
```
