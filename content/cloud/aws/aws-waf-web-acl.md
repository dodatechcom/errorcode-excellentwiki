---
title: "[Solution] AWS WAF Web ACL"
description: "InvalidWebACLId for CloudFront WAF."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `WAF Web ACL` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- ACL not for CloudFront
- Must be us-east-1

## How to Fix

### List web ACLs

```bash
aws wafv2 list-web-acls --scope CLOUDFRONT
```

## Examples

- Example scenario: acl not for cloudfront
- Example scenario: must be us-east-1

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
