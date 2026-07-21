---
title: "[Solution] AZURE Container Group"
description: "ContainerGroupError for container groups."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Container Group` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- YAML validation failed
- Container port conflict
- Volume mount error

## How to Fix

### Create group

```bash
az container create -g myRG -n myCG --image nginx
```

## Examples

- Example scenario: yaml validation failed
- Example scenario: container port conflict
- Example scenario: volume mount error

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
