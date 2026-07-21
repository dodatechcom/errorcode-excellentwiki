---
title: "[Solution] AWS Log Group"
description: "ResourceNotFoundException for log groups."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Log Group` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Name incorrect
- Not exist
- Wrong region

## How to Fix

### Describe log groups

```bash
aws logs describe-log-groups
```

## Examples

- Example scenario: name incorrect
- Example scenario: not exist
- Example scenario: wrong region

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
