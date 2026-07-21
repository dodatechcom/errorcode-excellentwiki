---
title: "[Solution] GCP Looker Error -- instance connection explore look errors"
description: "Fix GCP Looker errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 130
---

Looker errors occur when there are issues with Looker instance provisioning, database connections, or data exploration.

## Common Causes
- Instance creation exceeds quota
- Database connection string invalid
- Looker API key or OAuth credentials expired
- Instance not reachable due to VPC peering
- Looker API not enabled

## How to Fix

### 1. Enable Looker API
```bash
gcloud services enable looker.googleapis.com --project=PROJECT_ID
```

### 2. List Looker instances
```bash
gcloud looker instances list --location=REGION
```

### 3. Create Looker instance
```bash
gcloud looker instances create INSTANCE_NAME \
  --location=REGION \
  --oauth-client-id=CLIENT_ID \
  --oauth-client-secret=CLIENT_SECRET \
  --public-ip-enabled
```

### 4. Check instance status
```bash
gcloud looker instances describe INSTANCE_NAME --location=REGION
```

### 5. Delete instance
```bash
gcloud looker instances delete INSTANCE_NAME --location=REGION --quiet
```

## Examples

### Create private Looker instance
```bash
gcloud looker instances create secure-looker \
  --location=us-central1 \
  --oauth-client-id=ID \
  --oauth-client-secret=SECRET \
  --private-ip-enabled \
  --consumer-network=projects/PROJECT/global/networks/VPC
```

### Check instance domain
```bash
gcloud looker instances describe my-looker \
  --location=us-central1 \
  --format="value(publicIpAddress)"
```

## Related Errors
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
- [GCP Cloud SQL Error](/cloud/gcp/gcp-cloud-sql-error/)
- [GCP VPC Network Error](/cloud/gcp/gcp-vpc-error/)