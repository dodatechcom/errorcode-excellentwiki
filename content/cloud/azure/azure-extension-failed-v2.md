---
title: "[Solution] AZURE Extension Failed"
description: "VMExtensionProvisioningError for extensions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Extension Failed` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Extension script failed
- Extension dependency missing
- VM agent not responsive

## How to Fix

### Get extension

```bash
az vm extension list -n myVM -g myRG
```

## Examples

- Example scenario: extension script failed
- Example scenario: extension dependency missing
- Example scenario: vm agent not responsive

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
