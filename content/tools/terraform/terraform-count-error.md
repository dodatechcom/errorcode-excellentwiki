---
title: "[Solution] Terraform Count Error - Fix count and for_each Cannot Be Used Together"
description: "Fix Terraform error when count and for_each are used on the same resource. Refactor to use one iteration method and avoid meta-argument conflicts."
tools: ["terraform"]
error-types: ["count-error"]
severities: ["error"]
weight: 5
---

This error means you are using both `count` and `for_each` on the same resource or module. Terraform only allows one iteration meta-argument per resource because they serve overlapping purposes.

## What This Error Means

When you apply or plan a configuration that uses both `count` and `for_each` on the same block, Terraform reports:

```
Error: Invalid combination of arguments

  on main.tf line 15, in resource "aws_instance" "web":
  count = var.instance_count
  for_each = var.instance_map

Only one of "count" and "for_each" can be specified.
```

`count` creates N identical resources controlled by a number. `for_each` creates resources from a map or set. Using both creates ambiguity about which drives resource identity.

## Why It Happens

- You are refactoring from `count` to `for_each` and left both in temporarily
- A module was copied and modified without removing the original iteration
- A resource block inherited both arguments from a template or code generator
- You are trying to combine a numeric count with per-instance configuration
- A conditional expression uses `count` while the same resource has `for_each` from a parent module

## How to Fix It

### Choose one method and remove the other

If you need indexed resources:

```hcl
resource "aws_instance" "web" {
  count = var.instance_count
  ami           = "ami-12345"
  instance_type = "t3.micro"
  tags = { Name = "web-${count.index}" }
}
```

If you need unique configurations per instance:

```hcl
resource "aws_instance" "web" {
  for_each = var.instances
  ami           = each.value.ami
  instance_type = each.value.type
  tags = { Name = each.key }
}
```

### Migrate from count to for_each

```hcl
# Before
count = length(var.subnet_ids)

# After
for_each = toset(var.subnet_ids)
```

Use `toset()` to convert a list to a set for `for_each`.

### Use locals to combine both patterns

```hcl
locals {
  instances = {
    for i in range(var.count) : "instance-${i}" => {
      type = var.instance_types[i]
    }
  }
}

resource "aws_instance" "web" {
  for_each      = locals.instances
  instance_type = each.value.type
}
```

### Handle conditional creation with for_each

```hcl
for_each = var.create_resource ? toset(["enabled"]) : toset([])
```

This replaces the `count = var.create_resource ? 1 : 0` pattern.

## Common Mistakes

- Starting a migration from `count` to `for_each` but not finishing it
- Using `count` for conditional logic when `for_each` with an empty set is cleaner
- Not understanding that `count` and `for_each` produce different resource addresses
- Assuming you can combine both for extra flexibility
- Forgetting that `count.index` and `each.key` have different semantics

## Related Pages

- [Terraform Validation Error]({{< relref "/tools/terraform/terraform-validation-error" >}}) -- configuration validation
- [Terraform Apply Error]({{< relref "/tools/terraform/terraform-apply-error" >}}) -- resource creation failures
- [Terraform Plan Changed]({{< relref "/tools/terraform/terraform-plan-changed" >}}) -- unexpected plan changes
