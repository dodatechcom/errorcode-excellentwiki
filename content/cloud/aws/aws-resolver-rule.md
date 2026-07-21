---
title: "[Solution] AWS Resolver Rule"
description: "ResourceNotFoundException for resolver."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Resolver Rule` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Rule ID not exist
- Type mismatch

## How to Fix

### List rules

```bash
route53resolver list-resolver-rules
```

## Examples

- Example scenario: rule id not exist
- Example scenario: type mismatch

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
