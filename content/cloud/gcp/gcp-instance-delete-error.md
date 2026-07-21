---
title: "[Solution] GCP Instance Delete Error"
description: "InstanceDeleteError for deletion."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Instance Delete Error` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Instance protected by delete-protection
- Instance in provisioning state
- Instance group membership

## How to Fix

### Remove protection

```bash
gcloud compute instances update myVM --no-deletion-protection
```

## Examples

- Example scenario: instance protected by delete-protection
- Example scenario: instance in provisioning state
- Example scenario: instance group membership

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
