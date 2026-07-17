---
title: "AWS VPCIdNotSupported / InvalidVPCID"
description: "VPCIdNotSupported / InvalidVPCID — Fix AWS VPC configuration errors."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The `VPCIdNotSupported` or `InvalidVPCID` error occurs when an AWS API call references a VPC ID that does not exist, is in a different account, or is in a different region. This often happens when resources are provisioned with hardcoded VPC IDs.

## Common Causes

- The VPC ID is from a different AWS account or region
- The VPC was deleted and the ID is still referenced in configuration
- Typo in the VPC ID format (must be `vpc-` followed by hex characters)
- Cross-account resource sharing is not configured

## How to Fix

Verify the VPC exists and note its ID:

```bash
aws ec2 describe-vpcs \
  --query 'Vpcs[].{VpcId:VpcId,CidrBlock:CidrBlock,State:State}' \
  --output table
```

Check the VPC in a specific region:

```bash
aws ec2 describe-vpcs \
  --region eu-west-1 \
  --query 'Vpcs[].{VpcId:VpcId,Name:Tags[?Key==`Name`].Value|[0]}'
```

If using Terraform, reference by data source instead of hardcoded ID:

```hcl
data "aws_vpc" "selected" {
  tags = {
    Name = "my-vpc"
  }
}

resource "aws_instance" "app" {
  vpc_security_group_ids = [aws_security_group.app.id]
  subnet_id              = data.aws_subnets.selected.ids[0]
}
```

## Examples

- Terraform apply fails with `InvalidVPCID` after VPC was destroyed and recreated
- Hardcoded VPC ID in a CloudFormation template used across multiple accounts
- Cross-account peering request references a VPC that does not exist in the target account

## Related Errors

- [AWS EC2 Quota Exceeded]({{< relref "/cloud/aws/ec2-quota" >}}) — VPC limits reached.
- [AWS Instance Not Found]({{< relref "/cloud/aws/instance-not-found" >}}) — EC2 instance missing.
- [Azure NSG Error]({{< relref "/cloud/azure/nsg-error" >}}) — network security group issues.
