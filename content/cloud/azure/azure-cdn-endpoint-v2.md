---
title: "[Solution] AZURE CDN Endpoint"
description: "CDNEndpointError for CDN endpoints."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `CDN Endpoint` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Endpoint name taken
- Origin host invalid
- Profile type mismatch

## How to Fix

### List endpoints

```bash
az cdn endpoint list -g myRG --profile myProfile
```

## Examples

- Example scenario: endpoint name taken
- Example scenario: origin host invalid
- Example scenario: profile type mismatch

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
