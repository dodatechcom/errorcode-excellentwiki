---
title: "[Solution] AWS Concurrency Limit"
description: "ReservedFunctionConcurrencyInvocationLimit exceeded."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Concurrency Limit` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Account-level reached (1000 default)
- Burst region reached

## How to Fix

### Check concurrency

```bash
aws lambda get-function-concurrency --function my-function
```

## Examples

- Example scenario: account-level reached (1000 default)
- Example scenario: burst region reached

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
