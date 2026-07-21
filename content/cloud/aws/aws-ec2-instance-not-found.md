---
title: "[Solution] AWS EC2 Instance Not Found"
description: "InstanceNotFound error when the specified EC2 instance cannot be located."
cloud: ["aws"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

The `EC2 Instance Not Found` error occurs when an AWS service cannot complete the requested operation.

## Common Causes

- The instance was terminated or stopped and deregistered
- Incorrect instance ID in the API call
- The instance belongs to a different AWS account or region
- IAM permissions do not allow DescribeInstances for the instance

## How to Fix

### Check instance status

```bash
aws ec2 describe-instance-status --instance-ids i-0abc123
```
### List all instances

```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name]' --output table
```
### Verify region

```bash
aws ec2 describe-instances --region us-east-1 --instance-ids i-0abc123
```

## Examples

- Calling describe_instances with a terminated instance ID returns NotFound
- Using an instance ID from a different region returns InvalidInstanceIDNotFound

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) -- General EC2 errors
- [Instance Limit]({{< relref "/cloud/aws/ec2-instance-limit" >}}) -- Instance limit errors
