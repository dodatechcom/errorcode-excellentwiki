---
title: "[Solution] AZURE Org Not Found"
description: "OrganizationNotFound for Azure DevOps."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Org Not Found` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Org name incorrect
- Org deleted
- User not member

## How to Fix

### List orgs

```bash
az devops admin show
```

## Examples

- Example scenario: org name incorrect
- Example scenario: org deleted
- Example scenario: user not member

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
