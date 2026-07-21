---
title: "[Solution] AZURE Auditing"
description: "SQLAuditError for auditing."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Auditing` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Audit retention policy invalid
- Storage account unreachable
- Event types not set

## How to Fix

### Enable auditing

```bash
az sql db audit-policy update -g myRG -s myServer -n myDb --state Enabled
```

## Examples

- Example scenario: audit retention policy invalid
- Example scenario: storage account unreachable
- Example scenario: event types not set

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
