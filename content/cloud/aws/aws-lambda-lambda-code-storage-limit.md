---
title: "[Solution] AWS Lambda Code Storage Limit"
description: "CodeStorageExceededException when Lambda code is too large."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Code Storage Limit` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Total code size for all functions exceeds 75GB
- Function code size exceeds 250MB unzipped
- Container images exceed the image size limit
- Historical function versions accumulate storage
- Large dependencies not moved to Lambda Layers

## How to Fix

### Check account usage

```bash
aws lambda get-account-settings --query AccountUsage
```

### Delete old versions

```bash
aws lambda delete-function --function-name my-function --qualifier 3
```

## Examples

- Example scenario: total code size for all functions exceeds 75gb
- Example scenario: function code size exceeds 250mb unzipped
- Example scenario: container images exceed the image size limit
- Example scenario: historical function versions accumulate storage

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
