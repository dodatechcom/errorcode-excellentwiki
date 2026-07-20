---
title: "[Solution] GCP Cloud Trace Error — span trace sampling export errors"
description: "Fix GCP Cloud Trace errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 150
---

Cloud Trace errors occur when there are issues with span creation, trace sampling configuration, or export to destinations.

## Common Causes
- Trace quota exceeded for project
- Sampling rate too high causing performance issues
- Trace export destination unreachable
- Invalid trace ID or span format
- Cloud Trace API not enabled

## How to Fix

### 1. Enable Cloud Trace API
```bash
gcloud services enable cloudtrace.googleapis.com --project=PROJECT_ID
```

### 2. List traces
```bash
gcloud traces list --filter='has Span' --limit=10
```

### 3. Get trace details
```bash
gcloud traces describe TRACE_ID
```

### 4. Create trace sampling config
```bash
gcloud alpha monitoring time-series create \
  --metric="cloudtrace.googleapis.com/trace/trace" \
  --resource-type=global
```

### 5. Export traces
```bash
gcloud logging read 'trace="projects/PROJECT/traces/TRACE_ID"' \
  --limit=100 \
  --format=json > traces.json
```

## Examples

### Query traces for specific service
```bash
gcloud logging read 'trace:my-service AND latency>1s' \
  --limit=20 \
  --format="table(timestamp,textPayload,httpRequest.status)"
```

### Check trace quota
```bash
gcloud alpha services quota describe cloudtrace.googleapis.com \
  --consumer=projects/PROJECT_ID
```

## Related Errors
- [GCP Cloud Monitoring Error](/cloud/gcp/gcp-cloud-monitoring-error/)
- [GCP Cloud Logging Error](/cloud/gcp/gcp-cloud-logging-error/)
- [GCP Cloud Profiler Error](/cloud/gcp/gcp-cloud-profiler-error/)