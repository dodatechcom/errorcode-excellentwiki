---
title: "[Solution] AWS Insufficient Data"
description: "InsufficientData for CloudWatch alarm."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Insufficient Data` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- No datapoints in period
- Metric generation stopped
- Recently created

## How to Fix

### Get metric data

```bash
aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric CPUUtilization
```

## Examples

- Example scenario: no datapoints in period
- Example scenario: metric generation stopped
- Example scenario: recently created

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
