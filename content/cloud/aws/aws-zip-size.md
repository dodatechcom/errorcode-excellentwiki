---
title: "[Solution] AWS ZIP size"
description: "InvalidParameterException zip more than 50MB."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ZIP size` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Direct zip limited to 50MB
- Can use S3 for larger

## How to Fix

### Check size

```bash
ls -lh my-function.zip
```

## Examples

- Example scenario: direct zip limited to 50mb
- Example scenario: can use s3 for larger

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
