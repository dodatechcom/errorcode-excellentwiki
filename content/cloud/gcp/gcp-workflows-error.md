---
title: "[Solution] GCP Workflows Error — execution step connector errors"
description: "Fix GCP Workflows errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 174
---

Workflows errors occur when there are issues with workflow definition, step execution, or connector configuration.

## Common Causes
- Workflow YAML/JSON syntax invalid
- Connector authentication fails
- Step timeout exceeded
- Workflow execution quota reached
- Workflows API not enabled

## How to Fix

### 1. Enable Workflows API
```bash
gcloud services enable workflows.googleapis.com --project=PROJECT_ID
```

### 2. List workflows
```bash
gcloud workflows list --location=REGION
```

### 3. Create workflow
```bash
gcloud workflows create WORKFLOW_NAME \
  --location=REGION \
  --source=workflow.yaml
```

### 4. Execute workflow
```bash
gcloud workflows execute WORKFLOW_NAME \
  --location=REGION \
  --data='{"key":"value"}'
```

### 5. Check execution status
```bash
gcloud workflows executions describe EXECUTION_NAME \
  --workflow=WORKFLOW_NAME \
  --location=REGION
```

## Examples

### Create workflow with HTTP connector
```bash
cat > workflow.yaml <<EOF
main:
  params: [input]
  steps:
    - callAPI:
        call: http.get
        args:
          url: "https://jsonplaceholder.typicode.com/posts/1"
        result: response
    - returnResult:
        return: \${response.body}
EOF
gcloud workflows create http-workflow \
  --location=us-central1 \
  --source=workflow.yaml
```

### Execute and get result
```bash
gcloud workflows executions describe my-execution \
  --workflow=my-workflow \
  --location=us-central1 \
  --format="value(result)"
```

## Related Errors
- [GCP Cloud Tasks Error](/cloud/gcp/gcp-cloud-tasks-error/)
- [GCP Eventarc Error](/cloud/gcp/gcp-eventarc-error/)
- [GCP Cloud Functions Error](/cloud/gcp/gcp-cloud-functions-error/)