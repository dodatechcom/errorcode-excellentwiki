---
title: "[Solution] GCP Query Exceeded"
description: "QueryExceededError for limits."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Query Exceeded` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Bytes billed exceeded limit
- Concurrent query slot limit reached
- Result too large > 10 GB

## How to Fix

### Set max bytes

```bash
bq query --maximum_bytes_billed=1000000000 'SELECT 1'
```

## Examples

- Example scenario: bytes billed exceeded limit
- Example scenario: concurrent query slot limit reached
- Example scenario: result too large > 10 gb

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
