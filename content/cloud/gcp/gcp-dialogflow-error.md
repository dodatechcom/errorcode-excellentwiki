---
title: "[Solution] GCP Dialogflow Error — agent intent fulfillment webhook errors"
description: "Fix GCP Dialogflow errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 137
---

Dialogflow errors occur when there are issues with agent configuration, intent matching, fulfillment webhooks, or integrations.

## Common Causes
- Agent language not supported
- Fulfillment webhook URL unreachable
- Intent training phrases insufficient
- Webhook SSL certificate invalid
- Dialogflow API not enabled

## How to Fix

### 1. Enable Dialogflow API
```bash
gcloud services enable dialogflow.googleapis.com --project=PROJECT_ID
```

### 2. List agents
```bash
gcloud dialogflow agents list
```

### 3. Create agent
```bash
gcloud dialogflow agents create AGENT_NAME \
  --display-name="My Agent" \
  --default-language-code=en \
  --time-zone=America/New_York
```

### 4. Export agent
```bash
gcloud dialogflow agents export AGENT_NAME \
  --destination-uri=gs://bucket/agent-export.zip
```

### 5. Update fulfillment webhook
```bash
gcloud dialogflow agents update AGENT_NAME \
  --enable-stackdriver-logging \
  --default-language-code=en
```

## Examples

### Create agent with fulfillment
```bash
gcloud dialogflow agents create support-agent \
  --display-name="Customer Support" \
  --default-language-code=en \
  --time-zone=America/New_York
```

### Import agent from backup
```bash
gcloud dialogflow agents import AGENT_NAME \
  --source=gs://bucket/agent-export.zip
```

## Related Errors
- [GCP Vertex Agent Builder Error](/cloud/gcp/gcp-vertex-agent-builder-error/)
- [GCP Cloud Run Error](/cloud/gcp/gcp-cloud-run-error/)
- [GCP Cloud Functions Error](/cloud/gcp/gcp-cloud-functions-error/)