---
title: "[Solution] AWS Dashboard"
description: "InvalidParameter for dashboards."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Dashboard` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- JSON invalid
- Name > 255 chars
- Widget unsupported

## How to Fix

### List dashboards

```bash
aws cloudwatch list-dashboards
```

## Examples

- Example scenario: json invalid
- Example scenario: name > 255 chars
- Example scenario: widget unsupported

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
