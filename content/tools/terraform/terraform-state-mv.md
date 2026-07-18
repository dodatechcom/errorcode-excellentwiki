---
title: "[Solution] Terraform State Mv Error - Fix state mv Failed Resource Not Found"
description: "Fix terraform state mv failures when moving resources in state. Resolve resource not found errors and state migration issues."
tools: ["terraform"]
error-types: ["state-mv"]
severities: ["error"]
weight: 5
---

This error means `terraform state mv` cannot find the source resource in the state file or the destination already exists. State migration requires precise source and destination addresses.

## What This Error Means

When you run `terraform state mv` and it fails, you see:

```
Error: Resource not found in state
# or
Error: Destination already exists in state
# or
Error: No such resource instance in state
```

State mv moves resource tracking from one address to another without destroying or creating infrastructure. Failures indicate the state file does not contain what you expect.

## Why It Happens

- The source resource address is misspelled or uses the wrong format
- The resource is in a different workspace or state file
- The resource was already moved and no longer exists at the source address
- The destination address already has a resource tracked
- The resource is in a module and the module path is wrong
- You are using an index that does not exist

## How to Fix It

### Verify the source resource exists

```bash
terraform state list | grep <resource-name>
```

Check the exact address of the resource you want to move.

### Move resources between addresses

```bash
terraform state mv aws_instance.old_name aws_instance.new_name
```

### Move resources into or out of modules

```bash
terraform state mv aws_instance.web module.compute.aws_instance.web
terraform state mv module.old_module.aws_instance.web aws_instance.web
```

### Move resources in for_each or count

```bash
terraform state mv 'aws_instance.web[0]' 'aws_instance.web["primary"]'
```

Use quotes and brackets to specify indexed resources.

### Check the correct workspace

```bash
terraform workspace list
terraform workspace select correct-workspace
terraform state list
```

### Move between state files using state pull and push

```bash
terraform state pull > state.json
# Edit state.json
terraform state push state.json
```

For complex moves, editing the state file directly can be safer.

### Use moved blocks for permanent renames

```hcl
moved {
  from = aws_instance.web
  to   = aws_instance.application
}
```

This is tracked in configuration and applied automatically.

## Common Mistakes

- Not backing up state before running `state mv`
- Using wrong resource addresses without checking `terraform state list` first
- Forgetting that `state mv` does not rename the actual cloud resource
- Running state mv across different workspaces accidentally
- Not removing the old resource block from configuration after moving in state

## Related Pages

- [Terraform State Locked]({{< relref "/tools/terraform/terraform-state-locked" >}}) -- state locking
- [Terraform Import Error]({{< relref "/tools/terraform/terraform-import-error" >}}) -- resource import
- [Terraform Removal Error]({{< relref "/tools/terraform/terraform-removal-error" >}}) -- resource removal
