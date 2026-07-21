---
title: "[Solution] GCP Recommendation AI Error -- catalog event predict errors"
description: "Fix GCP Recommendation AI errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 143
---

Recommendation AI errors occur when there are issues with catalog management, event logging, or prediction requests.

## Common Causes
- Catalog item attributes missing required fields
- Event timestamp format invalid
- User event not properly formatted
- Prediction request exceeds model limits
- Recommendation AI API not enabled

## How to Fix

### 1. Enable Recommendation AI API
```bash
gcloud services enable recommendations.googleapis.com --project=PROJECT_ID
```

### 2. Create catalog
```bash
gcloud recommendation-engine catalogs create CATALOG_NAME \
  --location=LOCATION
```

### 3. Import catalog items
```bash
gcloud recommendation-engine catalogs items import CATALOG_NAME \
  --location=LOCATION \
  --gcs-uris="gs://bucket/catalog.json"
```

### 4. Log user event
```bash
gcloud recommendation-engine user-events log \
  --catalog=CATALOG_NAME \
  --location=LOCATION \
  --user-event='{"eventType":"detail-page-view","visitorId":"user123"}'
```

### 5. List placements
```bash
gcloud recommendation-engine placements list \
  --catalog=CATALOG_NAME \
  --location=LOCATION
```

## Examples

### Create placement for recommendations
```bash
gcloud recommendation-engine placements create home-page \
  --catalog=my-catalog \
  --location=global \
  --display-name="Home Page Recommendations"
```

### Train recommendation model
```bash
gcloud recommendation-engine models train \
  --catalog=my-catalog \
  --location=global \
  --placement-id=home-page \
  --model-type=cloud-user-personalization
```

## Related Errors
- [GCP Retail Error](/cloud/gcp/gcp-retail-error/)
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
- [GCP Vertex AI Error](/cloud/gcp/gcp-vertex-ai-error/)