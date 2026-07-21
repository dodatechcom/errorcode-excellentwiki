---
title: "[Solution] AWS Lambda Handler Not Found"
description: "HandlerNotFound when the Lambda function handler does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Handler Not Found` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Handler value does not match the exported function name
- Code does not contain the specified handler path
- Handler missing the file extension (.py, .js)
- Lambda runtime unable to locate the module
- Handler is in a subdirectory not in PATH

## How to Fix

### Check handler config

```bash
aws lambda get-function-configuration --function-name my-function
```

### Update handler

```bash
aws lambda update-function-configuration --function-name my-function --handler index.handler
```

## Examples

- Example scenario: handler value does not match the exported function name
- Example scenario: code does not contain the specified handler path
- Example scenario: handler missing the file extension (.py, .js)
- Example scenario: lambda runtime unable to locate the module

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
