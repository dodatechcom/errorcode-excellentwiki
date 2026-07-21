---
title: "[Solution] AWS Lambda Memory Limit Error"
description: "MemoryAllocationError/Lambda memory limit exhausted."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Memory Limit Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Function uses more memory than allocated, triggering OOM
- Memory limit set too low for workload
- Memory leak in code over execution cycles
- Large payload processing exceeds memory
- Concurrent executions accumulate memory pressure

## How to Fix

### Check memory setting

```bash
aws lambda get-function-configuration --function-name my-function --query MemorySize
```

### Update memory

```bash
aws lambda update-function-configuration --function-name my-function --memory-size 2048
```

## Examples

- Example scenario: function uses more memory than allocated, triggering oom
- Example scenario: memory limit set too low for workload
- Example scenario: memory leak in code over execution cycles
- Example scenario: large payload processing exceeds memory

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
