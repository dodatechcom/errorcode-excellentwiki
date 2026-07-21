---
title: "[Solution] AWS Lambda Concurrency Limit"
description: "ReservedFunctionConcurrencyInvocationLimit exceeded."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Concurrency Limit` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Account-level concurrency limit reached (1000 default)
- Reserved concurrency quota exceeded at function level
- Burst concurrency per region reached
- Provisioned concurrency uses all available slots
- No unreserved concurrency available across functions

## How to Fix

### Get concurrency settings

```bash
aws lambda get-function-concurrency --function-name my-function
```

## Examples

- Example scenario: account-level concurrency limit reached (1000 default)
- Example scenario: reserved concurrency quota exceeded at function level
- Example scenario: burst concurrency per region reached
- Example scenario: provisioned concurrency uses all available slots

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
