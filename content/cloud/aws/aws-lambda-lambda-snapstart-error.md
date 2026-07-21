---
title: "[Solution] AWS Lambda SnapStart Error"
description: "SnapStartNotSupported/SnapStartCreateUpdateFailed for Lambda SnapStart."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda SnapStart Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Function code has network connections on init
- Unique identifiers generated during initialization
- Temporary credentials fetched during init
- Larger initial state takes longer to snapshot
- Runtime does not support SnapStart

## How to Fix

### Enable SnapStart

```bash
aws lambda update-function-configuration --function-name my-function --snap-start ApplyOn=PublishedVersions
```

## Examples

- Example scenario: function code has network connections on init
- Example scenario: unique identifiers generated during initialization
- Example scenario: temporary credentials fetched during init
- Example scenario: larger initial state takes longer to snapshot

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
