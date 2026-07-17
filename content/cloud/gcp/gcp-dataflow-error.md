---
title: "[Solution] GCP Dataflow Job Error"
description: "Fix GCP Dataflow job errors. Resolve Dataflow pipeline and job issues."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["gcp", "dataflow", "pipeline", "beam", "streaming"]
weight: 5
---

A GCP Dataflow job error occurs when Dataflow pipelines fail to start, execute, or complete. This can be caused by code, configuration, or resource issues.

## Common Causes

- Pipeline code has errors
- Worker instance type not available in the region
- Insufficient permissions for Dataflow operations
- Staging/temporary bucket not accessible
- Template parameters are invalid

## How to Fix

### Check Job Status

```bash
gcloud dataflow jobs list --region=us-central1
gcloud dataflow jobs describe JOB_ID --region=us-central1
```

### View Logs

```bash
gcloud logging read "resource.type=dataflow_step AND resource.labels.job_id=JOB_ID" --limit 50
```

### Cancel Job

```bash
gcloud dataflow jobs cancel JOB_ID --region=us-central1
```

### Run Template

```bash
gcloud dataflow run-template \
  --gcs-location gs://my-bucket/templates/my-template \
  --parameters input=gs://input,output=gs://output \
  --region us-central1
```

### Check Worker Logs

```bash
gcloud logging read "resource.type=gce_instance AND resource.labels.job_name=JOB_ID" --limit 50
```

## Examples

```bash
# Example 1: Worker failed
# Worker failed to start
# Fix: check machine type availability and quota

# Example 2: Template error
# Invalid template parameters
# Fix: verify template parameters and input format
```

## Related Errors

- [GCP BigQuery Error]({{< relref "/cloud/gcp/gcp-bigquery-error" >}}) — BigQuery query error
- [GCP IAM Error]({{< relref "/cloud/gcp/gcp-iam-error" >}}) — IAM permission denied
