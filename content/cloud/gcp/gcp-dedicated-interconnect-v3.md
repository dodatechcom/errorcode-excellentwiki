---
title: "[Solution] GCP Dedicated Interconnect"
description: "InterconnectError for physical interconnect."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Dedicated Interconnect` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Interconnect name taken
- Location capacity unavailable
- VLAN attachment limit reached

## How to Fix

### List interconnects

```bash
gcloud compute interconnects list
```

## Examples

- Example scenario: interconnect name taken
- Example scenario: location capacity unavailable
- Example scenario: vlan attachment limit reached

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
