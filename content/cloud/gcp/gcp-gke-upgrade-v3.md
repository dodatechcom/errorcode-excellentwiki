---
title: "[Solution] GCP GKE Upgrade"
description: "GKEUpgradeError for upgrades."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `GKE Upgrade` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Upgrade already in progress
- Node pool not ready for upgrade
- Maintenance window not set

## How to Fix

### Upgrade cluster

```bash
gcloud container clusters upgrade myCluster --master --cluster-version=1.28
```

## Examples

- Example scenario: upgrade already in progress
- Example scenario: node pool not ready for upgrade
- Example scenario: maintenance window not set

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
