---
title: "[Solution] AWS OAI/OAC"
description: "OriginAccessControlNotFound."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `OAI/OAC` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- OAC not enabled
- OAI ID not exist

## How to Fix

### Create OAC

```bash
aws cloudfront create-origin-access-control --config file://oac.json
```

## Examples

- Example scenario: oac not enabled
- Example scenario: oai id not exist

## Related Errors

- [AWS CLOUDFRONT Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) -- General cloudfront errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
