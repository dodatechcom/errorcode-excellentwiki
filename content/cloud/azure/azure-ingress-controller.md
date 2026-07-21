---
title: "[Solution] AZURE Ingress Controller"
description: "IngressError for ingress controllers."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Ingress Controller` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Ingress class not found
- SSL cert missing
- Hostname conflict

## How to Fix

### Get ingresses

```bash
kubectl get ingress
```

## Examples

- Example scenario: ingress class not found
- Example scenario: ssl cert missing
- Example scenario: hostname conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
