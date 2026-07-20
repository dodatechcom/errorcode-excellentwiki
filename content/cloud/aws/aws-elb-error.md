---
title: "[Solution] AWS ELB Error — health check/target group failures"
description: "Fix AWS ELB errors. Resolve Classic, ALB, and NLB health check and target group issues."
error-types: ["api-error"]
severities: ["error"]
weight: 107
---

An AWS ELB error occurs when load balancers fail health checks, targets become unhealthy, or traffic routing fails. This can be caused by misconfigured health checks, security groups, or target registration issues.

## Common Causes

- Health check path or port misconfigured
- Target instances fail health check responses
- Security groups block health check traffic
- Target group has no registered targets
- Cross-zone load balancing issues

## How to Fix

### Check Load Balancer Health

```bash
aws elbv2 describe-target-health \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-tg/xxx
```

### Verify Health Check Configuration

```bash
aws elbv2 describe-target-group-attributes \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-tg/xxx
```

### Register Targets

```bash
aws elbv2 register-targets \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-tg/xxx \
  --targets Id=i-xxx Id=i-yyy
```

### Update Health Check Settings

```bash
aws elbv2 modify-target-group \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-tg/xxx \
  --health-check-path /health \
  --health-check-interval-seconds 15 \
  --healthy-threshold-count 3
```

### Describe Load Balancer

```bash
aws elbv2 describe-load-balancers \
  --names my-alb
```

## Examples

```bash
# Example 1: Unhealthy targets
# TargetHealthDescription: State = unhealthy, Reason = Target.FailedHealthChecks
# Fix: verify health check endpoint responds 200 OK

# Example 2: No targets registered
# TargetGroupNotFound: Target group not found
# Fix: register targets with register-targets
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) — CloudWatch monitoring errors
