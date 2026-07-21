---
title: "[Solution] AWS Lambda Memory Limit Exceeded"
description: "OutOfMemoryException when a Lambda function exceeds memory."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Memory Limit Exceeded` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Function processes large data sets in memory
- Memory limit set too low
- Recursive calls consume increasing memory
- Large objects loaded entirely into memory

## How to Fix

### Check memory config

```bash
aws lambda get-function-configuration --function-name my-function --query MemorySize
```
### Increase memory

```bash
aws lambda update-function-configuration --function-name my-function --memory-size 1024
```
### Monitor memory

```bash
aws cloudwatch get-metric-statistics --namespace AWS/Lambda --metric-name Memory --dimensions Name=FunctionName,Value=my-function --start-time $(date -u -d "1 hour ago" +\%FT\%TZ) --end-time $(date -u +\%FT\%TZ) --period 60 --statistics Maximum
```

## Examples

- Function with 128 MB processing a 200 MB JSON file
- Recursive invocation causing memory exhaustion

## Related Errors

- [Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General Lambda errors
- [Timeout Error]({{< relref "/cloud/aws/aws-lambda-timeout-error" >}}) -- Timeout issues
