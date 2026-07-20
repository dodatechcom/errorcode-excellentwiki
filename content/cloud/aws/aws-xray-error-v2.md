---
title: "[Solution] AWS X-Ray Error (v2) — sampling/trace/segment failures"
description: "Fix AWS X-Ray v2 errors. Resolve sampling rules, trace aggregation, and segment processing issues."
error-types: ["api-error"]
severities: ["error"]
weight: 131
---

An AWS X-Ray error occurs when sampling rules conflict, traces fail to aggregate, or segments are not written. X-Ray provides distributed tracing for microservices but requires correct sampling and daemon configuration.

## Common Causes

- X-Ray daemon not running or not listening on port 2000
- Sampling rule priority conflicts
- Segment size exceeds 64 KB limit
- IAM role does not allow X-Ray write access
- Service graph showing partial traces

## How to Fix

### Check Sampling Rules

```bash
aws xray get-sampling-rules \
  --query 'SamplingRuleRecords[*].SamplingRule'
```

### Create Custom Sampling Rule

```bash
aws xray create-sampling-rule \
  --sampling-rule '{
    "RuleName": "my-api-rule",
    "ResourceARN": "*",
    "Priority": 100,
    "FixedRate": 0.1,
    "ReservoirSize": 5,
    "ServiceName": "my-api",
    "ServiceType": "AWS::ApiGateway::Stage"
  }'
```

### Get Trace Summaries

```bash
aws xray get-trace-summaries \
  --start-time $(date -u -d '1 hour ago' +%s) \
  --end-time $(date -u +%s)
```

### Get Service Graph

```bash
aws xray get-service-graph \
  --start-time $(date -u -d '1 hour ago' +%s) \
  --end-time $(date -u +%s)
```

### Get Groups

```bash
aws xray get-groups \
  --query 'Groups[*].{Name:Name,FilterExpression:FilterExpression}'
```

## Examples

```bash
# Example 1: X-Ray daemon not connected
# Segment was submitted but daemon not running
# Fix: start xray daemon on port 2000

# Example 2: Sampling rule conflict
# ThrottlingException: Sampling rule already exists
# Fix: delete or update existing rule with same priority
```

## Related Errors

- [AWS X-Ray Error]({{< relref "/cloud/aws/aws-xray-error" >}}) — X-Ray v1 errors
- [AWS Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) — Lambda function errors
- [AWS API Gateway Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) — API Gateway errors
