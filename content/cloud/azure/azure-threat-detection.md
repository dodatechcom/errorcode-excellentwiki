---
title: "[Solution] AZURE Threat Detection"
description: "SQLThreatDetectionError for Defender."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Threat Detection` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Alert type not supported
- Storage account missing
- Email recipients not set

## How to Fix

### Enable threat detection

```bash
az sql db threat-policy update -g myRG -s myServer -n myDb
```

## Examples

- Example scenario: alert type not supported
- Example scenario: storage account missing
- Example scenario: email recipients not set

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
