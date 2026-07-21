---
title: "[Solution] GCP Security Rules"
description: "FirestoreRulesError for rules."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Security Rules` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Rules syntax error
- Rules too large (>64KB)
- Rules not deployed

## How to Fix

### Deploy rules

```bash
gcloud firestore rules deploy --source=firestore.rules
```

## Examples

- Example scenario: rules syntax error
- Example scenario: rules too large (>64kb)
- Example scenario: rules not deployed

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
