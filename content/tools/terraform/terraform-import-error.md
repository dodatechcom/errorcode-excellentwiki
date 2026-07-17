---
title: "[Solution] Terraform Import Error — Fix Resource Import"
description: "Fix Terraform import failed errors. Resolve import configuration mismatches, ID formats, and state conflicts with step-by-step fixes."
---

## What This Error Means

The `terraform import` error occurs when Terraform cannot bring an existing cloud resource under management. This happens when the import ID is wrong, the resource does not exist, or the configuration does not match the actual resource.

A typical error:

```
Error: resource address "aws_instance.web" does not exist in the configuration

Before importing this resource, please add it to your Terraform configuration
using a "resource" block.
```

Or:

```
Error: import aws_instance.web (i-0abc123def456789): import returned unexpected
error: Cannot import non-existent remote object. While attempting to import an
existing object, a pre-existing resource was detected.
```

## Why It Happens

Import errors occur for several reasons:

- **Missing resource block**: The resource address must exist in your `.tf` files before importing.
- **Wrong import ID**: The resource ID format differs between cloud providers and Terraform expects specific formats.
- **Resource does not exist**: The specified resource ID is invalid or the resource was deleted.
- **State conflicts**: The resource is already tracked in the current state file.
- **Provider version mismatch**: Import behavior changes between provider versions.

## How to Fix It

**Step 1: Add the resource block to your configuration first**

The resource block must exist before running import:

```hcl
resource "aws_instance" "web" {
  # Terraform will fill this in after import
}
```

**Step 2: Use the correct import ID format**

Check provider documentation for the expected ID format:

```bash
# AWS EC2 instance
terraform import aws_instance.web i-0abc123def456789

# AWS S3 bucket
terraform import aws_s3_bucket.mybucket my-bucket-name

# Kubernetes namespace
terraform import kubernetes_namespace.prod prod-namespace
```

**Step 3: Generate import blocks with `moved` or `import` blocks (HCL 1.6+)**

Use the declarative import syntax:

```hcl
import {
  to = aws_instance.web
  id = "i-0abc123def456789"
}
```

Then run:

```bash
terraform plan -generate-config-out=imported.tf
```

**Step 4: Verify import with plan**

After import, check that Terraform sees no drift:

```bash
terraform plan
```

## Common Mistakes

- **Importing without adding the resource block first**: Always add the empty resource block to your `.tf` files before importing.
- **Guessing the resource ID**: Check provider documentation for exact ID formats.
- **Not running `terraform plan` after import**: Always verify the import result to catch drift immediately.
- **Importing to the wrong workspace**: Verify you are in the correct workspace before importing: `terraform workspace show`.

## Related Pages

- [Terraform Resource Already Managed](/tools/terraform/terraform-resource-already-managed/) — Resource tracking conflicts
- [Terraform State Lock Error](/tools/terraform/terraform-state-locked/) — State lock issues
- [Kubectl Resource Not Found](/tools/kubectl/kubectl-resource-not-found/) — Resource lookup failures
