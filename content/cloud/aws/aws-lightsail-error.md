---
title: "[Solution] AWS Lightsail Error — instance/disk/network failures"
description: "Fix AWS Lightsail errors. Resolve Lightsail instance, disk, and networking issues."
error-types: ["api-error"]
severities: ["error"]
weight: 106
---

An AWS Lightsail error occurs when instances fail to start, disks become unavailable, or networking configurations cause connectivity issues. Lightsail simplifies EC2 management but can still encounter resource and configuration errors.

## Common Causes

- Instance plan limit exceeded
- Disk size exceeds plan maximum
- Static IP not attached to instance
- Firewall rules block required ports
- Snapshot restore fails due to incompatible plan

## How to Fix

### Check Instance Status

```bash
aws lightsail get-instance-state \
  --instance-name my-instance
```

### List All Instances

```bash
aws lightsail get-instances \
  --query 'instances[*].{Name:name,State:state.name,IP:publicIpAddress}'
```

### Attach Static IP

```bash
aws lightsail attach-static-ip \
  --static-ip-name my-static-ip \
  --instance-name my-instance
```

### Update Firewall Rules

```bash
aws lightsail update-instance-firewall-rules \
  --instance-name my-instance \
  --port-info name=HTTP,protocol=TCP,fromPort=80,toPort=80
```

### Create Disk from Snapshot

```bash
aws lightsail create-disk-from-snapshot \
  --disk-name my-disk \
  --snapshot-name my-snapshot \
  --size-in-gb 100
```

## Examples

```bash
# Example 1: Plan limit exceeded
# InvalidInputException: Instance plan limit exceeded
# Fix: upgrade instance plan

# Example 2: Disk attach failed
# ResourceNotFoundException: Disk not found
# Fix: verify disk name and region
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS EBS Throttling]({{< relref "/cloud/aws/throttling" >}}) — EBS throttling errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
