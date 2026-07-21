---
title: "[Solution] AWS CNAME Already Exists"
description: "CNAMEAlreadyExists."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `CNAME Already Exists` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Already associated with another dist
- Other account

## How to Fix

### List aliases

```bash
aws cloudfront get-distribution --id E123EXAMPLE --query Aliases
```

## Examples

- Example scenario: already associated with another dist
- Example scenario: other account

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
