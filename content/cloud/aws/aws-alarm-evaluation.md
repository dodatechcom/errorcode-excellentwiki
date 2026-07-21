---
title: "[Solution] AWS Alarm Evaluation"
description: "BadRequest for alarm evaluation."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Alarm Evaluation` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Period not divisor of 60
- Evaluation periods exhausted
- Insufficient data

## How to Fix

### Describe alarm

```bash
aws cloudwatch describe-alarms --alarm-names my-alarm
```

## Examples

- Example scenario: period not divisor of 60
- Example scenario: evaluation periods exhausted
- Example scenario: insufficient data

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
