---
title: "[Solution] GCP Row Key"
description: "BigtableRowKeyError for row keys."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Row Key` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Row key not found
- Row key design causing hot spotting
- Row key > 4 MB

## How to Fix

### Read rows

```bash
cbt read myTable
```

## Examples

- Example scenario: row key not found
- Example scenario: row key design causing hot spotting
- Example scenario: row key > 4 mb

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
