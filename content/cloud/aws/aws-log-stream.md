---
title: "[Solution] AWS Log Stream"
description: "ResourceNotFoundException for log streams."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Log Stream` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Name not exist
- Deleted
- Wrong log group

## How to Fix

### Describe log streams

```bash
aws logs describe-log-streams --log-group /aws/lambda/myFunc
```

## Examples

- Example scenario: name not exist
- Example scenario: deleted
- Example scenario: wrong log group

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
