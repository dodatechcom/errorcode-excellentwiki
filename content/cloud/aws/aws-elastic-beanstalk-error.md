---
title: "[Solution] AWS Elastic Beanstalk Error — deployment/env/health failures"
description: "Fix AWS Elastic Beanstalk errors. Resolve Beanstalk deployment, environment, and health issues."
error-types: ["api-error"]
severities: ["error"]
weight: 103
---

An AWS Elastic Beanstalk error occurs when deployments fail, environments become unhealthy, or health checks report issues. This can be caused by configuration problems, resource limits, or application errors.

## Common Causes

- Application health status Degraded or Severe
- Deployment timeouts or rolling update failures
- Insufficient instance capacity
- Missing .ebextensions configuration
- Environment tier mismatch (Web vs Worker)

## How to Fix

### Check Environment Health

```bash
aws elasticbeanstalk describe-environments \
  --environment-name my-env \
  --query 'Environments[*].Health'
```

### View Events

```bash
aws elasticbeanstalk describe-events \
  --environment-name my-env \
  --max-items 20
```

### Check Instance Health

```bash
aws elasticbeanstalk describe-instances-health \
  --environment-name my-env
```

### Update Environment Configuration

```bash
aws elasticbeanstalk update-environment \
  --environment-name my-env \
  --option-namespace aws:autoscaling:launchconfiguration \
  --option-name InstanceType \
  --option-value t3.medium
```

### Terminate and Recreate Environment

```bash
aws elasticbeanstalk terminate-environment \
  --environment-name my-env
```

## Examples

```bash
# Example 1: Deployment timeout
# ERROR: Deployment timed out
# Fix: increase DeploymentTimeout or use RollingWithAdditionalBatch

# Example 2: Health degraded
# Environment health has transitioned from Ok to Degraded
# Fix: check CloudWatch logs and application configuration
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS ELB Error]({{< relref "/cloud/aws/aws-elb-error" >}}) — Load balancer errors
- [AWS CloudFormation Error]({{< relref "/cloud/aws/aws-cloudformation-error" >}}) — CloudFormation errors
