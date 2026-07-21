---
title: "[Solution] AWS Metric Filter"
description: "InvalidParameterException for filters."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Metric Filter` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Filter pattern syntax wrong
- Metric name invalid

## How to Fix

### List filters

```bash
aws logs describe-metric-filters --log-group /aws/lambda/myFunc
```

## Examples

- Example scenario: filter pattern syntax wrong
- Example scenario: metric name invalid

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
