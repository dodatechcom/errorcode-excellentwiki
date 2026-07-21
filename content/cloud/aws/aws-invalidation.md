---
title: "[Solution] AWS Invalidation"
description: "InvalidArgumentException for invalidations."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Invalidation` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Path format wrong
- Too many items

## How to Fix

### Create invalidation

```bash
aws cloudfront create-invalidation --id E123EXAMPLE --paths /images/*
```

## Examples

- Example scenario: path format wrong
- Example scenario: too many items

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
