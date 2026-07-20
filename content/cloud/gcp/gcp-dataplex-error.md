---
title: "[Solution] GCP Dataplex Error — lake zone asset scan errors"
description: "Fix GCP Dataplex errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 132
---

Dataplex errors occur when there are issues with lake creation, zone management, asset discovery, or data quality scans.

## Common Causes
- Lake already exists or name collision
- Asset discovery fails due to IAM permissions
- Data scan job exceeds resource limits
- Zone type incompatible with asset
- Dataplex API not enabled

## How to Fix

### 1. Enable Dataplex API
```bash
gcloud services enable dataplex.googleapis.com --project=PROJECT_ID
```

### 2. List lakes and zones
```bash
gcloud dataplex lakes list --location=REGION
gcloud dataplex zones list --lake=LAKE_NAME --location=REGION
```

### 3. Create lake
```bash
gcloud dataplex lakes create LAKE_NAME \
  --location=REGION \
  --display-name="My Lake"
```

### 4. Create zone
```bash
gcloud dataplex zones create ZONE_NAME \
  --lake=LAKE_NAME \
  --location=REGION \
  --type=RAW \
  --display-name="Raw Zone"
```

### 5. Create data scan
```bash
gcloud dataplex data-scans create DATA_SCAN_NAME \
  --location=REGION \
  --data-source-resource=projects/PROJECT/locations/REGION/lakes/LAKE/zones/ZONE/assets/ASSET \
  --data-scan-type=DATA_QUALITY
```

## Examples

### Discover BigQuery assets
```bash
gcloud dataplex assets create bq-asset \
  --lake=my-lake \
  --zone=curated-zone \
  --location=us-central1 \
  --resource-name=projects/PROJECT/datasets/DATASET
```

### Run data quality scan
```bash
gcloud dataplex data-scans run quality-scan \
  --location=us-central1
```

## Related Errors
- [GCP Data Catalog Error](/cloud/gcp/gcp-data-catalog-error/)
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)