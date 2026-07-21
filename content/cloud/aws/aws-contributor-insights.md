---
title: "[Solution] AWS Contributor Insights"
description: "AccessDenied for Contributor Insights."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Contributor Insights` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Rule not found
- S3 bucket not configured

## How to Fix

### List rules

```bash
aws logs describe-resource-policies
```

## Examples

- Example scenario: rule not found
- Example scenario: s3 bucket not configured

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
