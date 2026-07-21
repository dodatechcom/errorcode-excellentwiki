---
title: "[Solution] GCP Cloud Tasks Error -- queue task handler deadline errors"
description: "Fix GCP Cloud Tasks errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 123
---

Cloud Tasks errors occur when there are issues with queue configuration, task dispatching, handler endpoints, or rate limiting.

## Common Causes
- Task dispatch rate exceeds queue rate limits
- Target service returns non-2xx response
- Task age exceeds maximum age limit
- Queue misconfigured with wrong target
- Cloud Tasks API not enabled

## How to Fix

### 1. Enable Cloud Tasks API
```bash
gcloud services enable cloudtasks.googleapis.com --project=PROJECT_ID
```

### 2. List queues and tasks
```bash
gcloud tasks queues list --location=REGION
gcloud tasks queues describe QUEUE_NAME --location=REGION
```

### 3. Create queue
```bash
gcloud tasks queues create QUEUE_NAME --location=REGION
```

### 4. Add task to queue
```bash
gcloud tasks create-tasks add QUEUE_NAME \
  --location=REGION \
  --uri="https://example.com/task" \
  --http-method=POST \
  --body='{"task":"process"}'
```

### 5. Update queue rate limits
```bash
gcloud tasks queues update QUEUE_NAME \
  --location=REGION \
  --max-dispatches-per-second=10 \
  --max-concurrent-dispatches=5
```

## Examples

### Create queue with retry config
```bash
gcloud tasks queues create high-priority \
  --location=us-central1 \
  --max-attempts=5 \
  --min-backoff=1s \
  --max-backoff=30s \
  --max-doublings=3
```

### Add task with ETA
```bash
gcloud tasks create-tasks add my-queue \
  --location=us-central1 \
  --uri="https://worker.run.app/process" \
  --schedule="2025-01-01T12:00:00Z"
```

## Related Errors
- [GCP Cloud Scheduler Error](/cloud/gcp/gcp-cloud-scheduler-error/)
- [GCP Cloud Run Error](/cloud/gcp/gcp-cloud-run-error/)
- [GCP Pub/Sub Error](/cloud/gcp/gcp-pubsub-error/)