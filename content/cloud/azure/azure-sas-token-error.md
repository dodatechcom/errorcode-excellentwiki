---
title: "[Solution] AZURE SAS Token Error"
description: "SASError for shared access signature."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SAS Token Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Token expired
- Signature field mismatch
- Permissions scope invalid

## How to Fix

### Generate SAS

```bash
az storage container generate-sas -n mycontainer --account myAccount --expiry 2026-12-31
```

## Examples

- Example scenario: token expired
- Example scenario: signature field mismatch
- Example scenario: permissions scope invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
