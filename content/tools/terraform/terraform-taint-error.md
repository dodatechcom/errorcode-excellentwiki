---
title: "[Solution] Terraform Taint Deprecated Error - Fix taint is Deprecated Use Replace"
description: "Fix Terraform taint deprecation warning. Migrate from terraform taint to terraform apply -replace or lifecycle replace_triggered_by."
tools: ["terraform"]
error-types: ["taint-error"]
severities: ["warning"]
weight: 5
---

This error or warning means you are using `terraform taint`, which is deprecated since Terraform 0.15.1. Terraform recommends using `terraform apply -replace` or the `lifecycle` block instead.

## What This Error Means

When you run `terraform taint`, Terraform displays:

```
Warning: terraform taint is deprecated
The "terraform taint" command is deprecated. Use "terraform apply -replace"
instead to mark a resource for replacement.
```

Taint modifies state directly and bypasses Terraform's normal plan-apply workflow. This can lead to state inconsistencies, especially in collaborative environments with remote state.

## Why It Happens

- Your team's scripts still use `terraform taint` from older Terraform versions
- Documentation or blog posts reference the deprecated command
- CI/CD pipelines were set up before the deprecation
- You want to force recreation of a resource and taint was the only method you knew
- Legacy Terraform code has not been updated to modern practices

## How to Fix It

### Use -replace flag on apply

```bash
terraform apply -replace=aws_instance.web
```

This marks the resource for replacement during the next plan and apply cycle.

### Use -replace in the plan phase

```bash
terraform plan -replace=aws_instance.web
```

This shows what will change before you commit to the apply.

### Use lifecycle replace_triggered_by

```hcl
resource "aws_instance" "web" {
  ami           = "ami-new"
  instance_type = "t3.micro"

  lifecycle {
    replace_triggered_by = [aws_launch_template.new.id]
  }
}
```

This automatically replaces the resource when the referenced resource changes.

### Force recreation through attribute changes

```hcl
resource "aws_instance" "web" {
  ami = var.new_ami_id
  tags = {
    ForceReplace = timestamp()
  }
}
```

Adding `timestamp()` forces a change on every plan, but use sparingly.

### Update CI/CD scripts

```yaml
# Old
- run: terraform taint aws_instance.web

# New
- run: terraform apply -replace=aws_instance.web -auto-approve
```

### Use replace_triggered_by for infrastructure updates

```hcl
resource "aws_instance" "web" {
  launch_template {
    id = aws_launch_template.new.id
  }

  lifecycle {
    replace_triggered_by = [aws_launch_template.new]
  }
}
```

This is the Terraform-native way to trigger replacements.

## Common Mistakes

- Continuing to use `terraform taint` because it still works despite the deprecation
- Not understanding that taint modifies state directly, which can cause drift
- Forgetting that tainted resources show as "tainted" in state, which teammates can see
- Using `terraform taint` in automation instead of the `-replace` flag
- Not testing replacement behavior before production changes

## Related Pages

- [Terraform State Locked]({{< relref "/tools/terraform/terraform-state-locked" >}}) -- state locking
- [Terraform Apply Error]({{< relref "/tools/terraform/terraform-apply-error" >}}) -- apply failures
- [Terraform Plan Changed]({{< relref "/tools/terraform/terraform-plan-changed" >}}) -- unexpected plan changes
