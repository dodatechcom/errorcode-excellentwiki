---
title: "[Solution] GCP Memorystore Error — Redis Memcached connection failover errors"
description: "Fix GCP Memorystore errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 119
---

Memorystore errors occur when there are issues with Redis/Memcached instance connections, failover, or performance.

## Common Causes
- Connection refused due to IP whitelist or network issues
- Failover in progress causing temporary unavailability
- Memory quota exceeded for Redis instance
- Auth token mismatch for protected instances
- Version mismatch between client and instance

## How to Fix

### 1. List Memorystore instances
```bash
gcloud redis instances list --location=REGION
```

### 2. Check instance status
```bash
gcloud redis instances describe INSTANCE_NAME --location=REGION \
  --format="yaml(name,status,memorySizeGb,redisVersion,authEnabled)"
```

### 3. Create Redis instance
```bash
gcloud redis instances create INSTANCE_NAME \
  --location=REGION \
  --size=5 \
  --region=REGION \
  --redis-version=redis_7_0 \
  --tier=STANDARD_HA \
  --network=NETWORK_NAME
```

### 4. Update memory size
```bash
gcloud redis instances resize INSTANCE_NAME \
  --location=REGION \
  --size=10
```

### 5. Enable AUTH
```bash
gcloud redis instances update INSTANCE_NAME \
  --location=REGION \
  --update-auth-enabled
```

## Examples

### Connect to Redis instance
```bash
gcloud redis instances describe my-redis --location=us-central1 \
  --format="value(redisNetworkEndpoints.ipAddress)"

redis-cli -h IP_ADDRESS -p 6379 -a AUTH_STRING ping
```

### Create Memcached instance
```bash
gcloud memcached instances create CACHE_NAME \
  --region=us-central1 \
  --node-count=3 \
  --node-cpu=2 \
  --node-memory=8GB \
  --network=prod-vpc
```

## Related Errors
- [GCP Cloud SQL Error](/cloud/gcp/gcp-cloud-sql-error/)
- [GCP Bigtable Error](/cloud/gcp/gcp-bigtable-error/)
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)