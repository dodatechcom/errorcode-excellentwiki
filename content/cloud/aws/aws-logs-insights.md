---
title: "[Solution] AWS Logs Insights"
description: "InvalidQueryException for Logs Insights."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Logs Insights` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Syntax error
- Log group not found
- Query timeout

## How to Fix

### Query logs

```bash
aws logs start-query --log-group-names /aws/lambda/myFunc --query file://query.json
```

## Examples

- Example scenario: syntax error
- Example scenario: log group not found
- Example scenario: query timeout

## Related Errors

- [AWS CLOUDWATCH Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- General cloudwatch errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
