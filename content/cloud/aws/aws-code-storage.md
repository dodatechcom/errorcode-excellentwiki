---
title: "[Solution] AWS Code Storage"
description: "CodeStorageExceeded storage limit."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Code Storage` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Total code more than 75GB across functions
- Function code more than 250MB unzipped

## How to Fix

### Check usage

```bash
aws lambda get-account-settings --query AccountUsage
```

## Examples

- Example scenario: total code more than 75gb across functions
- Example scenario: function code more than 250mb unzipped

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
