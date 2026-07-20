---
title: "[Solution] GCP Retail API Error — product event serving-config errors"
description: "Fix GCP Retail API errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 144
---

Retail API errors occur when there are issues with product catalog, user events, or serving configurations.

## Common Causes
- Product JSON schema validation fails
- Serving config references non-existent catalog
- User event missing required fields
- Product not in active state for predictions
- Retail API not enabled

## How to Fix

### 1. Enable Retail API
```bash
gcloud services enable retail.googleapis.com --project=PROJECT_ID
```

### 2. Create catalog
```bash
gcloud retail catalogs create CATALOG_NAME \
  --display-name="Product Catalog"
```

### 3. Import products
```bash
gcloud retail catalogs products import CATALOG_NAME \
  --gcs-uris="gs://bucket/products.json" \
  --invalid-products-skip
```

### 4. Write user event
```bash
gcloud retail catalogs user-events write CATALOG_NAME \
  --user-event='{"eventType":"detail-page-view","visitorId":"user1","productDetails":[{"productId":"SKU123"}]}'
```

### 5. Create serving config
```bash
gcloud retail catalogs serving-configs create CONFIG_NAME \
  --catalog=CATALOG_NAME \
  --type=home-page \
  --model-id=MODEL_ID
```

## Examples

### Generate predictions
```bash
gcloud retail catalogs serving-configs predict home-page \
  --catalog=my-catalog \
  --user-event='{"eventType":"detail-page-view","visitorId":"user1"}' \
  --page-size=10
```

### List product operations
```bash
gcloud retail catalogs products list CATALOG_NAME \
  --format="table(name,title,availability)"
```

## Related Errors
- [GCP Recommendation AI Error](/cloud/gcp/gcp-recommendation-ai-error/)
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
- [GCP Vertex AI Error](/cloud/gcp/gcp-vertex-ai-error/)