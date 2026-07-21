---
title: "[Solution] AZURE Container App Ingress"
description: "ContainerAppIngressError for ingress."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Container App Ingress` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Port not open inside container
- TLS certificate not found
- Traffic split percentage invalid

## How to Fix

### Show ingress

```bash
az containerapp ingress show -g myRG -n myApp
```

## Examples

- Example scenario: port not open inside container
- Example scenario: tls certificate not found
- Example scenario: traffic split percentage invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
