---
title: "[Solution] GCP Document Not Found"
description: "FirestoreDocumentNotFound for documents."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Document Not Found` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Document path incorrect
- Document deleted
- Collection does not exist

## How to Fix

### Get document

```bash
gcloud firestore documents get myCollection/myDoc
```

## Examples

- Example scenario: document path incorrect
- Example scenario: document deleted
- Example scenario: collection does not exist

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
