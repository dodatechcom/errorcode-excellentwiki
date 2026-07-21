---
title: "[Solution] AWS SNS Action"
description: "InvalidParameter for SNS actions."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SNS Action` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- SNS topic not exist
- Permissions missing
- Cross-region not supported

## How to Fix

### Check alarm actions

```bash
aws cloudwatch describe-alarms --alarm-name my-alarm
```

## Examples

- Example scenario: sns topic not exist
- Example scenario: permissions missing
- Example scenario: cross-region not supported

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
