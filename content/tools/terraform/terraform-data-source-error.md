---
title: "[Solution] Terraform Data Source Lookup Failed Error — How to Fix"
description: "Fix Terraform data source lookup failures including missing resources, filter mismatches, and provider authentication issues quickly."
comments: true
---

A Terraform data source lookup failed error occurs when Terraform cannot find or read the external resource referenced by a `data` block. This prevents Terraform from computing values that depend on the data source and blocks subsequent resource creation.

## Why It Happens

Data sources query external infrastructure to fetch information Terraform does not manage directly. Lookup failures stem from:

- **Resource does not exist**: The data source queries for a resource that has not been created yet, has been deleted, or exists in a different region/account.
- **Filter returns no results**: Tags, IDs, or filter expressions do not match any existing resources, causing the data source to find zero matches.
- **Permission denied**: The IAM role or user running Terraform lacks read permissions for the queried resource type.
- **Provider version mismatch**: The provider version does not support the filter attributes or data source type being used.
- **Timing issues**: The data source queries a resource that is still being created by another process or Terraform run.
- **Incorrect attribute references**: The data source schema has changed, and the attribute name used in the configuration no longer exists.

## Common Error Messages

**Error: No matching resource found**

```
Error: No matching AMI found

You can use more specific Terraform provider arguments to narrow
down the results, or use a different data source. If the AMI is
owned by another account, make sure the owner is specified.

  data.aws_ami.ubuntu:

  owners     = ["099720109477"]
  most_recent = true
```

**Error: Multiple results found**

```
Error: Multiple data sources found

The data source "aws_iam_role" "app" returned multiple results.
Use a more specific filter or set expect_single_result = true.

Filter criteria matched 3 results:
  - app-role-prod
  - app-role-staging
  - app-role-dev
```

**Error: Data source attribute not found**

```
Error: Invalid attribute reference

data.aws_eks_cluster.cluster does not have attribute
"certificate_authority.0.data". Available attributes are:
  - arn
  - name
  - endpoint
  - version
  - certificate_authority (nested block)
```

**Error: Access denied for data source**

```
Error: Reading ELBv2 Load Balancers failed

AuthorizationError: User: arn:aws:iam::123456789012:user/tf
is not authorized to perform: elasticloadbalancing:DescribeLoadBalancers
on resource: *
```

## How to Fix It

### Solution 1: Verify the data source resource exists

Ensure the resource you are querying actually exists in the target region and account:

```bash
# Check if the AMI exists
aws ec2 describe-images \
  --owners 099720109477 \
  --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-*" \
  --region us-east-1

# Check if the VPC exists
aws ec2 describe-vpcs \
  --filters "Name=tag:Name,Values=production-vpc" \
  --region us-east-1
```

If the resource must exist first, add `depends_on`:

```hcl
resource "aws_iam_role" "app" {
  name = "app-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

data "aws_iam_role" "app" {
  name = "app-role"
  depends_on = [aws_iam_role.app]
}
```

### Solution 2: Broaden or narrow data source filters

Adjust filter criteria to match exactly one or more expected results:

```hcl
# Too broad — might match multiple AMIs
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu-*"]
  }
}

# More specific — matches exactly one
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}
```

For multiple results, use `data` with `for_each`:

```hcl
data "aws_subnets" "private" {
  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }

  tags = {
    Tier = "private"
  }
}

resource "aws_db_subnet_group" "main" {
  name       = "main-db-subnet-group"
  subnet_ids = data.aws_subnets.private.ids
}
```

### Solution 3: Ensure proper IAM permissions

Data sources require read permissions for the queried API. Add the necessary IAM policies:

```hcl
# Policy for reading AMIs
data "aws_iam_policy_document" "terraform_data_read" {
  statement {
    sid    = "AllowDescribeImages"
    effect = "Allow"
    actions = [
      "ec2:DescribeImages",
      "ec2:DescribeInstances",
      "ec2:DescribeVpcs",
      "ec2:DescribeSubnets",
      "ec2:DescribeSecurityGroups"
    ]
    resources = ["*"]
  }
}
```

Verify with the AWS CLI:

```bash
# Test the exact API call Terraform makes
aws ec2 describe-images \
  --owners 099720109477 \
  --filters "Name=name,Values=ubuntu-*" \
  --region us-east-1 \
  --query 'Images[*].{ID:ImageId,Name:Name}'
```

### Solution 4: Handle attribute access safely

Use `try()` or check available attributes when data source schemas differ across provider versions:

```hcl
data "aws_eks_cluster" "cluster" {
  name = var.cluster_name
}

# Safe attribute access with try()
locals {
  cluster_ca = try(data.aws_eks_cluster.cluster.certificate_authority[0].data, "")
  cluster_endpoint = try(data.aws_eks_cluster.cluster.endpoint, "unknown")
}

output "cluster_ca" {
  value     = local.cluster_ca
  sensitive = true
}
```

Check the provider documentation for the exact attribute schema of your version.

## Common Scenarios

**Scenario 1: AMI data source returns no results after account change**

After an AWS account migration or organizational change, the AMI owner ID changes. The data source filter with the old owner ID returns empty. Update the `owners` field to match the new account.

**Scenario 2: Security group data source queries wrong VPC**

When deploying to multiple VPCs, a data source for security groups without a VPC filter may return results from the wrong VPC. Always include a `vpc-id` filter to scope the query.

**Scenario 3: Data source depends on resource in another module**

A data source in `module.b` queries a resource created in `module.a`. Without explicit `depends_on` or output references, Terraform cannot determine the ordering. Add the dependency explicitly or pass the resource as a module variable.

## Prevent It

- **Always include specific filters**: Never rely on unfiltered data source queries. Use tags, names, or IDs to narrow results.
- **Validate data source results in plan**: Review `terraform plan` output carefully to ensure data sources resolved correctly before applying.
- **Test data source permissions separately**: Run the equivalent AWS CLI or API calls manually to verify permissions before adding the data source to Terraform.

## Related Pages

- [Terraform Provider Error](/tools/terraform/terraform-provider-error/) — Provider authentication issues
- [Terraform Unknown Value Error](/tools/terraform/terraform-unknown-value/) — Known after apply warnings
- [Terraform Import Error](/tools/terraform/terraform-import-error/) — Importing existing resources
