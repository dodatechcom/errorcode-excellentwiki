---
title: "[Solution] AWS Health Check"
description: "NoSuchHealthCheck."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Health Check` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- ID not exist
- Config invalid

## How to Fix

### List health checks

```bash
aws route53 list-health-checks
```

## Examples

- Example scenario: id not exist
- Example scenario: config invalid

## Related Errors

- [AWS ROUTE53 Error]({{< relref "/cloud/aws/aws-route53-error" >}}) -- General route53 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
