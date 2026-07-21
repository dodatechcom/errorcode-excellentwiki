---
title: "[Solution] AZURE Policy Definition"
description: "PolicyDefError for definitions."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Policy Definition` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Definition already exists
- Parameters not specified
- Effect invalid

## How to Fix

### Create definition

```bash
az policy definition create -n myPolicy --rules @policy.json
```

## Examples

- Example scenario: definition already exists
- Example scenario: parameters not specified
- Example scenario: effect invalid

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
