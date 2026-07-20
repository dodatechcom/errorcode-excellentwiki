---
title: "[Solution] GCP Carbon Footprint Error — data scope export errors"
description: "Fix GCP Carbon Footprint errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 157
---

Carbon Footprint errors occur when there are issues with emissions data retrieval, scope configuration, or export to BigQuery.

## Common Causes
- Carbon Footprint data not available for selected time range
- Export destination BigQuery dataset not created
- Organization scope exceeds reporting window
- Carbon Footprint API not enabled
- Insufficient permissions for emissions data

## How to Fix

### 1. Enable Carbon Footprint API
```bash
gcloud services enable carbonfootprint.googleapis.com --project=PROJECT_ID
```

### 2. List carbon footprint data
```bash
curl -X GET \
  "https://carbonfootprint.googleapis.com/v1/organizations/ORG_ID/footprints" \
  -H "Authorization: Bearer TOKEN"
```

### 3. Create export destination
```bash
bq mk --dataset carbon-footprint-data
```

### 4. Configure export
```bash
curl -X POST \
  "https://carbonfootprint.googleapis.com/v1/organizations/ORG_ID/exports" \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"bigqueryDestination":{"dataset":"carbon-footprint-data","tableId":"emissions"}}'
```

### 5. Check data availability
```bash
curl -X GET \
  "https://carbonfootprint.googleapis.com/v1/organizations/ORG_ID/availableDataRegions" \
  -H "Authorization: Bearer TOKEN"
```

## Examples

### Query carbon footprint data
```bash
bq query --use_legacy_sql=false \
  "SELECT service, sum(emissions_e2_c) as total_emissions
   FROM \`carbon-footprint-data.emissions\`
   GROUP BY service
   ORDER BY total_emissions DESC"
```

### Check organization emissions summary
```bash
curl -X GET \
  "https://carbonfootprint.googleapis.com/v1/organizations/ORG_ID/footprints:summarize" \
  -H "Authorization: Bearer TOKEN"
```

## Related Errors
- [GCP Resource Manager Error](/cloud/gcp/gcp-resource-manager-error/)
- [GCP BigQuery Error](/cloud/gcp/gcp-bigquery-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)