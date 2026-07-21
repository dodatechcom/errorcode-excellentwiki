---
title: "[Solution] AZURE Connection Error (SQL)"
description: "SQLConnectionError for connectivity."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Connection Error (SQL)` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Firewall rule blocking IP
- VNet service endpoint missing
- SSL/TLS required

## How to Fix

### Add firewall rule

```bash
az sql server firewall-rule create -g myRG -s myServer --start-ip 0.0.0.0 --end-ip 0.0.0.0
```

## Examples

- Example scenario: firewall rule blocking ip
- Example scenario: vnet service endpoint missing
- Example scenario: ssl/tls required

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
