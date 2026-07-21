---
title: "[Solution] GCP Instance Group"
description: "InstanceGroupError for managed groups."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Instance Group` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Group name taken
- Instance template not found
- Named port conflict

## How to Fix

### Create group

```bash
gcloud compute instance-groups managed create myGroup --template myTemplate --size=3
```

## Examples

- Example scenario: group name taken
- Example scenario: instance template not found
- Example scenario: named port conflict

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
