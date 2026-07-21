---
title: "[Solution] GCP Query (Firestore)"
description: "FirestoreQueryError for queries."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Query (Firestore)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Inequality filter on multiple fields
- Composite index missing
- OR queries not supported for compound sorts

## How to Fix

### Add index

```bash
gcloud firestore indexes composite create --collection-group=myCollection --query-scope=COLLECTION --field-config=field-path=name,order=ASCENDING
```

## Examples

- Example scenario: inequality filter on multiple fields
- Example scenario: composite index missing
- Example scenario: or queries not supported for compound sorts

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
