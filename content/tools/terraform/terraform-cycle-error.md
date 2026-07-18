---
title: "[Solution] Terraform Cycle Error - Fix Cycle in Module Dependencies"
description: "Fix Terraform cycle error when resources or modules have circular dependencies. Restructure dependencies to break cycles and enable proper ordering."
tools: ["terraform"]
error-types: ["cycle-error"]
severities: ["error"]
weight: 5
---

This error means Terraform detected a circular dependency between resources, modules, or variables. No valid ordering exists because two or more resources depend on each other.

## What This Error Means

When Terraform analyzes your dependency graph and finds a cycle, it reports:

```
Error: Cycle: aws_instance.web, aws_security_group.sg
# or
Error: Cycle: module.vpc, module.compute (module dependency)
```

Terraform cannot determine which resource to create first because each one needs the other to exist. This is a hard error that blocks all operations.

## Why It Happens

- Resource A references resource B and resource B references resource A
- A module outputs a value used by its parent while the parent provides a value the module needs
- A `data` source references a resource that depends on the data source
- Tags or other metadata reference each other across resources
- Security group rules reference each other for ingress and egress
- An `output` in a module references a resource that uses the module's `variable`

## How to Fix It

### Identify the cycle

```bash
terraform graph | dot -Tpng > graph.png
```

Open the generated graph image to visually identify the circular reference.

### Break the cycle with separate resources

```hcl
# Instead of circular security group rules
resource "aws_security_group" "web" {
  name = "web"
}

resource "aws_security_group_rule" "web_ingress" {
  type        = "ingress"
  from_port   = 80
  to_port     = 80
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = aws_security_group.web.id
}

resource "aws_security_group_rule" "db_ingress" {
  type        = "ingress"
  from_port   = 5432
  to_port     = 5432
  protocol    = "tcp"
  source_security_group_id = aws_security_group.web.id
  security_group_id = aws_security_group.db.id
}
```

### Use depends_on to clarify ordering

```hcl
resource "aws_instance" "web" {
  ami = "ami-12345"
  depends_on = [aws_security_group.web]
}
```

### Extract shared values into locals

```hcl
locals {
  vpc_id = aws_vpc.main.id
}

resource "aws_security_group" "web" {
  vpc_id = local.vpc_id
}
```

### Use data sources instead of direct references

```hcl
data "aws_vpc" "main" {
  id = var.vpc_id
}
```

A data source reads an existing resource without creating a dependency.

### Split modules to break circular references

Move the shared resource into its own module and reference it by ID rather than through outputs.

## Common Mistakes

- Not realizing that `depends_on` can create cycles even when it seems harmless
- Referencing module outputs that create circular module dependencies
- Creating inline security group rules instead of separate rule resources
- Not running `terraform graph` to visualize dependencies before they become complex
- Assuming Terraform will auto-detect and break cycles

## Related Pages

- [Terraform Unknown Value]({{< relref "/tools/terraform/terraform-unknown-value" >}}) -- unknown value errors
- [Terraform Module Not Found]({{< relref "/tools/terraform/terraform-module-not-found" >}}) -- module resolution
- [Terraform Apply Error]({{< relref "/tools/terraform/terraform-apply-error" >}}) -- apply failures
