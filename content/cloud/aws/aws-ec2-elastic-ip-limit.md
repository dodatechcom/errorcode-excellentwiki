---
title: "[Solution] AWS EC2 Elastic IP Address Limit"
description: "AddressLimitExceeded when the account has reached the maximum EIPs."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Elastic IP Address Limit` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Default limit of 5 EIPs per region reached
- EIPs on stopped instances still count
- Multiple EIPs allocated but not associated
- VPC-Classic has separate limit

## How to Fix

### Check EIP count

```bash
aws ec2 describe-addresses --query 'Addresses[*].[PublicIp,AllocationId,AssociationId]' --output table
```
### Release unused EIPs

```bash
aws ec2 release-address --allocation-id eipalloc-0abc123
```
### Request limit increase

```bash
aws service-quotas request-service-quota-increase --service-code ec2 --quota-code L-0263D0A6 --desired-value 10 --region us-east-1
```

## Examples

- 5 EIPs allocated but only 2 associated
- Trying to allocate 6th EIP when limit is 5

## Related Errors

- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [VPC Limit]({{< relref "/cloud/aws/aws-ec2-vpc-limit" >}}) -- VPC limits
