---
title: "[Solution] GCP View Error"
description: "ViewError for logical views."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `View Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- View definition invalid SQL
- Authorized view not set up
- Nested views exceed depth (5)

## How to Fix

### Create view

```bash
bq mk --use_legacy_sql=false 'myDataset.myView' 'SELECT * FROM myDataset.myTable'
```

## Examples

- Example scenario: view definition invalid sql
- Example scenario: authorized view not set up
- Example scenario: nested views exceed depth (5)

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
