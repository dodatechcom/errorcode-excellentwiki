---
title: "[Solution] AWS Certificate Renewal"
description: "ValidationException for renewal."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Certificate Renewal` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Email validation pending
- DNS records missing
- CAA records blocking

## How to Fix

### Describe cert

```bash
aws acm describe-certificate --certificate-arn arn:aws:acm::123:certificate/xxx
```

## Examples

- Example scenario: email validation pending
- Example scenario: dns records missing
- Example scenario: caa records blocking

## Related Errors

- [AWS KMS Error]({{< relref "/cloud/aws/aws-kms-error" >}}) -- General kms errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
