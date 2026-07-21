---
title: "[Solution] AWS Distribution Not Found"
description: "NoSuchDistribution for CloudFront."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Distribution Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- ID incorrect
- Deleted
- Other account

## How to Fix

### List distributions

```bash
aws cloudfront list-distributions
```

## Examples

- Example scenario: id incorrect
- Example scenario: deleted
- Example scenario: other account

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
