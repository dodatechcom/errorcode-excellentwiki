---
title: "[Solution] AWS Systems Manager Error"
description: "Fix AWS Systems Manager errors. Resolve SSM parameter and patch issues."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

An AWS Systems Manager error occurs when SSM operations fail due to agent, permission, or configuration issues.

## Common Causes

- SSM agent not installed or not running on the instance
- IAM instance profile lacks SSM permissions
- Instance is not managed (not in managed instance inventory)
- Parameter Store parameter does not exist
- Patch baseline not associated with the instance

## How to Fix

### Check Managed Instances

```bash
aws ssm describe-instance-information
```

### Check SSM Agent Status

```bash
# On the instance
sudo systemctl status amazon-ssm-agent
```

### Send Command

```bash
aws ssm send-command \
  --instance-ids i-xxx \
  --document-name "AWS-RunShellScript" \
  --parameters 'commands=["echo hello"]'
```

### Get Parameter

```bash
aws ssm get-parameter --name /myapp/config
aws ssm get-parameters-by-path --path /myapp/
```

### Verify Instance Role

```bash
aws iam list-instance-profiles-for-role --role-name my-ec2-role
```

## Examples

```bash
# Example 1: Agent not running
# Instance i-xxx is not managed
# Fix: install and start SSM agent

# Example 2: Parameter not found
# ParameterNotFound: /myapp/config not found
# Fix: aws ssm put-parameter --name /myapp/config --value "xxx"
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance error
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission denied
