---
title: "[Solution] GCP Cloud Profiler Error -- agent profile collection errors"
description: "Fix GCP Cloud Profiler errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 151
---

Cloud Profiler errors occur when there are issues with profiler agent initialization, profile collection, or data export.

## Common Causes
- Profiler agent fails to initialize in application
- Insufficient IAM permissions for profile upload
- Application crashes during profiling
- Profile data exceeds storage limits
- Cloud Profiler API not enabled

## How to Fix

### 1. Enable Cloud Profiler API
```bash
gcloud services enable cloudprofiler.googleapis.com --project=PROJECT_ID
```

### 2. Check profiler status
```bash
gcloud profiler list --project=PROJECT_ID
```

### 3. Configure profiler agent for Java
```xml
<dependency>
  <groupId>com.google.cloud.opentelemetry</groupId>
  <artifactId>cloud-profiler-java</artifactId>
  <version>LATEST</version>
</dependency>
```

### 4. Check IAM permissions
```bash
gcloud projects get-iam-policy PROJECT_ID \
  --filter="bindings.members:serviceAccount:PROJECT_NUMBER@cloudservices.gserviceaccount.com"
```

### 5. List profiler targets
```bash
curl -X GET \
  "https://cloudprofiler.googleapis.com/v2/projects/PROJECT/targets" \
  -H "Authorization: Bearer TOKEN"
```

## Examples

### Verify profiler deployment
```bash
gcloud profiler targets list --project=PROJECT_ID \
  --format="table(name,displayName,profilerType)"
```

### Check profile collection logs
```bash
gcloud logging read 'resource.type="cloud_profiler" AND jsonPayload.targetName="my-app"' \
  --limit=10
```

## Related Errors
- [GCP Cloud Trace Error](/cloud/gcp/gcp-cloud-trace-error/)
- [GCP Cloud Debugger Error](/cloud/gcp/gcp-cloud-debugger-error/)
- [GCP IAM Error](/cloud/gcp/gcp-iam-error/)