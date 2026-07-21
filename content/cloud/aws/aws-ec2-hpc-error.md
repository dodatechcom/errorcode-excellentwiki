---
title: "[Solution] AWS EC2 HPC Error"
description: "ClusterNotFound or InsufficientCapacity for HPC operations."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 HPC Error` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- HPC instance limits insufficient
- EFA configuration issue
- Placement group not configured for HPC
- Scratch storage bottleneck

## How to Fix

### Check HPC limits

```bash
aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --region us-east-1
```
### Describe EFA

```bash
aws ec2 describe-elastic-fabric-adapters --query 'ElasticFabricAdapters[*].[AdapterName,State]' --output table
```
### Launch with placement group

```bash
aws ec2 run-instances --instance-type hpc6id.4xlarge --placement GroupName=my-cluster --image-id ami-0abcdef
```

## Examples

- hpc6id.4xlarge fails due to insufficient vCPU quota
- EFA not attached to cluster instance

## Related Errors

- [EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [Insufficient Capacity]({{< relref "/cloud/aws/aws-ec2-insufficient-capacity" >}}) -- Capacity issues
