---
title: "[Solution] AWS Lambda@Edge Error"
description: "LambdaAtEdgeError when CloudFront triggers fail."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda@Edge Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Function exceeds 128MB limit for viewer-request/response
- Function exceeds 1MB size limit for all CloudFront events
- Function is not in us-east-1 region
- IAM role not replicated to us-east-1
- Invalid trigger event type specified
- Edge function timeout exceeds 5s for viewer events

## How to Fix

### Check function size

```bash
aws lambda get-function --function-name my-function --query Configuration.CodeSize
```

### List function versions

```bash
aws lambda list-versions-by-function --function-name my-function
```

## Examples

- Example scenario: function exceeds 128mb limit for viewer-request/response
- Example scenario: function exceeds 1mb size limit for all cloudfront events
- Example scenario: function is not in us-east-1 region
- Example scenario: iam role not replicated to us-east-1

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
