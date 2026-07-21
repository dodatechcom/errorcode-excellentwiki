---
title: "[Solution] AWS Geolocation Routing"
description: "InvalidChangeBatch for geolocation."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Geolocation Routing` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Code invalid
- Overlapping scopes
- Default missing

## How to Fix

### List records

```bash
aws route53 list-resource-record-sets --hosted-zone ZONE123
```

## Examples

- Example scenario: code invalid
- Example scenario: overlapping scopes
- Example scenario: default missing

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
