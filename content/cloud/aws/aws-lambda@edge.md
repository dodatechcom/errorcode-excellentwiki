---
title: "[Solution] AWS Lambda@Edge"
description: "LambdaAtEdgeError CloudFront triggers."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda@Edge` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Viewer events limited to 128MB
- Function not in us-east-1
- Timeout more than 5s for viewer

## How to Fix

### Check size

```bash
aws lambda get-function --function my-function --query CodeSize
```

## Examples

- Example scenario: viewer events limited to 128mb
- Example scenario: function not in us-east-1
- Example scenario: timeout more than 5s for viewer

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
