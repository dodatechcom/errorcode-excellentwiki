---
title: "[Solution] AWS EMR Error — cluster/step/notebook failures"
description: "Fix AWS EMR errors. Resolve EMR cluster, step execution, and notebook issues."
error-types: ["api-error"]
severities: ["error"]
weight: 139
---

An AWS EMR error occurs when clusters fail to provision, steps abort, or notebook notebooks encounter permission issues. EMR provides managed Hadoop/Spark but requires careful cluster and step configuration.

## Common Causes

- EC2 instance limits insufficient for cluster size
- Step failures due to incorrect S3 paths
- Bootstrap action script errors
- IAM role lacks EMR or S3 permissions
- Notebook instance not in same VPC as cluster

## How to Fix

### Check Cluster Status

```bash
aws emr list-clusters \
  --query 'Clusters[*].{ID:Id,Name:Name,Status:Status.State}'
```

### Describe Cluster

```bash
aws emr describe-cluster \
  --cluster-id j-xxx
```

### List Steps

```bash
aws emr list-steps \
  --cluster-id j-xxx \
  --query 'Steps[*].{ID:Id,Name:Name,Status:Status.State}'
```

### Terminate Cluster

```bash
aws emr terminate-clusters --cluster-ids j-xxx
```

### Create Cluster

```bash
aws emr create-cluster \
  --name my-cluster \
  --release-label emr-6.15.0 \
  --applications Name=Spark \
  --instance-groups InstanceGroupType=MASTER,InstanceType=m5.xlarge,InstanceCount=1 InstanceGroupType=CORE,InstanceType=m5.xlarge,InstanceCount=3 \
  --service-role EMR_DefaultRole
```

## Examples

```bash
# Example 1: Instance limit exceeded
# ValidationException: EC2 instance limit exceeded
# Fix: request limit increase or use smaller instance type

# Example 2: Step failed
# Step failed with exit code 1
# Fix: check step logs in S3 or CloudWatch
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS S3 Error]({{< relref "/cloud/aws/aws-s3-error" >}}) — S3 data errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
