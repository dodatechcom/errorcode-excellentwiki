---
title: "[Solution] AWS Lambda ENI Creation Error"
description: "ENILimit/InsufficientIP for Lambda VPC ENI creation."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `Lambda ENI Creation Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Elastic Network Interface per region limit reached
- VPC does not have enough available IPs
- Security group max rules exceeded
- Rate limiting on EC2 API calls for ENI creation
- VPC does not have DHCP options set

## How to Fix

### Check ENI count

```bash
aws ec2 describe-network-interfaces --filters Name=vpc-id,Values=vpc-abc
```

### Release unused ENIs

```bash
aws ec2 delete-network-interface --network-interface-id eni-abc
```

## Examples

- Example scenario: elastic network interface per region limit reached
- Example scenario: vpc does not have enough available ips
- Example scenario: security group max rules exceeded
- Example scenario: rate limiting on ec2 api calls for eni creation

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [AWS CloudWatch Error]({{< relref "/cloud/aws/aws-cloudwatch-error" >}}) -- CloudWatch errors
