---
title: "[Solution] GCP Job Failed"
description: "JobFailedError for BQ jobs."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Job Failed` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Job ID not found
- Job cancelled by user
- Job timed out (6 hr limit)

## How to Fix

### List jobs

```bash
bq ls -j
```

## Examples

- Example scenario: job id not found
- Example scenario: job cancelled by user
- Example scenario: job timed out (6 hr limit)

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
