---
title: "[Solution] AWS SSL Cert Not Found"
description: "InvalidViewerCertificate."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `SSL Cert Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- ACM cert not in us-east-1
- Doesn't match CNAME
- Expired

## How to Fix

### List certs

```bash
aws acm list-certificates --region us-east-1
```

## Examples

- Example scenario: acm cert not in us-east-1
- Example scenario: doesn't match cname
- Example scenario: expired

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
