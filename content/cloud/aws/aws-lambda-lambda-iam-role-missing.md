---
title: "[Solution] AWS Lambda IAM Role Missing"
description: "InvalidParameterValueException for IAM role in Lambda."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda IAM Role Missing` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- IAM role ARN is invalid or does not exist
- IAM role was deleted after function creation
- IAM role is in a different AWS account
- IAM trust policy does not allow Lambda service
- IAM role path mismatch in ARN

## How to Fix

### Verify IAM role

```bash
aws iam get-role --role-name my-lambda-role
```

### Check trust policy

```bash
aws iam get-role --role-name my-lambda-role --query Role.AssumeRolePolicyDocument
```

## Examples

- Example scenario: iam role arn is invalid or does not exist
- Example scenario: iam role was deleted after function creation
- Example scenario: iam role is in a different aws account
- Example scenario: iam trust policy does not allow lambda service

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
