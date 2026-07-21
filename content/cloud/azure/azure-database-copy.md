---
title: "[Solution] AZURE Database Copy"
description: "DatabaseCopyError for copy operations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Database Copy` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Source DB not found
- Target server not same region
- Copy in progress already

## How to Fix

### Start copy

```bash
az sql db copy -g myRG -s myServer -n myDB --dest-name myCopy
```

## Examples

- Example scenario: source db not found
- Example scenario: target server not same region
- Example scenario: copy in progress already

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
