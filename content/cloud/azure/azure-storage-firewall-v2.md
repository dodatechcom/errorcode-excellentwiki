---
title: "[Solution] AZURE Storage Firewall"
description: "StorageFirewallError for firewall rules."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Storage Firewall` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Client IP not in whitelist
- Service endpoint missing
- Private endpoint conflict

## How to Fix

### Add network rule

```bash
az storage account network-rule add -g myRG --account myAccount --ip-address 203.0.113.0
```

## Examples

- Example scenario: client ip not in whitelist
- Example scenario: service endpoint missing
- Example scenario: private endpoint conflict

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
