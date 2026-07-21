---
title: "[Solution] AWS Lambda Unreserved Concurrent Executions"
description: "UnreservedConcurrentExecutions limit hit across all functions."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Unreserved Concurrent Executions` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Account-level concurrency exhausted by reserved concurrency
- Too many functions use reserved concurrency
- Non-reserved pool completely consumed
- Sudden traffic spike across multiple functions
- Inadequate function-level tuning

## How to Fix

### Check account summary

```bash
aws lambda get-account-settings
```

## Examples

- Example scenario: account-level concurrency exhausted by reserved concurrency
- Example scenario: too many functions use reserved concurrency
- Example scenario: non-reserved pool completely consumed
- Example scenario: sudden traffic spike across multiple functions

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
