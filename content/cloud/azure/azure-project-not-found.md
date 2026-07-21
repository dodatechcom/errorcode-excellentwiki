---
title: "[Solution] AZURE Project Not Found"
description: "ProjectNotFound for DevOps projects."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Project Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Project name incorrect
- Deleted by admin
- Visibility restriction

## How to Fix

### List projects

```bash
az devops project list
```

## Examples

- Example scenario: project name incorrect
- Example scenario: deleted by admin
- Example scenario: visibility restriction

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
