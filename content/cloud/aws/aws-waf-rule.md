---
title: "[Solution] AWS WAF Rule"
description: "WAFNonexistentRuleException."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `WAF Rule` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Rule name incorrect
- Deleted but still used

## How to Fix

### List WAF rules

```bash
aws wafv2 list-rules --scope REGIONAL
```

## Examples

- Example scenario: rule name incorrect
- Example scenario: deleted but still used

## Related Errors

- [AWS APIGW Error]({{< relref "/cloud/aws/aws-api-gateway-error" >}}) -- General apigw errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
