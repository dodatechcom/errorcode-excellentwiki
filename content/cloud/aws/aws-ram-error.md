---
title: "[Solution] AWS RAM Error — share/invite/participation failures"
description: "Fix AWS RAM errors. Resolve Resource Access Manager share, invite, and resource association issues."
error-types: ["api-error"]
severities: ["error"]
weight: 121
---

An AWS RAM error occurs when resource shares fail to create, invites are not accepted, or shared resources become unavailable. RAM lets you share AWS resources across accounts but requires proper invitation and permission handling.

## Common Causes

- Resource share invitation expired or rejected
- Target account is not in the same organization
- IAM permissions not updated for shared resource
- Resource type not shareable via RAM
- Principal not associated with resource share

## How to Fix

### List Resource Shares

```bash
aws ram get-resource-shares \
  --resource-owner SELF \
  --query 'resourceShares[*].{ID:resourceShareArn,Name:name,Status:status}'
```

### Get Shared Resources

```bash
aws ram get-resources \
  --resource-owner SELF
```

### Accept Invitation

```bash
aws ram accept-resource-share-invitation \
  --resource-share-invitation-id invite-xxx
```

### Create Resource Share

```bash
aws ram create-resource-share \
  --name my-share \
  --resource-arns arn:aws:ec2:us-east-1:123456789012:subnet/subnet-xxx
```

### Associate Principal

```bash
aws ram associate-resource-share \
  --resource-share-arn arn:aws:ram:us-east-1:123456789012:resource-share/xxx \
  --principals 098765432109
```

## Examples

```bash
# Example 1: Invitation expired
# InvalidParameterException: Invitation has expired
# Fix: ask resource owner to send new invitation

# Example 2: Resource not shareable
# InvalidParameterException: Resource type not supported
# Fix: check which resource types RAM supports
```

## Related Errors

- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS Organizations Error]({{< relref "/cloud/aws/aws-organizations-error" >}}) — Organizations errors
- [AWS CloudFormation Error]({{< relref "/cloud/aws/aws-cloudformation-error" >}}) — CloudFormation errors
