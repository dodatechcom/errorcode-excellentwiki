---
title: "[Solution] Terraform Plan Changed Outside — Fix Drift"
description: "Fix Terraform plan changed outside errors. Resolve infrastructure drift, refresh state, and re-align configuration with actual resources."
---

## What This Error Means

The `Error: Plan changed outside of Terraform` message indicates that the real infrastructure state no longer matches what Terraform recorded in its state file. Terraform detects this mismatch during `apply` when the current resource attributes differ from what was shown in the last `plan`.

A typical output:

```
Error: Error: Plan has changed outside of Terraform

The current plan is no longer consistent with the state file. If you
recently modified resources outside of Terraform, run "terraform refresh"
and then try again.
```

Or:

```
Error: Resource terraform_plan.master has changed

  ~ resource "aws_instance" "web" {
        id                = "i-0abc123def456789"
      ~ instance_type     = "t3.micro" -> "t3.small"
```

## Why It Happens

Plan drift occurs when:

- **Manual changes via console or CLI**: Teammates or scripts modified resources outside Terraform.
- **Auto-scaling changes**: Cloud auto-scaling groups adjusted instance counts or types.
- **External automation**: Other tools (Ansible, CloudFormation, scripts) modified the same infrastructure.
- **State staleness**: Long time between `terraform plan` and `terraform apply`.
- **Provider-side changes**: Cloud providers auto-updating or rotating credentials attached to resources.

## How to Fix It

**Step 1: Refresh the state to detect current reality**

```bash
terraform refresh
```

Or combine refresh with your next plan:

```bash
terraform plan -refresh=true
```

**Step 2: Review the drift in the plan output**

Check which resources changed and why:

```bash
terraform plan -detailed-exitcode 2>&1 || true
```

**Step 3: Decide whether to adopt or revert the changes**

If the manual changes are correct, update your configuration to match:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.small"  # Updated to match actual state
}
```

If the changes should be reverted, apply Terraform to restore the desired state:

```bash
terraform apply
```

**Step 4: Prevent future drift**

Enable drift detection in your CI/CD pipeline:

```yaml
# GitHub Actions example
- name: Terraform Plan
  run: terraform plan -detailed-exitcode -lock=false
  continue-on-error: true
```

Use `prevent_destroy` lifecycle rules for critical resources:

```hcl
resource "aws_instance" "web" {
  lifecycle {
    prevent_destroy = true
  }
}
```

## Common Mistakes

- **Running apply without reviewing the refreshed plan**: Always check `terraform plan` output after `terraform refresh` before applying.
- **Ignoring drift in production**: Set up automated drift detection to catch unauthorized changes early.
- **Not using `-refresh-only` mode**: Use `terraform apply -refresh-only` to update state without making changes.
- **Multiple teams managing same resources**: Establish clear ownership using workspaces or separate state files.

## Related Pages

- [Terraform Resource Already Managed](/tools/terraform/terraform-resource-already-managed/) — Untracked resource conflicts
- [Terraform State Lock Error](/tools/terraform/terraform-state-locked/) — State lock acquisition failures
- [Ansible Task Failed](/tools/ansible/ansible-task-failed/) — Task execution errors
