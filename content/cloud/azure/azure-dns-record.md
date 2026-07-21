---
title: "[Solution] AZURE DNS Record"
description: "DNSRecordError for DNS records."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DNS Record` error occurs when a AZURE service cannot complete the requested operation.

## Common Causes

- Record set conflict
- TTL out of range
- Record type not allowed

## How to Fix

### Create record

```bash
az network dns record-set a add-record -g myRG -z mydomain.com -n www -a 10.0.0.1
```

## Examples

- Example scenario: record set conflict
- Example scenario: ttl out of range
- Example scenario: record type not allowed

## Related Errors

- [AZURE EC2 Error]({{< relref "/cloud/azure/azure-error" >}}) -- General errors
- [AZURE Logging Error]({{< relref "/cloud/azure/azure-logging-error" >}}) -- Logging errors
