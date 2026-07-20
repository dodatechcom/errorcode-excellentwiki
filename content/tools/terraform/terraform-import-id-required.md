---
title: "[Solution] Terraform Import Id Required"
description: "Fix Terraform import id required errors when the resource ID is not provided."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Import ID required errors occur when importing without specifying the ID:

```
Error: Required argument missing

To import a resource, you must provide the resource ID.
```

## Common Causes

- Forgot to specify resource ID in import command.
- Import syntax is wrong.

## How to Fix

**Provide the correct ID:**

```bash
terraform import aws_instance.web i-0123456789abcdef0
```

**Import with module path:**

```bash
terraform import module.vpc.aws_vpc.main vpc-abc123
```

**Check resource ID first:**

```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].{ID:InstanceId,Name:Tags[?Key==`Name`].Value|[0]}' --output table
```

## Examples

```bash
# Import EC2 instance
terraform import aws_instance.web i-0123456789abcdef0

# Import S3 bucket
terraform import aws_s3_bucket.main my-bucket-name

# Import with module
terraform import module.vpc.aws_vpc.main vpc-abc123
```
