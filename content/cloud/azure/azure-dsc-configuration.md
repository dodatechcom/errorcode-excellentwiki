---
title: "[Solution] AZURE DSC Configuration"
description: "DSCConfigError for DSC."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DSC Configuration` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Configuration syntax error
- Module dependency missing
- Node registration failed

## How to Fix

### List configs

```bash
az automation dsc configuration list -g myRG -a myAccount
```

## Examples

- Example scenario: configuration syntax error
- Example scenario: module dependency missing
- Example scenario: node registration failed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
