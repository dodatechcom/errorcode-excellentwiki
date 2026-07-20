---
title: "[Solution] GCP Vertex AI Agent Builder Error — search conversation errors"
description: "Fix GCP Vertex AI Agent Builder errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 136
---

Vertex AI Agent Builder errors occur when there are issues with search data stores, conversation agents, or grounding.

## Common Causes
- Data store not properly indexed
- Conversation agent configuration invalid
- Grounding source unreachable
- Vertex AI Search API not enabled
- Insufficient IAM permissions for agent

## How to Fix

### 1. Enable Vertex AI Search API
```bash
gcloud services enable discoveryengine.googleapis.com --project=PROJECT_ID
```

### 2. List data stores
```bash
gcloud discovery-engine data-stores list --location=REGION
```

### 3. Create data store
```bash
gcloud discovery-engine data-stores create DATA_STORE_NAME \
  --location=REGION \
  --display-name="My Data Store" \
  --content-config=UNSTRUCTURED
```

### 4. Create search app
```bash
gcloud discovery-engine search-apps create APP_NAME \
  --location=REGION \
  --data-store-ids=DATA_STORE_ID \
  --search-app-type=SEARCH_APP_TYPE_GENERIC
```

### 5. Create conversation agent
```bash
gcloud discovery-engine conversational-agents create AGENT_NAME \
  --location=REGION \
  --data-store-ids=DATA_STORE_ID
```

## Examples

### Import documents to data store
```bash
gcloud discovery-engine documents import \
  --data-store=my-store \
  --location=us-central1 \
  --gcs-uris="gs://bucket/docs/*"
```

### Test search query
```bash
gcloud discovery-engine search-apps serve-my-search \
  --app=my-app \
  --location=us-central1 \
  --query="how to fix errors"
```

## Related Errors
- [GCP Vertex AI Error](/cloud/gcp/gcp-vertex-ai-error/)
- [GCP Dialogflow Error](/cloud/gcp/gcp-dialogflow-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)