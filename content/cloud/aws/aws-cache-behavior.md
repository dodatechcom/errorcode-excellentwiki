---
title: "[Solution] AWS Cache Behavior"
description: "InvalidArgumentException for behavior."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Cache Behavior` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Path pattern conflicts
- Priority ambiguous

## How to Fix

### Get config

```bash
aws cloudfront get-distribution-config --id E123EXAMPLE
```

## Examples

- Example scenario: path pattern conflicts
- Example scenario: priority ambiguous

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
