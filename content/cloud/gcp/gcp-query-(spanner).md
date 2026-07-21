---
title: "[Solution] GCP Query (Spanner)"
description: "SpannerQueryError for queries."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Query (Spanner)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Query not valid for primary key
- Stale read timestamp error
- Interleaved table join not correct

## How to Fix

### Execute query

```bash
gcloud spanner databases execute-sql myDB --instance=myInstance --sql='SELECT * FROM myTable'
```

## Examples

- Example scenario: query not valid for primary key
- Example scenario: stale read timestamp error
- Example scenario: interleaved table join not correct

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
