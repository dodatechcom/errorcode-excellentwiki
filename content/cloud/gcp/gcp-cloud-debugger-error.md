---
title: "[Solution] GCP Cloud Debugger Error -- snapshot logpoint source errors"
description: "Fix GCP Cloud Debugger errors. Actionable solutions with gcloud CLI commands."
error-types: ["api-error"]
severities: ["error"]
weight: 152
---

Cloud Debugger errors occur when there are issues with snapshot creation, logpoint configuration, or source code synchronization.

## Common Causes
- Debugger agent not attached to running instance
- Source code doesn't match deployed version
- Snapshot breakpoint limit exceeded
- Logpoint syntax invalid
- Cloud Debugger API not enabled

## How to Fix

### 1. Enable Cloud Debugger API
```bash
gcloud services enable clouddebugger.googleapis.com --project=PROJECT_ID
```

### 2. List active debug targets
```bash
gcloud debug targets list --project=PROJECT_ID
```

### 3. Create snapshot
```bash
gcloud debug snapshots create SNAPSHOT_NAME \
  --project=PROJECT_ID \
  --location=com.example.MyClass:42
```

### 4. Create logpoint
```bash
gcloud debug logpoints create LOGPOINT_NAME \
  --project=PROJECT_ID \
  --location=com.example.MyClass:42 \
  --expression="message" \
  --log-level=info
```

### 5. List breakpoints
```bash
gcloud debug breakpoints list --project=PROJECT_ID
```

## Examples

### Create snapshot on exception
```bash
gcloud debug snapshots create exception-snapshot \
  --project=PROJECT_ID \
  --location=com.example.Handler:process \
  --condition="error != null" \
  --action=CAPTURE \
  --expression="error"
```

### Set conditional logpoint
```bash
gcloud debug logpoints create debug-logpoint \
  --project=PROJECT_ID \
  --location=com.example.Service:handleRequest \
  --condition="statusCode >= 400" \
  --expression="request" \
  --log-level=warning
```

## Related Errors
- [GCP Cloud Profiler Error](/cloud/gcp/gcp-cloud-profiler-error/)
- [GCP Cloud Trace Error](/cloud/gcp/gcp-cloud-trace-error/)
- [GCP Cloud Logging Error](/cloud/gcp/gcp-cloud-logging-error/)