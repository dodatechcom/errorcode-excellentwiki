---
title: "[Solution] AZURE Long-Term Retention"
description: "LTRBackupError for backup retention."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Long-Term Retention` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Retention period not set
- Backup not yet available
- Vault not configured

## How to Fix

### Set policy

```bash
az sql db ltr-policy set -g myRG -s myServer -n myDB --weekly-retention P4W
```

## Examples

- Example scenario: retention period not set
- Example scenario: backup not yet available
- Example scenario: vault not configured

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
