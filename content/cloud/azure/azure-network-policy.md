---
title: "[Solution] AZURE Network Policy"
description: "NetworkPolicyError for Calico/Azure NPM."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Network Policy` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Pod selector mismatch
- Policy order incorrect
- Port/protocol not allowed

## How to Fix

### Get policies

```bash
kubectl get networkpolicies
```

## Examples

- Example scenario: pod selector mismatch
- Example scenario: policy order incorrect
- Example scenario: port/protocol not allowed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
