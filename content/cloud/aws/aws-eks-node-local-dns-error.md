---
title: "[Solution] EKS Node Local DNS Cache Error"
description: "Resolve EKS node local DNS cache errors when DNS resolution is inconsistent across nodes."
cloud: ["aws"]
error-types: ["cloud-error"]
---

# [Solution] EKS Node Local DNS Cache Error

Resolve EKS node local DNS cache errors when DNS resolution is inconsistent across nodes.

## Common Causes

- Misconfiguration of the AWS service or resource
- Insufficient IAM permissions for the operation
- Resource limits or quotas exceeded
- Network connectivity issues between services
- Incorrect resource identifiers or ARNs

## How to Fix

### Check Current Configuration

```bash
aws cloudformation describe-stacks --stack-name my-stack 2>/dev/null || echo "Check resource configuration"
```

### Verify IAM Permissions

```bash
aws iam simulate-principal-policy   --policy-source-arn arn:aws:iam::123456789:role/my-role   --action-names "s3:GetObject"   --resource-arns "arn:aws:s3:::my-bucket/*"
```

### Check Service Quotas

```bash
aws service-quotas list-services   --query "Services[?contains(ServiceCode,'ec2')]"
```

### Review CloudWatch Logs

```bash
aws logs filter-log-events   --log-group-name /aws/aws-eks-node-local-dns-error   --start-time $(date -d '1 hour ago' +%s)000   --filter-pattern "ERROR"
```

### Enable Detailed Error Logging

```bash
aws eks describe-* 2>&1 | head -50
```

## Examples

```bash
# Example 1: Common configuration error
# The operation failed due to invalid parameters
# Fix: verify all parameters match the expected format

# Example 2: Permission error
# AccessDenied: User is not authorized to perform this action
# Fix: attach the required IAM policy to the role
```

## Related Errors

- [AWS IAM Error]({< relref "/cloud/aws/aws-iam-error" >})
- [AWS Service Quota]({< relref "/cloud/aws/aws-service-quota" >})
