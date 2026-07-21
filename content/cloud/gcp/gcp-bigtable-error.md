---
title: "[Solution] GCP Bigtable Error -- cluster table read-write throttle errors"
description: "Fix GCP Bigtable errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 120
---

Bigtable errors occur when there are issues with cluster operations, table management, read/write throttling, or replication.

## Common Causes
- Read/write requests throttled due to node count
- Cluster zone experiencing outage
- Schema changes blocking operations
- Replication lag between clusters
- Table creation with invalid column families

## How to Fix

### 1. List Bigtable instances
```bash
gcloud bigtable instances list
```

### 2. Check cluster status
```bash
gcloud bigtable clusters list --instance=INSTANCE_NAME
```

### 3. Create Bigtable instance
```bash
gcloud bigtable instances create INSTANCE_NAME \
  --cluster=CLUSTER_NAME,zone=ZONE,nodes=3 \
  --cluster-config=storage-type=SSD \
  --display-name="Production instance"
```

### 4. Scale cluster nodes
```bash
gcloud bigtable clusters update CLUSTER_NAME \
  --instance=INSTANCE_NAME \
  --nodes=5
```

### 5. List tables and column families
```bash
gcloud bigtable tables list --instance=INSTANCE_NAME
gcloud bigtable tables describe TABLE_NAME --instance=INSTANCE_NAME
```

## Examples

### Create replicated Bigtable instance
```bash
gcloud bigtable instances create multi-region-bt \
  --cluster=cluster-us,zone=us-central1-a,nodes=3 \
  --cluster=cluster-eu,zone=europe-west1-b,nodes=3 \
  --cluster-config=storage-type=SSD \
  --display-name="Multi-region instance"
```

### Check replication status
```bash
gcloud bigtable clusters describe CLUSTER_NAME --instance=INSTANCE_NAME \
  --format="yaml(name,serveNodes,clusterConfig.state)"
```

## Related Errors
- [GCP Cloud SQL Error](/cloud/gcp/gcp-cloud-sql-error/)
- [GCP Firestore Error](/cloud/gcp/gcp-firestore-error/)
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)