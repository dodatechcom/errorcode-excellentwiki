---
title: "[Solution] AZURE Point in Time Restore"
description: "PITRError for point in time restore."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Point in Time Restore` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Restore time > 35 days ago
- Target server same as source
- Restore to different tier

## How to Fix

### Restore

```bash
az sql db restore -g myRG -s myServer -n myDB --dest-name myRestoredDb --time 2025-06-15T12:00:00Z
```

## Examples

- Example scenario: restore time > 35 days ago
- Example scenario: target server same as source
- Example scenario: restore to different tier

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
