---
title: "[Solution] AWS Lambda Reserved Concurrency Error"
description: "ReservedConcurrentExecutionsLimit when setting reserved concurrency."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Reserved Concurrency Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Reserved concurrency value cannot be zero
- Total reserved concurrency across functions exceeds account limit
- Cannot set reserved concurrency below already provisioned amount
- Requested value exceeds available unreserved concurrency

## How to Fix

### Remove reserved concurrency

```bash
aws lambda delete-function-concurrency --function-name my-function
```

### Set reserved concurrency

```bash
aws lambda put-function-concurrency --function-name my-function --reserved-concurrent-executions 10
```

## Examples

- Example scenario: reserved concurrency value cannot be zero
- Example scenario: total reserved concurrency across functions exceeds account limit
- Example scenario: cannot set reserved concurrency below already provisioned amount
- Example scenario: requested value exceeds available unreserved concurrency

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
