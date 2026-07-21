---
title: "[Solution] GCP User (CloudSQL)"
description: "CloudSQLUserError for users."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `User (CloudSQL)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Username already exists in instance
- Password policy not met
- Host wildcard (%) not allowed for some auth

## How to Fix

### Create user

```bash
gcloud sql users create myUser --instance=myInstance --password=secret
```

## Examples

- Example scenario: username already exists in instance
- Example scenario: password policy not met
- Example scenario: host wildcard (%) not allowed for some auth

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
