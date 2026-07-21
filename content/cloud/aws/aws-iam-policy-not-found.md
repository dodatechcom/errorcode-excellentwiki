---
title: "[Solution] AWS IAM Policy Not Found"
description: "ResourceNotFoundException for policies."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `IAM Policy Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Policy not found
- Recently deleted

## How to Fix

### List policies

```bash
aws iam list-policies --scope AWS
```

## Examples

- Example scenario: policy not found
- Example scenario: recently deleted

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
