---
title: "[Solution] GCP API Gateway Error -- API config gateway errors"
description: "Fix GCP API Gateway errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 169
---

API Gateway errors occur when there are issues with API configuration, gateway deployment, or OpenAPI spec validation.

## Common Causes
- OpenAPI spec has invalid syntax
- Backend service unreachable from gateway
- Gateway deployment fails due to IAM
- API Gateway API not enabled
- Certificate for custom domain invalid

## How to Fix

### 1. Enable API Gateway API
```bash
gcloud services enable apigateway.googleapis.com --project=PROJECT_ID
```

### 2. List APIs and gateways
```bash
gcloud apigateway apis list --location=REGION
gcloud apigateway gateways list --location=REGION
```

### 3. Create API
```bash
gcloud apigateway apis create API_NAME --location=REGION
```

### 4. Create API config
```bash
gcloud apigateway api-configs create CONFIG_NAME \
  --api=API_NAME \
  --openapi-spec=openapi.yaml \
  --location=REGION
```

### 5. Create gateway
```bash
gcloud apigateway gateways create GATEWAY_NAME \
  --api=API_NAME \
  --api-config=CONFIG_NAME \
  --location=REGION
```

## Examples

### Deploy gateway with Cloud Run backend
```bash
cat > openapi.yaml <<EOF
openapi: "3.0.0"
info:
  title: My API
  version: "1.0"
paths:
  /hello:
    get:
      x-google-backend:
        address: https://my-service.run.app
      operationId: hello
      responses:
        "200":
          description: Success
EOF
gcloud apigateway api-configs create run-config \
  --api=my-api \
  --openapi-spec=openapi.yaml \
  --location=us-central1
```

### Update gateway config
```bash
gcloud apigateway gateways update my-gateway \
  --api=my-api \
  --api-config=new-config \
  --location=us-central1
```

## Related Errors
- [GCP Apigee Error](/cloud/gcp/gcp-apigee-error/)
- [GCP Cloud Endpoints Error](/cloud/gcp/gcp-endpoints-error/)
- [GCP Cloud Run Error](/cloud/gcp/gcp-cloud-run-error/)