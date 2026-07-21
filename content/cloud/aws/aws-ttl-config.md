---
title: "[Solution] AWS TTL Config"
description: "InvalidArgumentException for TTL."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `TTL Config` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Min > max TTL
- Default > max TTL

## How to Fix

### Update distribution

```bash
aws cloudfront update-distribution --id E123EXAMPLE --config file://config.json
```

## Examples

- Example scenario: min > max ttl
- Example scenario: default > max ttl

## Related Errors

- [AWS DYNAMODB Error]({{< relref "/cloud/aws/aws-dynamodb-error" >}}) -- General dynamodb errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
