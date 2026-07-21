---
title: "[Solution] AZURE Volume Group"
description: "VolumeGroupError for SAN volume groups."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Volume Group` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Group name taken
- VNet encryption mismatch
- Protocol type invalid

## How to Fix

### Create group

```bash
az elastic-san volume-group create -g myRG -e mySAN -n myGroup
```

## Examples

- Example scenario: group name taken
- Example scenario: vnet encryption mismatch
- Example scenario: protocol type invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
