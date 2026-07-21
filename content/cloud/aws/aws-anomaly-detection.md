---
title: "[Solution] AWS Anomaly Detection"
description: "InvalidParameter for anomaly detection."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Anomaly Detection` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Band not exist
- Time series too short
- Too many zeros

## How to Fix

### Describe anomaly detectors

```bash
aws cloudwatch describe-anomaly-detectors
```

## Examples

- Example scenario: band not exist
- Example scenario: time series too short
- Example scenario: too many zeros

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
