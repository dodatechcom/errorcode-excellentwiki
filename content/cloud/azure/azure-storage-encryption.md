---
title: "[Solution] AZURE Storage Encryption"
description: "StorageEncryptionError for encryption."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Storage Encryption` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Encryption scope not existing
- Key vault key missing
- Infrastructure encryption not set

## How to Fix

### Enable encryption

```bash
az storage account update -g myRG -n myAccount --encryption-key-type Account
```

## Examples

- Example scenario: encryption scope not existing
- Example scenario: key vault key missing
- Example scenario: infrastructure encryption not set

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
