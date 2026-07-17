---
title: "AWS InvalidInstanceID.NotFound"
description: "InvalidInstanceID.NotFound — Fix AWS EC2 instance not found errors."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The `InvalidInstanceID.NotFound` error occurs when an AWS API call references an EC2 instance ID that does not exist in the account or region. The instance may have been terminated, never created, or the wrong region is being queried.

## Common Causes

- The instance was terminated or does not exist
- The instance ID is from a different AWS account or region
- Typo in the instance ID (e.g., missing `i-` prefix)
- The instance was created in a different region and is being referenced without specifying the region

## How to Fix

Verify the instance exists in the current region:

```bash
aws ec2 describe-instances \
  --instance-ids i-0123456789abcdef0 \
  --region us-east-1
```

List all instances across all regions:

```bash
aws ec2 describe-instances \
  --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,Region:Placement.Region}' \
  --output table
```

Check the correct region:

```bash
# List all regions
aws ec2 describe-regions --query 'Regions[].RegionName' --output table

# Search in a specific region
aws ec2 describe-instances \
  --filters "Name=instance-id,Values=i-0123456789abcdef0" \
  --region eu-west-1
```

## Examples

- Running `aws ec2 stop-instances --instance-ids i-012345` in `us-east-1` when the instance is in `eu-west-1`
- Referencing an instance ID from an old Terraform state after the instance was replaced
- Using a hardcoded instance ID in a script after a redeployment created new instances

## Related Errors

- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC configuration issues.
- [AWS EC2 Quota Exceeded]({{< relref "/cloud/aws/ec2-quota" >}}) — instance limits reached.
- [Azure VM Not Found]({{< relref "/cloud/azure/vm-not-found" >}}) — Azure equivalent.
