---
title: "[Solution] AWS WAF Association"
description: "BadRequestException for WAF."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `WAF Association` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Regional web ACL not exist
- ACL version mismatch

## How to Fix

### List for resource

```bash
aws wafv2 list-resources-for-web-acl --web-acl-arn arn:aws:waf...
```

## Examples

- Example scenario: regional web acl not exist
- Example scenario: acl version mismatch

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
