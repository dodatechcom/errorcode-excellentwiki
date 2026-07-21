---
title: "[Solution] AZURE Append Blob"
description: "AppendBlobError for append blobs."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Append Blob` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Append position not at end
- Block size exceeds 4MB
- Concurrent append conflict

## How to Fix

### Create blob

```bash
az storage blob upload -f myfile.txt -c mycontainer -n myblob --type AppendBlob
```

## Examples

- Example scenario: append position not at end
- Example scenario: block size exceeds 4mb
- Example scenario: concurrent append conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
