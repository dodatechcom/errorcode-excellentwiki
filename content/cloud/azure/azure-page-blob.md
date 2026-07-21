---
title: "[Solution] AZURE Page Blob"
description: "PageBlobError for page blobs."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Page Blob` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Page size not 512 bytes aligned
- Offset not 512KB aligned
- Disk type not page blob

## How to Fix

### Upload pages

```bash
az storage blob upload -f myfile.vhd -c mycontainer -n myblob --type PageBlob
```

## Examples

- Example scenario: page size not 512 bytes aligned
- Example scenario: offset not 512kb aligned
- Example scenario: disk type not page blob

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
