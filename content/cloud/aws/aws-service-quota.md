---
title: "[Solution] AWS Service Quota"
description: "LimitExceeded for CloudWatch."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Quota` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- 5000 alarms per region
- 500 dashboards
- 1000 metric filters

## How to Fix

### Check quotas

```bash
aws service-quotas get-service-quota --service-code cloudwatch --quota-code L-00CMI9Q0
```

## Examples

- Example scenario: 5000 alarms per region
- Example scenario: 500 dashboards
- Example scenario: 1000 metric filters

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
