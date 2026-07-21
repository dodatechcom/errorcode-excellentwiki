---
title: "[Solution] GCP Cluster (Bigtable)"
description: "BigtableClusterError for clusters."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cluster (Bigtable)` error occurs when a GCP service cannot complete the requested operation.

## Common Causes

- Cluster ID taken within instance
- Node count too low (min 3 for prod)
- Zone not available for Bigtable

## How to Fix

### Create cluster

```bash
gcloud bigtable clusters create myCluster --instance=myInstance --zone=us-central1-a
```

## Examples

- Example scenario: cluster id taken within instance
- Example scenario: node count too low (min 3 for prod)
- Example scenario: zone not available for bigtable

## Related Errors

- [GCP EC2 Error]({{< relref "/cloud/gcp/gcp-error" >}}) -- General errors
- [GCP Logging Error]({{< relref "/cloud/gcp/gcp-logging-error" >}}) -- Logging errors
