---
title: "[Solution] AZURE Integration Runtime"
description: "IntegrationRuntimeError for IR."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Integration Runtime` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Self-hosted IR not registered (90 min)
- Express VNet injection not set up
- Nodes offline

## How to Fix

### List IRs

```bash
az synapse integration-runtime list -g myRG -w myWS
```

## Examples

- Example scenario: self-hosted ir not registered (90 min)
- Example scenario: express vnet injection not set up
- Example scenario: nodes offline

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
