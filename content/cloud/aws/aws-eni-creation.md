---
title: "[Solution] AWS ENI creation"
description: "ENILimit/InsufficientIP for ENI creation."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `ENI creation` error occurs when a AWS service cannot complete the requested operation.

## Common Causes

- ENI region limit reached
- VPC exhausted IPs
- Rate limiting on EC2 API

## How to Fix

### Check ENI count

```bash
aws ec2 describe-network-interfaces --f vpc,vpc-abc
```

## Examples

- Example scenario: eni region limit reached
- Example scenario: vpc exhausted ips
- Example scenario: rate limiting on ec2 api

## Related Errors

- [AWS LAMBDA Error]({{< relref "/cloud/aws/aws-lambda-error" >}}) -- General lambda errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
