---
title: "[Solution] GCP Forwarding Rule"
description: "ForwardingRuleError for rules."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Forwarding Rule` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Rule name taken
- IP address already in use
- Port range overlapping

## How to Fix

### Create rule

```bash
gcloud compute forwarding-rules create myRule --region=us-central1 --ip-protocol=TCP --ports=80
```

## Examples

- Example scenario: rule name taken
- Example scenario: ip address already in use
- Example scenario: port range overlapping

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
