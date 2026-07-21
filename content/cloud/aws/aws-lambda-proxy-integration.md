---
title: "[Solution] AWS Lambda Proxy Integration"
description: "InternalServerError for Lambda proxy."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Proxy Integration` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Lambda not exist
- Invalid response format
- Role insufficient

## How to Fix

### Check Lambda response

```bash
aws lambda invoke --function my-function response.json
```

## Examples

- Example scenario: lambda not exist
- Example scenario: invalid response format
- Example scenario: role insufficient

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
