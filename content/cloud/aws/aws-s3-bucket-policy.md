---
title: "[Solution] AWS S3 bucket policy"
description: "Malformed/PolicyTooLong for bucket policy."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 bucket policy` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Size more than 20 KB
- Syntax error in principal
- Missing Action in statement

## How to Fix

### Get policy

```bash
aws s3api get-bucket-policy --bucket my-bucket
```

### Put new policy

```bash
aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json
```

## Examples

- Example scenario: size more than 20 kb
- Example scenario: syntax error in principal
- Example scenario: missing action in statement

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General s3 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
