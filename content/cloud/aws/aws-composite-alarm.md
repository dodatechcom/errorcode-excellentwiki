---
title: "[Solution] AWS Composite Alarm"
description: "BadRequest for composite alarms."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Composite Alarm` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Rule expression empty
- References non-existent alarm
- Circular dependency

## How to Fix

### List composite alarms

```bash
aws cloudwatch describe-alarms --alarm-type CompositeAlarm
```

## Examples

- Example scenario: rule expression empty
- Example scenario: references non-existent alarm
- Example scenario: circular dependency

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
