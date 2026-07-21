---
title: "[Solution] GCP Cloud Spanner Increase Quota Error"
description: "Fix Cloud Spanner quota increase errors. Resolve node limits, storage capacity, and regional quota issues in Google Cloud Spanner."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Spanner Increase Quota Error

The Cloud Spanner Increase Quota error occurs when requests to add nodes or increase storage capacity to a Spanner instance are denied due to quota limits.

## Common Causes

- Instance node count exceeds project or region quota
- Storage increase request is pending admin approval
- Edition-based capacity limits are reached
- Billing account cannot support additional capacity
- Regional resource availability is constrained

## How to Fix

### 1. Check current quota
```bash
gcloud spanner instances describe INSTANCE_ID \
  --format="yaml(nodeCount,edition,config)"
```

### 2. Update instance node count
```bash
gcloud spanner instances update INSTANCE_ID \
  --node-count=10
```

### 3. Request quota increase
```bash
gcloud alpha quota requests submit \
  --service=spanner.googleapis.com \
  --quota=SPANNER_NODES \
  --value=20
```

### 4. Check billing account status
```bash
gcloud billing accounts list --format="table(name,open)"
```

## Examples

### Update Spanner to 20 nodes
```bash
gcloud spanner instances update my-spanner \
  --node-count=20 \
  --quiet
```

### Check regional node limits
```bash
gcloud alpha quota list --service=spanner.googleapis.com \
  --filter="metric=spanner.googleapis.com/nodes"
```

## Related Errors

- [GCP Spanner Error]({{< relref "/cloud/gcp/gcp-spanner-error" >}})
- [GCP Instance Spanner]({{< relref "/cloud/gcp/gcp-instance-(spanner)" >}})
