---
title: "[Solution] AWS Service Role"
description: "InvalidServiceRole for service-linked roles."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Service Role` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Trust policy missing service principal

## How to Fix

### Check role

```bash
aws iam get-role --role AWSServiceRoleForAmazonElasticsearchService
```

## Examples

- Example scenario: trust policy missing service principal

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) -- General iam errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
