---
title: "[Solution] GCP DNS (GCP)"
description: "DNSZoneError for Cloud DNS."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `DNS (GCP)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Zone name taken
- DNS name already managed (SOA)
- DNSSEC signing failed

## How to Fix

### Create zone

```bash
gcloud dns managed-zones create myZone --dns-name=example.com
```

## Examples

- Example scenario: zone name taken
- Example scenario: dns name already managed (soa)
- Example scenario: dnssec signing failed

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
