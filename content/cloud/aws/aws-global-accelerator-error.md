---
title: "[Solution] AWS Global Accelerator Error — endpoint/accelerator failures"
description: "Fix AWS Global Accelerator errors. Resolve accelerator, endpoint, and traffic routing issues."
error-types: ["api-error"]
severities: ["error"]
weight: 108
---

An AWS Global Accelerator error occurs when accelerators fail to provision, endpoints become unhealthy, or traffic routing malfunctions. This can be due to endpoint configuration, health checks, or AWS Global Accelerator limits.

## Common Causes

- Accelerator is in a non-configurable state
- Endpoint health check failures
- Maximum endpoints per accelerator exceeded
- Cross-account endpoint permissions missing
- Static IP address allocation limits reached

## How to Fix

### Check Accelerator Status

```bash
aws globalaccelerator describe-accelerator \
  --accelerator-arn arn:aws:globalaccelerator::123456789012:accelerator/xxx
```

### List Endpoints

```bash
aws globalaccelerator describe-endpoint-group \
  --endpoint-group-arn arn:aws:globalaccelerator::123456789012:accelerator/xxx/endpoint-group/us-east-1
```

### Create Listener

```bash
aws globalaccelerator create-listener \
  --accelerator-arn arn:aws:globalaccelerator::123456789012:accelerator/xxx \
  --port-ranges FromPort=80,ToPort=80 \
  --protocol TCP
```

### Update Endpoint Group

```bash
aws globalaccelerator update-endpoint-group \
  --endpoint-group-arn arn:aws:globalaccelerator::123456789012:accelerator/xxx/endpoint-group/us-east-1 \
  --endpoint-configurations EndpointId=i-xxx,Weight=100,HealthCheckPort=80
```

### Check Accelerator Health

```bash
aws globalaccelerator describe-accelerator-health \
  --accelerator-arn arn:aws:globalaccelerator::123456789012:accelerator/xxx
```

## Examples

```bash
# Example 1: Endpoint unhealthy
# EndpointHealth: State = UNHEALTHY
# Fix: verify EC2 instance or ALB is running and healthy

# Example 2: Accelerator not found
# NotFoundException: Accelerator not found
# Fix: verify accelerator ARN and region
```

## Related Errors

- [AWS ELB Error]({{< relref "/cloud/aws/aws-elb-error" >}}) — Load balancer errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS CloudFront Error]({{< relref "/cloud/aws/aws-cloudfront-error" >}}) — CloudFront distribution errors
