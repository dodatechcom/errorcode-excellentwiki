---
title: "[Solution] AWS Viewer Protocol"
description: "InvalidProtocolException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Viewer Protocol` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- HTTPS only without SSL cert
- Policy mismatch

## How to Fix

### Update behavior

```bash
aws cloudfront update-distribution --id E123EXAMPLE --behavior file://behavior.json
```

## Examples

- Example scenario: https only without ssl cert
- Example scenario: policy mismatch

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
