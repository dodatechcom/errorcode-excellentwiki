---
title: "[Solution] AWS NLB Target Group Error — registration/health failures"
description: "Fix AWS NLB target group errors. Resolve NLB target registration, health check, and connection issues."
error-types: ["api-error"]
severities: ["error"]
weight: 114
---

An AWS NLB Target Group error occurs when targets fail to register, health checks fail, or connection tracking issues cause traffic drops. NLB operates at Layer 4 and has different health check behavior than ALB.

## Common Causes

- Target type mismatch (IP vs instance)
- Health check protocol does not match target port
- Security group or NACL blocks health check traffic
- Cross-zone load balancing disabled with single-AZ targets
- Connection tracking table full

## How to Fix

### Check Target Health

```bash
aws elbv2 describe-target-health \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-nlb-tg/xxx
```

### Describe Target Group Attributes

```bash
aws elbv2 describe-target-group-attributes \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-nlb-tg/xxx
```

### Register Targets

```bash
aws elbv2 register-targets \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-nlb-tg/xxx \
  --targets Id=i-xxx,Port=443
```

### Modify Health Check Settings

```bash
aws elbv2 modify-target-group \
  --target-group-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-nlb-tg/xxx \
  --health-check-protocol TCP \
  --health-check-port 80
```

### Enable Cross-Zone Load Balancing

```bash
aws elbv2 modify-load-balancer-attributes \
  --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/app/my-nlb/xxx \
  --attributes Key=load_balancing.cross_zone.enabled,Value=true
```

## Examples

```bash
# Example 1: Unhealthy target
# State: unhealthy, Reason: Target.Timeout
# Fix: verify TCP port is open and responding

# Example 2: Target registration failed
# InvalidTarget: Target not in VPC
# Fix: use IP target type for cross-VPC targets
```

## Related Errors

- [AWS ELB Error]({{< relref "/cloud/aws/aws-elb-error" >}}) — ALB/CLB health check errors
- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
