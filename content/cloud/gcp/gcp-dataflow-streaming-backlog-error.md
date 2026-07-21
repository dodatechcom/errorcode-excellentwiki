---
title: "[Solution] GCP Dataflow Streaming Backlog Error"
description: "Fix Dataflow streaming backlog errors. Resolve worker, autoscaling, and pipeline throughput issues in Google Cloud Dataflow streaming jobs."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Dataflow Streaming Backlog Error

The Dataflow Streaming Backlog error occurs when a streaming pipeline cannot keep up with incoming data, causing growing unprocessed message counts.

## Common Causes

- Worker count is insufficient for data volume
- Autoscaling is disabled or misconfigured
- Pipeline has slow DoFn operations bottlenecking throughput
- Pub/Sub subscription backlog triggers throttling
- Data shuffle writes are disk-throttled

## How to Fix

### 1. Check pipeline backlog
```bash
gcloud dataflow jobs describe JOB_ID --region=REGION \
  --format="yaml(jobMetrics)"
```

### 2. Enable autoscaling
```bash
gcloud dataflow jobs run JOB_NAME \
  --gcs-location=gs://BUCKET/templates/template.json \
  --parameters=autoscalingAlgorithm=THROUGHPUT_BASED
```

### 3. Increase worker count
```bash
gcloud dataflow jobs run JOB_NAME \
  --gcs-location=gs://BUCKET/templates/template.json \
  --parameters=numWorkers=10,maxNumWorkers=50
```

### 4. Monitor Pub/Sub backlog
```bash
gcloud pubsub subscriptions describe SUBSCRIPTION \
  --format="value(numUnackedMessages)"
```

## Examples

### Adjust streaming parameters
```bash
gcloud dataflow jobs run my-streaming-job \
  --gcs-location=gs://my-bucket/templates/streaming.json \
  --parameters= \
    autoscalingAlgorithm=THROUGHPUT_BASED,maxNumWorkers=100
```

### Check worker utilization
```bash
gcloud monitoring time-series list \
  --filter='metric.type="dataflow.googleapis.com/job/current_num_vcpus"' \
  --interval-start-time=$(date -u -d "1 hour ago" +%Y-%m-%dT%H:%M:%SZ)
```

## Related Errors

- [GCP Dataflow Error]({{< relref "/cloud/gcp/gcp-dataflow-error" >}})
- [GCP Job Failed]({{< relref "/cloud/gcp/gcp-job-failed" >}})
