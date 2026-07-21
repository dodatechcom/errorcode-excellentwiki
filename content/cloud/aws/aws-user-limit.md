---
title: "[Solution] AWS User Limit"
description: "LimitExceeded for user count."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `User Limit` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- 5000 users per account default

## How to Fix

### List users

```bash
aws iam list-users
```

## Examples

- Example scenario: 5000 users per account default

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
