---
title: "[Solution] AZURE Volume"
description: "VolumeError for SAN volumes."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Volume` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Volume name taken
- Size too large (max 64 TiB)
- iSCSI target not accessible

## How to Fix

### Create volume

```bash
az elastic-san volume create -g myRG -e mySAN -v myGroup -n myVol --size 100
```

## Examples

- Example scenario: volume name taken
- Example scenario: size too large (max 64 tib)
- Example scenario: iscsi target not accessible

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
