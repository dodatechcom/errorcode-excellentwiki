---
title: "[Solution] Terraform Unknown Value Error - Fix Value for Unknown Cannot Be Computed"
description: "Fix Terraform 'value for unknown cannot be computed' error. Resolve unknown values in plans, apply, and resource references."
tools: ["terraform"]
error-types: ["unknown-value"]
severities: ["error"]
weight: 5
---

This error means Terraform encountered a value that it cannot determine during planning or apply. The value depends on something that has not yet been computed, making the plan incomplete.

## What This Error Means

When Terraform tries to evaluate an expression and the value is not yet known, you see:

```
Error: Error in function call: value for unknown cannot be computed
# or
Error: Invalid for_each argument: value depends on resource attributes
```

This typically happens when you reference an attribute of a resource that has not been created yet, or when a variable value depends on a resource output that is not yet available.

## Why It Happens

- You are using `for_each` or `count` with a value that depends on a resource not yet created
- An output from one resource is referenced as an input to another without proper `depends_on`
- A variable default uses `null` and the code does not handle the null case
- You are referencing `data` source attributes that require the resource to exist first
- A conditional expression references attributes that are unknown during plan
- The resource uses `create_before_destroy` and the new resource's attributes are not yet known

## How to Fix It

### Add explicit depends_on

```hcl
resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_instance" "web" {
  subnet_id = aws_subnet.main.id
  depends_on = [aws_subnet.main]
}
```

### Use try() or can() for unknown values

```hcl
instance_type = try(aws_instance.web[0].instance_type, "t3.micro")
```

The `try()` function returns a fallback when the value is unknown.

### Avoid referencing yet-to-be-created resources in for_each

```hcl
# Instead of referencing an unknown list
for_each = aws_subnet.main[*].id

# Use a known value
for_each = toset(["subnet-a", "subnet-b", "subnet-c"])
```

### Use locals to defer evaluation

```hcl
locals {
  subnet_ids = aws_subnet.main[*].id
}

resource "aws_instance" "web" {
  count      = length(local.subnet_ids)
  subnet_id  = local.subnet_ids[count.index]
}
```

### Handle null variables

```hcl
variable "config" {
  default = null
}

resource "aws_instance" "web" {
  instance_type = var.config != null ? var.config.type : "t3.micro"
}
```

### Use lifecycle ignore_changes for drift

```hcl
lifecycle {
  ignore_changes = [tags]
}
```

This prevents plan from failing on unknown attribute changes.

## Common Mistakes

- Referencing resource attributes in `for_each` that are not yet known at plan time
- Not using `try()` to handle attributes that may be unavailable
- Creating circular dependencies between resources and data sources
- Assuming Terraform can predict values that only exist after apply
- Forgetting that `output` values from child modules may be unknown during plan

## Related Pages

- [Terraform Plan Changed]({{< relref "/tools/terraform/terraform-plan-changed" >}}) -- unexpected plan changes
- [Terraform Cycle Error]({{< relref "/tools/terraform/terraform-cycle-error" >}}) -- dependency cycles
- [Terraform Apply Error]({{< relref "/tools/terraform/terraform-apply-error" >}}) -- apply failures
