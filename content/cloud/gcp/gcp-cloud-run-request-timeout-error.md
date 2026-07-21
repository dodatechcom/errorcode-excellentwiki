---
title: "[Solution] GCP Cloud Run Request Timeout Error"
description: "Fix Cloud Run request timeout errors. Resolve 504 gateway timeout, request duration limits, and backend timeout issues in Cloud Run."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run Request Timeout Error

The Cloud Run Request Timeout error occurs when requests to Cloud Run services exceed the platform timeout limits, resulting in 504 errors.

## Common Causes

- Request processing time exceeds the 60-second limit (default)
- Slow external API calls block the request handler
- Large file uploads exceed timeout duration
- Backend database queries take too long
- Network latency to external services is high

## How to Fix

### 1. Increase request timeout
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE \
  --timeout=3600 \
  --region=REGION
```

### 2. Use async processing for long tasks
```python
@app.route('/process', methods=['POST'])
def process():
    # Queue long task and return immediately
    task_queue.enqueue(long_running_task, request.json)
    return {"status": "queued"}, 202
```

### 3. Optimize database queries
```python
# Add pagination and indexing
results = db.collection("items").limit(100).stream()
```

### 4. Check request duration
```bash
gcloud logging read "resource.type=cloud_run_revision \
  AND jsonPayload.requestMethod=GET" \
  --limit=20 --format="json(jsonPayload.requestTime,jsonPayload.status)"
```

## Examples

### Deploy with extended timeout
```bash
gcloud run deploy my-api \
  --image=gcr.io/my-project/api:latest \
  --timeout=3600 \
  --region=us-central1
```

### Check request latency
```bash
gcloud monitoring time-series list \
  --filter='metric.type="run.googleapis.com/request_latencies"' \
  --interval-start-time=$(date -u -d "1 hour ago" +%Y-%m-%dT%H:%M:%SZ)
```

## Related Errors

- [GCP Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}})
- [GCP Cloud Run Invoke Error]({{< relref "/cloud/gcp/gcp-cloud-run-invoke-error" >}})
