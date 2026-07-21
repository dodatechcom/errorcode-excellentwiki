---
title: "[Solution] GCP Cloud SQL Instance"
description: "CloudSQLInstanceError for instances."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud SQL Instance` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Instance name taken
- Storage auto-increase limit
- Maintenance window conflict

## How to Fix

### List instances

```bash
gcloud sql instances list
```

## Examples

- Example scenario: instance name taken
- Example scenario: storage auto-increase limit
- Example scenario: maintenance window conflict

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
