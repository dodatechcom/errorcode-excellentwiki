---
title: "[Solution] AZURE Variable Group"
description: "VariableGroupError for variables."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Variable Group` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Group name taken
- Variables not decrypted
- Linked variable count exceeded

## How to Fix

### List groups

```bash
az pipelines variable-group list
```

## Examples

- Example scenario: group name taken
- Example scenario: variables not decrypted
- Example scenario: linked variable count exceeded

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
