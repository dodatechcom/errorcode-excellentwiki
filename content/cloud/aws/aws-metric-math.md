---
title: "[Solution] AWS Metric Math"
description: "InvalidExpression for metric math."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Metric Math` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Syntax error in expression
- Period mismatch
- Statistic invalid

## How to Fix

### Get metric math

```bash
aws cloudwatch get-metric-data --queries file://queries.json
```

## Examples

- Example scenario: syntax error in expression
- Example scenario: period mismatch
- Example scenario: statistic invalid

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
