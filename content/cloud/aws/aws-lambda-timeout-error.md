---
title: "[Solution] AWS Lambda Timeout Error"
description: "Task timed out when Lambda execution exceeds configured timeout."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Timeout Error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Function takes longer than timeout
- External API calls are slow
- Database queries not optimized
- Function waits for downstream services

## How to Fix

### Check timeout config

```bash
aws lambda get-function-configuration --function-name my-function --query Timeout
```
### Increase timeout

```bash
aws lambda update-function-configuration --function-name my-function --timeout 900
```
### Check logs

```bash
aws logs filter-log-events --log-group-name /aws/lambda/my-function --filter-pattern "REPORT Duration" --limit 10
```

## Examples

- Timeout set to 3 seconds but takes 8 seconds
- External API call taking 30 seconds

## Related Errors

- [Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General Lambda errors
- [Memory Limit]({{< relref "/cloud/aws/aws-lambda-memory-limit" >}}) -- Memory issues
