---
title: "[Solution] AWS CodeDeploy Error — deployment-group/agent/hook failures"
description: "Fix AWS CodeDeploy errors. Resolve deployment group, agent, and lifecycle hook issues."
error-types: ["api-error"]
severities: ["error"]
weight: 153
---

An AWS CodeDeploy error occurs when deployments fail, lifecycle hooks encounter errors, or the CodeDeploy agent cannot communicate with the service. CodeDeploy automates code deployments but requires proper IAM and agent configuration.

## Common Causes

- CodeDeploy agent not installed or not running on instances
- IAM instance profile lacks CodeDeploy permissions
- Deployment group has no healthy instances
- AppSpec.yml references nonexistent Lambda functions
- Rollback trigger not configured

## How to Fix

### List Deployments

```bash
aws deploy list-deployments \
  --application-name my-app \
  --query 'deployments'
```

### Get Deployment Status

```bash
aws deploy get-deployment \
  --deployment-id d-xxx \
  --query 'deploymentInfo.{Status:status,Error:errorMessage}'
```

### Create Application

```bash
aws deploy create-application \
  --application-name my-app \
  --compute-platform Server
```

### Create Deployment Group

```bash
aws deploy create-deployment-group \
  --application-name my-app \
  --deployment-group-name my-dg \
  --service-role-arn arn:aws:iam::123456789012:role/CodeDeployRole \
  --auto-scaling-groups my-asg
```

### Create Deployment

```bash
aws deploy create-deployment \
  --application-name my-app \
  --deployment-group-name my-dg \
  --revision '{"revisionType":"S3","s3Location":{"bucket":"my-bucket","key":"appspec.yml"}}'
```

## Examples

```bash
# Example 1: Agent not communicating
# The deployment failed because the CodeDeploy agent was not found
# Fix: install and start codedeploy-agent on instances

# Example 2: Deployment failed
# HEALTH_CONSTRAINTS: No healthy instances in deployment group
# Fix: verify ASG has running instances
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 artifact errors
