---
title: "[Solution] GCP Cloud Trace Sampling Error"
description: "Fix Cloud Trace sampling errors. Resolve trace data collection, sampling rate, and span recording issues in Google Cloud Trace."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Trace Sampling Error

The Cloud Trace Sampling error occurs when trace data is not being collected or is incomplete due to sampling configuration or SDK issues.

## Common Causes

- Sampling rate is too low and important traces are missed
- Trace SDK is not initialized in the application
- Trace headers are not propagated across services
- Quota limit for traces per second is exceeded
- Trace labels exceed the maximum number of attributes

## How to Fix

### 1. Enable Cloud Trace API
```bash
gcloud services enable cloudtrace.googleapis.com --project=PROJECT_ID
```

### 2. Configure sampling rate
```python
from google.cloud import trace_v2
client = trace_v2.TraceServiceClient()
```

### 3. Set up trace export
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SA@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/cloudtrace.agent"
```

### 4. Check trace quota
```bash
gcloud services quota list --service=cloudtrace.googleapis.com
```

## Examples

### View traces in gcloud
```bash
gcloud trace traces list --project=PROJECT_ID \
  --format="table(traceId,spans.displayName)" \
  --limit=10
```

### Create trace with labels
```python
from google.cloud import trace_v2
span = trace_v2.Span(
    name="projects/PROJECT_ID/traces/TRACE_ID/spans/SPAN_ID",
    span_id="SPAN_ID",
    displayName="my-span",
    attributes={"http.method": "GET"}
)
```

## Related Errors

- [GCP Cloud Trace Error]({{< relref "/cloud/gcp/gcp-cloud-trace-error" >}})
- [GCP Cloud Monitoring Error]({{< relref "/cloud/gcp/gcp-cloud-monitoring-error" >}})
