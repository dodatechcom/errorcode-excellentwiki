---
title: "[Solution] AWS Lambda Concurrency Limit Exceeded"
description: "TooManyRequestsException when the account concurrency limit is reached."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Concurrency Limit Exceeded` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Account default limit (1000) reached
- Burst invocations exceed limit
- Multiple functions share concurrency pool
- Reserved concurrency reduces available pool

## How to Fix

### Check concurrency

```bash
aws lambda get-account-settings --query AccountUsage
```
### Check function concurrency

```bash
aws lambda get-function-concurrency --function-name my-function
```
### Set reserved concurrency

```bash
aws lambda put-function-concurrency --function-name my-function --reserved-concurrent-executions 100
```
### Request limit increase

```bash
aws service-quotas request-service-quota-increase --service-code lambda --quota-code L-B99A9384 --desired-value 3000
```

## Examples

- All 1000 concurrent executions used by one function
- Burst of 500 invocations/second exceeds account limit

## Related Errors

- [Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General Lambda errors
- [Unreserved Concurrency]({{< relref "/cloud/aws/aws-lambda-unreserved-concurrent" >}}) -- Concurrency
