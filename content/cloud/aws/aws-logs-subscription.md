---
title: "[Solution] AWS Logs Subscription"
description: "BadRequest for subscription."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Logs Subscription` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Destination not in same account
- Access policy missing

## How to Fix

### Describe subscriptions

```bash
aws logs describe-subscription-filters --log-group my-group
```

## Examples

- Example scenario: destination not in same account
- Example scenario: access policy missing

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
