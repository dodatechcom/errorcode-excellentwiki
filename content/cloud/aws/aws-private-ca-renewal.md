---
title: "[Solution] AWS Private CA Renewal"
description: "ResourceNotFound for private CA cert."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Private CA Renewal` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- CA not exist
- CA suspended

## How to Fix

### List CAs

```bash
aws acm-pca list-certificate-authorities
```

## Examples

- Example scenario: ca not exist
- Example scenario: ca suspended

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
