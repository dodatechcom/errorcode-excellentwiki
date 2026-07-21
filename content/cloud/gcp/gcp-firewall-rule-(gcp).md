---
title: "[Solution] GCP Firewall Rule (GCP)"
description: "FirewallRuleError for VPC firewall."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Firewall Rule (GCP)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Rule name taken
- Priority conflict (< 0 or > 65535)
- Source range overlaps

## How to Fix

### Create firewall

```bash
gcloud compute firewall-rules create myRule --allow tcp:80
```

## Examples

- Example scenario: rule name taken
- Example scenario: priority conflict (< 0 or > 65535)
- Example scenario: source range overlaps

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
