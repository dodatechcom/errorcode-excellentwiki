---
title: "[Solution] AWS EC2 Dedicated Host Error"
description: "HostLimitExceeded or InvalidParameterValue for Dedicated Hosts."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Dedicated Host Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- Max Dedicated Hosts per region exceeded
- Instance type not supported on host
- Release of host still has instances running
- Auto-placement misconfigured

## How to Fix

### List dedicated hosts

```bash
aws ec2 describe-hosts --query 'Hosts[*].[HostId,State,InstanceType]' --output table
```
### Allocate dedicated host

```bash
aws ec2 allocate-hosts --instance-type m5.large --availability-zone us-east-1a --quantity 2
```
### Release dedicated host

```bash
aws ec2 release-hosts --host-ids h-0abc123
```

## Examples

- Trying to allocate 11th host when limit is 10
- Launching c5.4xlarge on host configured for m5.large

## Related Errors

- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [Instance Limit]({{< relref "/cloud/aws/aws-ec2-instance-limit-exceeded" >}}) -- Instance limits
