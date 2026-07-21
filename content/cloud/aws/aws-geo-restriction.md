---
title: "[Solution] AWS Geo Restriction"
description: "IllegalUpdate for geo restriction."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Geo Restriction` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Invalid location code
- Both whitelist and blocklist

## How to Fix

### Update geo

```bash
aws cloudfront update-distribution --id E123EXAMPLE --config file://config.json
```

## Examples

- Example scenario: invalid location code
- Example scenario: both whitelist and blocklist

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
