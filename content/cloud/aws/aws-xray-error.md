---
title: "[Solution] AWS X-Ray Trace Error"
description: "Fix AWS X-Ray trace errors. Resolve X-Ray tracing and analysis issues."
cloud: ["aws"]
error-types: ["api-error"]
severities: ["error"]
tags: ["aws", "x-ray", "tracing", "debugging", "observability"]
weight: 5
---

An AWS X-Ray trace error occurs when X-Ray cannot collect, process, or display trace data. This affects distributed tracing and debugging capabilities.

## Common Causes

- X-Ray SDK not configured in the application
- IAM role lacks xray:PutTraceSegments permission
- Sampling rules not configured correctly
- X-Ray daemon not running on the instance
- Trace data format is invalid

## How to Fix

### Check X-Ray Daemon

```bash
# On the instance
ps aux | grep xray
```

### Start X-Ray Daemon

```bash
# On the instance
./xray-daemon -b 0.0.0.0:2000
```

### Configure SDK

```javascript
const AWSXRay = require('aws-xray-sdk');
const express = require('express');
const app = express();
app.use(AWSXRay.express.openSegment('my-app'));
```

### Check Trace

```bash
aws xray get-trace-summaries --start-time 2024-01-01T00:00:00 --end-time 2024-01-01T01:00:00
```

### Verify IAM Permissions

```bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::123456789012:role/my-role \
  --action-names xray:PutTraceSegments xray:GetTraceSummaries
```

## Examples

```bash
# Example 1: Daemon not running
# Connection refused: xray-daemon not listening
# Fix: start X-Ray daemon on the instance

# Example 2: Permission denied
# AccessDeniedException: xray:PutTraceSegments
# Fix: add X-Ray permissions to the IAM role
```

## Related Errors

- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function error
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) — API Gateway error
