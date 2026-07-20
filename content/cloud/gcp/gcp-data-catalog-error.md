---
title: "[Solution] GCP Data Catalog Error — tag template entry policy errors"
description: "Fix GCP Data Catalog errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 131
---

Data Catalog errors occur when there are issues with tag templates, entries, or metadata policies.

## Common Causes
- Tag template field type mismatch
- Insufficient permissions for tag attachment
- Entry group already exists or name invalid
- Data Catalog API not enabled
- IAM policy blocks metadata operations

## How to Fix

### 1. Enable Data Catalog API
```bash
gcloud services enable datacatalog.googleapis.com --project=PROJECT_ID
```

### 2. List tag templates
```bash
gcloud data-catalog tag-templates list --location=REGION
```

### 3. Create tag template
```bash
gcloud data-catalog tag-templates create TEMPLATE_NAME \
  --location=REGION \
  --display-name="Quality Tags" \
  --field=id=owner,display-name="Owner",type=enum,enum-values="Alice|Bob|Charlie" \
  --field=id=status,display-name="Status",type=enum,enum-values="ACTIVE|DEPRECATED"
```

### 4. Create entry group
```bash
gcloud data-catalog entry-groups create GROUP_NAME \
  --location=REGION \
  --display-name="My Entries" \
  --description="Entry group for data assets"
```

### 5. List entries
```bash
gcloud data-catalog entries list --location=REGION
```

## Examples

### Attach tag to BigQuery table
```bash
gcloud data-catalog tags create \
  --entry-group=PROJECT \
  --entry=BIGQUERY_DATASET.TABLE \
  --tag-template=quality-template \
  --tag-field=owner=Alice,status=ACTIVE \
  --location=us-central1
```

### Search catalog entries
```bash
gcloud data-catalog search "my-dataset" --location=REGION \
  --format="table(name,linkedResource)"
```

## Related Errors
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)
- [GCP Dataplex Error](/cloud/gcp/gcp-dataplex-error/)