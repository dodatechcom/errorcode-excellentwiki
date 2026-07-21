---
title: "[Solution] AZURE Resource Graph"
description: "ResourceGraphError for queries."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Resource Graph` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Query syntax error
- Authorization scope limit
- Too many results (>1000)

## How to Fix

### Run graph query

```bash
az graph query -q resources | project name, type
```

## Examples

- Example scenario: query syntax error
- Example scenario: authorization scope limit
- Example scenario: too many results (>1000)

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
