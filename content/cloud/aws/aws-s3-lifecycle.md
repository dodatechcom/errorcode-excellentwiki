---
title: "[Solution] AWS S3 Lifecycle"
description: "MalformedXML/InvalidRequest for lifecycle rules."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `S3 Lifecycle` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Rule ID duplicate
- Date format invalid
- 128KB min for transitions

## How to Fix

### Get lifecycle

```bash
aws s3api get-bucket-lifecycle-config --bucket my-bucket
```

## Examples

- Example scenario: rule id duplicate
- Example scenario: date format invalid
- Example scenario: 128kb min for transitions

## Related Errors

- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) -- General s3 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
