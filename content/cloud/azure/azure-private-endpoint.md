---
title: "[Solution] AZURE Private Endpoint"
description: "PrivateEndpointError for private endpoints."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Private Endpoint` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Private endpoint already exists
- Subnet already has endpoint
- DNS configuration missing

## How to Fix

### List endpoints

```bash
az network private-endpoint list -g myRG
```

## Examples

- Example scenario: private endpoint already exists
- Example scenario: subnet already has endpoint
- Example scenario: dns configuration missing

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
