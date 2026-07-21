---
title: "[Solution] AWS Origin Not Accessible"
description: "OriginAccessDenied for origin."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Origin Not Accessible` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Bucket policy missing CloudFront
- Different account
- OAI/OAC incorrect

## How to Fix

### Check origin

```bash
aws cloudfront get-distribution --id E123EXAMPLE
```

## Examples

- Example scenario: bucket policy missing cloudfront
- Example scenario: different account
- Example scenario: oai/oac incorrect

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
