---
title: "[Solution] GCP Cloud Router"
description: "CloudRouterError for routers."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cloud Router` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Router name taken
- ASN conflict across BGP sessions
- Router not in same region

## How to Fix

### Create router

```bash
gcloud compute routers create myRouter --region=us-central1
```

## Examples

- Example scenario: router name taken
- Example scenario: asn conflict across bgp sessions
- Example scenario: router not in same region

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
