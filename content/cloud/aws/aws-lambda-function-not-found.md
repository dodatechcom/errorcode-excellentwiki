---
title: "[Solution] AWS Lambda Function Not Found"
description: "ResourceNotFoundException when the specified Lambda function does not exist."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda Function Not Found` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- Function name or ARN is incorrect
- Function was deleted
- Function is in a different region
- IAM role lacks lambda:GetFunction permission

## How to Fix

### List functions

```bash
aws lambda list-functions --query "Functions[*].[FunctionName,LastModified]" --output table
```
### Get function

```bash
aws lambda get-function --function-name my-function
```
### Create function

```bash
aws lambda create-function --function-name my-function --runtime python3.11 --role arn:aws:iam::123456789012:role/lambda-role --handler index.handler --zip-file fileb://function.zip
```

## Examples

- Calling get-function with my-function but function is named myFunc
- Function my-old-fn deleted last week

## Related Errors

- [Lambda Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General Lambda errors
- [Handler Not Found]({{< relref "/cloud/aws/aws-lambda-handler-not-found" >}}) -- Handler issues
