---
title: "[Solution] Terraform Resource Already Managed — Fix State"
description: "Fix Terraform resource already managed errors. Import existing resources or remove state conflicts to resume normal operations."
---

## What This Error Means

The `resource already managed` error occurs when Terraform finds an infrastructure resource that already exists in the cloud provider but is not tracked in the current Terraform state. Terraform refuses to create a duplicate, and it cannot manage a resource it did not create.

A typical error looks like:

```
Error: Resource already managed by Terraform

Resource aws_instance.web already has a Terraform resource address
"aws_instance.web" in state. Please remove this resource from the state
first, or import it.
```

Or:

```
Error: Error creating instance: InvalidInstanceID.NotFound

The instance ID "i-0abc123def456789" does not exist, but the resource
already exists in Terraform state.
```

## Why It Happens

This error appears in several situations:

- **Manual resource creation**: Someone created the resource via console or CLI without updating Terraform state.
- **State file divergence**: The state file was modified or lost, leaving resources untracked.
- **Import conflicts**: Attempting to import a resource that is partially tracked.
- **Module or workspace issues**: Resources exist in a different workspace or module than expected.
- **Destroyed state but resource remains**: `terraform destroy` failed partway, leaving orphaned resources.

## How to Fix It

**Step 1: Import the existing resource**

Import the resource into your Terraform state:

```bash
terraform import aws_instance.web i-0abc123def456789
```

Or for module resources:

```bash
terraform import module.web.aws_instance.web i-0abc123def456789
```

**Step 2: Remove from state if the resource should be recreated**

If the resource should not exist, remove it from state and let Terraform recreate it:

```bash
terraform state rm aws_instance.web
terraform plan
```

**Step 3: Update configuration to match existing resource**

If the resource was created manually, update your `.tf` file to match its current configuration, then import:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  # Match all existing attributes
}
```

**Step 4: Use `moved` blocks for renames**

If the resource was renamed, use the `moved` block to preserve state:

```hcl
moved {
  from = aws_instance.web
  to   = aws_instance.web_server
}
```

## Common Mistakes

- **Forgetting to import before planning**: Always run `terraform import` before `terraform plan` for existing resources.
- **Not updating config to match reality**: After importing, the `.tf` file must reflect the actual resource attributes or Terraform will show drift.
- **Removing from state without deleting the resource**: `terraform state rm` does not delete the resource. It only removes the tracking.
- **Ignoring drift in collaborative environments**: Use remote state and state locking to prevent state divergence across team members.

## Related Pages

- [Terraform Plan Changed](/tools/terraform/terraform-plan-changed/) — Plan drift detection
- [Terraform Import Error](/tools/terraform/terraform-import-error/) — Import failures
- [Kubectl Resource Not Found](/tools/kubectl/kubectl-resource-not-found/) — Kubernetes resource lookup issues
