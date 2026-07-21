---
title: "[Solution] GCP DNS Record (GCP)"
description: "DNSRecordError for DNS records."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DNS Record (GCP)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Record name within zone conflict
- Invalid record type for zone
- TTL out of range

## How to Fix

### Add record

```bash
gcloud dns record-sets create --zone=myZone --name=www.example.com --type=A --ttl=300
```

## Examples

- Example scenario: record name within zone conflict
- Example scenario: invalid record type for zone
- Example scenario: ttl out of range

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
