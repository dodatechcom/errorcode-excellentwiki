---
title: "[Solution] AZURE Replica Error"
description: "ReplicaError for container replicas."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Replica Error` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Replica count exceeded max (10)
- OOMKilled in replica
- CrashLoopBackOff

## How to Fix

### Show replicas

```bash
az containerapp replica list -g myRG -n myApp
```

## Examples

- Example scenario: replica count exceeded max (10)
- Example scenario: oomkilled in replica
- Example scenario: crashloopbackoff

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
