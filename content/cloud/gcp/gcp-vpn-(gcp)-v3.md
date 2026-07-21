---
title: "[Solution] GCP VPN (GCP)"
description: "VPNError for Cloud VPN."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `VPN (GCP)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Tunnel name taken
- Shared secret mismatch
- IKE version incompatible

## How to Fix

### Create VPN tunnel

```bash
gcloud compute vpn-tunnels create myTunnel --peer-ip=1.2.3.4 --shared-secret=abc123
```

## Examples

- Example scenario: tunnel name taken
- Example scenario: shared secret mismatch
- Example scenario: ike version incompatible

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
