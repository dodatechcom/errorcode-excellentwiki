---
title: "[Solution] AWS CloudFormation Stack Failed"
description: "Fix AWS CloudFormation stack failures. Resolve CloudFormation deployment issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

A CloudFormation stack failed error occurs when a CloudFormation stack cannot be created, updated, or deleted. This can be caused by resource creation failures, IAM issues, or template errors.

## Common Causes

- Template syntax errors or invalid resource properties
- IAM role lacks permissions to create resources
- Resource limit exceeded (e.g., EC2 instances)
- Circular dependency in the template
- Resource deletion protection enabled

## How to Fix

### Check Stack Events

```bash
aws cloudformation describe-stack-events --stack-name my-stack \
  --query 'StackEvents[?ResourceStatus==`CREATE_FAILED`]'
```

### Validate Template

```bash
aws cloudformation validate-template --template-body file://template.yaml
```

### Check Stack Status

```bash
aws cloudformation describe-stacks --stack-name my-stack \
  --query 'Stacks[*].StackStatus'
```

### Delete Failed Stack

```bash
aws cloudformation delete-stack --stack-name my-stack
```

### Roll Back Changes

```bash
aws cloudformation cancel-update-stack --stack-name my-stack
```

## Examples

```bash
# Example 1: IAM permission
# CREATE_FAILED: arn:aws:iam::...:role/my-role
# Fix: add iam:CreateRole permission

# Example 2: Resource limit
# CREATE_FAILED: Instance limit exceeded
# Fix: request quota increase or use different instance type
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 launch failed
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
