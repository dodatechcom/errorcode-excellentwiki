---
title: "[Solution] GCP Cloud Scheduler Error — job target retry auth errors"
description: "Fix GCP Cloud Scheduler errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 122
---

Cloud Scheduler errors occur when there are issues with job scheduling, target service invocation, retry policies, or authentication.

## Common Causes
- Target URL unreachable or returns HTTP error
- Authentication token expired or invalid
- Retry count exhausted without successful delivery
- Job schedule syntax invalid
- Cloud Scheduler API not enabled

## How to Fix

### 1. Enable Cloud Scheduler API
```bash
gcloud services enable cloudscheduler.googleapis.com --project=PROJECT_ID
```

### 2. List scheduler jobs
```bash
gcloud scheduler jobs list --location=REGION
```

### 3. Create HTTP target job
```bash
gcloud scheduler jobs create http JOB_NAME \
  --location=REGION \
  --schedule="*/5 * * * *" \
  --uri="https://example.com/api/endpoint" \
  --http-method=POST \
  --message-body='{"key":"value"}'
```

### 4. Create Pub/Sub target job
```bash
gcloud scheduler jobs create pubsub JOB_NAME \
  --location=REGION \
  --schedule="0 * * * *" \
  --topic=TOPIC_NAME \
  --message-body='{"data":"test"}'
```

### 5. Create App Engine target job
```bash
gcloud scheduler jobs create app-engine JOB_NAME \
  --location=REGION \
  --schedule="0 9 * * 1" \
  --service=SERVICE_NAME \
  --relative-url="/cron/task"
```

## Examples

### Fix failing job by updating target
```bash
gcloud scheduler jobs update http daily-cleanup \
  --location=us-central1 \
  --uri="https://my-service.run.app/cleanup" \
  --oidc-service-account-email=my-sa@my-project.iam.gserviceaccount.com
```

### Run job immediately
```bash
gcloud scheduler jobs run daily-cleanup --location=us-central1
```

## Related Errors
- [GCP Cloud Tasks Error](/cloud/gcp/gcp-cloud-tasks-error/)
- [GCP Cloud Functions Error](/cloud/gcp/gcp-cloud-functions-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)