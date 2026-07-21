---
title: "[Solution] AWS SnapStart error"
description: "SnapStartNotSupported for Lambda SnapStart."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SnapStart error` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Network connections during init
- UUID seeded during init
- Temp credentials fetched during init

## How to Fix

### Set SnapStart

```bash
aws lambda update-function-config --function my-function --snap ApplyOn=Published
```

## Examples

- Example scenario: network connections during init
- Example scenario: uuid seeded during init
- Example scenario: temp credentials fetched during init

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
