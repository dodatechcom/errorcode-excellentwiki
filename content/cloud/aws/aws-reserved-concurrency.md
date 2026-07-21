---
title: "[Solution] AWS Reserved Concurrency"
description: "ReservedConcurrentExecutionsLimit."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Reserved Concurrency` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Cannot be 0
- Exceeds total account limit

## How to Fix

### Set reserved concurrency

```bash
aws lambda put-function-concurrency --function my-function --reserved 10
```

## Examples

- Example scenario: cannot be 0
- Example scenario: exceeds total account limit

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
