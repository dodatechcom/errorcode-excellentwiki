---
title: "[Solution] AWS App Runner Error — build/connection/scaling failures"
description: "Fix AWS App Runner errors. Resolve App Runner build, connection, and auto-scaling issues."
error-types: ["api-error"]
severities: ["error"]
weight: 104
---

An AWS App Runner error occurs when service builds fail, connections time out, or auto-scaling behaves unexpectedly. This can be due to source configuration, networking, or build errors.

## Common Causes

- Source code build configuration errors
- VPC connector misconfiguration
- Auto-scaling settings too aggressive
- Custom domain certificate validation failures
- Service role lacks required permissions

## How to Fix

### Check Service Status

```bash
aws apprunner describe-service \
  --service-arn arn:aws:apprunner:us-east-1:123456789012:service/my-service
```

### View Operation Status

```bash
aws apprunner list-operations \
  --service-arn arn:aws:apprunner:us-east-1:123456789012:service/my-service
```

### Create VPC Connector

```bash
aws apprunner create-vpc-connector \
  --connector-name my-connector \
  --subnets subnet-xxx subnet-yyy \
  --security-groups sg-xxx
```

### Update Auto Scaling

```bash
aws apprunner update-service \
  --service-arn arn:aws:apprunner:us-east-1:123456789012:service/my-service \
  --auto-scaling-configuration Arn=arn:aws:apprunner:::auto-scaling-configuration/my-config
```

### Start Deployment

```bash
aws apprunner start-deployment \
  --service-arn arn:aws:apprunner:us-east-1:123456789012:service/my-service
```

## Examples

```bash
# Example 1: Build failure
# OperationFailedException: Build failed
# Fix: check build command and source configuration

# Example 2: Connection timeout
# ServiceTimeoutException: Connection timed out
# Fix: verify VPC connector and security groups
```

## Related Errors

- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error" >}}) — ECS service errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
