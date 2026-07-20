---
title: "[Solution] GCP Cloud Endpoints Error — service rollout ESP errors"
description: "Fix GCP Cloud Endpoints errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 170
---

Cloud Endpoints errors occur when there are issues with service configuration, rollout process, or Extensible Service Proxy (ESP).

## Common Causes
- Service config YAML syntax invalid
- ESP fails to connect to backend
- Rollout conflicts with existing config
- Cloud Endpoints API not enabled
- API key restrictions blocking access

## How to Fix

### 1. Enable Cloud Endpoints API
```bash
gcloud services enable endpoints.googleapis.com --project=PROJECT_ID
```

### 2. Deploy service config
```bash
gcloud endpoints services deploy openapi.yaml --project=PROJECT_ID
```

### 3. List managed services
```bash
gcloud endpoints services list --project=PROJECT_ID
```

### 4. Roll out config
```bash
gcloud endpoints services rollout create SERVICE_NAME \
  --rollout-id=rollout-v1 \
  --service-config=CONFIG_ID
```

### 5. Check rollout status
```bash
gcloud endpoints services rollouts list SERVICE_NAME --project=PROJECT_ID
```

## Examples

### Deploy config with API key restrictions
```bash
cat > openapi.yaml <<EOF
swagger: "2.0"
info:
  title: My API
  description: Endpoints-protected API
  version: "1.0.0"
host: my-service.endpoints.PROJECT.cloud.goog
securityDefinitions:
  api_key:
    type: apiKey
    in: query
    name: key
paths:
  /hello:
    get:
      security:
      - api_key: []
      responses:
        "200":
          description: Success
EOF
gcloud endpoints services deploy openapi.yaml
```

### Verify ESP logs
```bash
gcloud logging read 'resource.type="gae_app" AND jsonPayload.message=~"ESP"' \
  --limit=10
```

## Related Errors
- [GCP API Gateway Error](/cloud/gcp/gcp-api-gateway-error/)
- [GCP Apigee Error](/cloud/gcp/gcp-apigee-error/)
- [GCP Cloud Run Error](/cloud/gcp/gcp-cloud-run-error/)