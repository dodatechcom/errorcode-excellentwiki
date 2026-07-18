---
title: "[Solution] Terraform Import ID Error - Fix Import ID Format Invalid"
description: "Fix Terraform import ID format errors when importing existing resources. Use correct ID formats and import commands for each resource type."
tools: ["terraform"]
error-types: ["import-id-error"]
severities: ["error"]
weight: 5
---

This error means the resource ID you provided to `terraform import` does not match the format expected for that resource type. Each resource type requires a specific ID structure.

## What This Error Means

When you run `terraform import` with an incorrectly formatted ID, you see:

```
Error: unexpected format of ID (<id>), expected <expected-format>
# or
Error: resource type <type> does not accept ID <id>
# or
Error: Error: Cannot import non-existent remote resource
```

Terraform parses the import ID to locate the resource in the cloud provider. If the format is wrong, it cannot find or identify the resource.

## Why It Happens

- The import ID format is different from what Terraform expects
- You are using the wrong resource type name
- The resource does not exist in the cloud provider
- You are importing into a different region or account than the resource is in
- The import ID includes extra characters like URL prefixes
- AWS account ID or region is missing from the ID

## How to Fix It

### Check the resource import documentation

```bash
terraform import --help
```

The help output shows the expected ID format for each resource type.

### Use the correct ID format for AWS

```bash
# EC2 instance
terraform import aws_instance.web i-1234567890abcdef0

# S3 bucket
terraform import aws_s3_bucket.data my-bucket-name

# Security group
terraform import aws_security_group.web sg-12345678
```

### Use the correct ID format for GCP

```bash
# Compute instance
terraform import google_compute_instance.web projects/my-project/zones/us-central1-a/instances/my-instance

# GCS bucket
terraform import google_storage_bucket.data my-bucket
```

### Use the correct ID format for Azure

```bash
# Resource group
terraform import azurerm_resource_group.main /subscriptions/{sub-id}/resourceGroups/{rg-name}
```

### Verify the resource exists first

```bash
aws ec2 describe-instances --instance-ids i-1234567890abcdef0
```

Confirm the resource actually exists before attempting import.

### Check region and account

```bash
export AWS_DEFAULT_REGION=us-east-1
terraform import aws_instance.web i-1234567890abcdef0
```

Ensure you are targeting the correct region.

### Use generate-config flag for complex imports

```bash
terraform import -generate-config-out=imported.tf aws_instance.web i-1234567890abcdef0
```

This generates the HCL configuration for the imported resource.

## Common Mistakes

- Using the resource name instead of the cloud provider resource ID
- Including AWS account ID or region in the ID when Terraform does not require it
- Forgetting that different resource types have completely different ID formats
- Importing into the wrong region where the resource does not exist
- Not writing the matching HCL configuration before or after import

## Related Pages

- [Terraform Import Error]({{< relref "/tools/terraform/terraform-import-error" >}}) -- general import issues
- [Terraform Apply Error]({{< relref "/tools/terraform/terraform-apply-error" >}}) -- apply failures
- [Terraform State Mv]({{< relref "/tools/terraform/terraform-state-mv" >}}) -- state migration
