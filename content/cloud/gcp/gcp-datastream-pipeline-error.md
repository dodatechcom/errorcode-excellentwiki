---
title: "[Solution] GCP Datastream Pipeline Error"
description: "Fix Datastream pipeline errors. Resolve CDC, replication, and data streaming issues between databases in Google Cloud Datastream."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Datastream Pipeline Error

The Datastream Pipeline error occurs when Datastream pipelines fail to replicate data between source and destination databases due to configuration or connectivity issues.

## Common Causes

- Source database does not have CDC enabled
- Datastream agent cannot connect to source database
- Destination dataset does not exist in BigQuery
- Stream is in a FAILED state due to schema changes
- Network firewall rules block Datastream ports

## How to Fix

### 1. Check stream status
```bash
gcloud datastream streams describe STREAM_NAME \
  --location=REGION --format="yaml(state)"
```

### 2. Create a Datastream connection profile
```bash
gcloud datastream connection-profiles create SOURCE_PROFILE \
  --location=REGION \
  --type=mysql \
  --mysql-hostname=SOURCE_HOST \
  --mysql-port=3306 \
  --mysql-username=USER
```

### 3. Start the stream
```bash
gcloud datastream streams start STREAM_NAME --location=REGION
```

### 4. Check pipeline logs
```bash
gcloud logging read "resource.type=datastream_stream \
  AND resource.labels.stream_id=STREAM_NAME" \
  --limit=20
```

## Examples

### Create PostgreSQL connection profile
```bash
gcloud datastream connection-profiles create PG_PROFILE \
  --location=REGION \
  --type=postgresql \
  --postgresql-hostname=db.example.com \
  --postgresql-port=5432 \
  --postgresql-username=replicator
```

### List active streams
```bash
gcloud datastream streams list --location=REGION \
  --format="table(name,state,displayName)"
```

## Related Errors

- [GCP Datastream Error]({{< relref "/cloud/gcp/gcp-datastream-error" >}})
- [GCP Cloud SQL Error]({{< relref "/cloud/gcp/gcp-cloud-sql-error" >}})
