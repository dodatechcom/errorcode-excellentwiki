---
title: "[Solution] Terraform Plan Invalid or Unknown Values Error — How to Fix"
description: "Fix Terraform plan errors including invalid values, unknown references, and plan conflicts with actionable step-by-step solutions."
comments: true
---

A Terraform plan error occurs when Terraform cannot generate a valid execution plan due to invalid configuration values, unknown references, or conflicts between the current state and the desired configuration. This prevents `apply` from proceeding with any changes.

## Why It Happens

The plan phase validates the entire configuration and computes the diff between current state and desired state. Errors arise from:

- **Invalid resource arguments**: A resource block contains arguments that are not valid for the resource type, contain typos, or use incorrect syntax.
- **Unknown computed values**: The plan references a value that is only known after apply, such as a dynamic ID or IP address from a resource not yet created.
- **Type conversion errors**: Values are passed between resources in incompatible types, such as a list where a string is expected.
- **Cycle detection**: Resources reference each other in a circular dependency, preventing Terraform from determining an execution order.
- **Provider schema changes**: After a provider upgrade, certain arguments were removed or renamed, making the existing configuration invalid.
- **Computed attribute references**: An output or resource references an attribute that is marked as computed (known only after apply).

## Common Error Messages

**Error: Invalid block definition**

```
Error: Invalid block type

Blocks of type "ingres" are not expected here. Did you mean
"ingress"?

  on main.tf line 45, in resource "aws_security_group" "web":
  45:   ingres {
  46:     from_port = 80
  47:     to_port   = 80
  48:     protocol  = "tcp"
  49:     cidr_blocks = ["0.0.0.0/0"]
  50:   }
```

**Error: Unknown value during plan**

```
Error: Provider produced inconsistent plan

When expanding the plan for aws_lambda_function.handler to
include new values learned so far during apply, provider
produced an unexpected new value.

Root resource was present, but now absent. This is a bug in the
provider, which should be reported as a provider issue.
```

**Error: Plan contains unknown value**

```
Error: Cycle detected in resource dependencies

  aws_subnet.private depends on aws_vpc.main
  aws_route_table.private depends on aws_subnet.private
  aws_route_table_association.private depends on aws_route_table.private
  aws_vpc.main depends on aws_route_table_association.private
```

**Error: Plan resource replacement conflict**

```
Error: Plan requires replacement

Resource aws_instance.web has been marked as tainted and will
be recreated, but the plan also includes changes that cannot be
applied to the replacement instance. Consider using -replace
flag explicitly or review the tainted resource state.
```

## How to Fix It

### Solution 1: Fix invalid block and argument names

Review the error message for the exact line and correct the typo or invalid argument:

```hcl
# Wrong — typo in "ingress"
resource "aws_security_group" "web" {
  name   = "web-sg"
  vpc_id = aws_vpc.main.id

  ingres {           # ERROR: "ingres" is not valid
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Correct
resource "aws_security_group" "web" {
  name   = "web-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

Run `terraform validate` to catch these before planning:

```bash
terraform validate
```

### Solution 2: Handle unknown values with lifecycle ignore or targets

When a value is only known after apply, use `ignore_changes` or `-target` to work around it:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  lifecycle {
    ignore_changes = [
      ami,
      tags["UpdatedAt"],
    ]
  }
}
```

For providers with known issues, use targeted applies:

```bash
# Plan and apply only the problematic resource first
terraform plan -target=aws_lambda_function.handler -out=tfplan
terraform apply tfplan

# Then plan the rest normally
terraform plan -out=tfplan
terraform apply tfplan
```

### Solution 3: Break circular dependencies

Identify and resolve dependency cycles:

```hcl
# Wrong — circular dependency
resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id    # depends on route table
  route_table_id = aws_route_table.private.id
}

# Fix — restructure dependencies
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}
```

Use `terraform graph | dot -Tpng > graph.png` to visualize dependencies:

```bash
# Generate dependency graph
terraform graph > graph.dot

# If graphviz is installed
terraform graph | dot -Tpng > dependency-graph.png
```

### Solution 4: Fix type mismatches between resources

Ensure output types match what the consuming resource expects:

```hcl
# Wrong — passing a list where a string is expected
output "subnet_ids" {
  value = aws_subnet.private[*].id  # list(string)
}

resource "aws_db_subnet_group" "main" {
  name       = "main"
  subnet_ids = module.vpc.subnet_ids  # expects list(string) — correct
}

# If the downstream resource expects a single string
resource "aws_instance" "web" {
  subnet_id = aws_subnet.private[0].id  # use indexing for single value
}
```

For type conversions:

```hcl
locals {
  # Convert number to string
  port_string = tostring(var.port)

  # Convert string to number
  port_number = tonumber(var.port_string)

  # Convert list to string with join
  subnet_list = join(",", aws_subnet.private[*].id)

  # Convert string to list with split
  cidr_list = split(",", var.cidr_blocks)
}
```

## Common Scenarios

**Scenario 1: Plan fails after provider upgrade**

After upgrading the AWS provider from v4 to v5, several resource arguments were removed. The plan fails with "Invalid attribute" errors. Check the provider migration guide and update affected resource blocks.

**Scenario 2: Null value in plan causes conflict**

A conditional expression evaluates to `null` when a resource is not created. The downstream resource receives a null value and fails validation. Use `coalesce()` or `try()` to provide fallback values.

**Scenario 3: Import conflict during plan**

After importing a resource with `terraform import`, the imported state does not match the configuration. The plan shows a diff for every attribute. Update the configuration to match the imported state, then run `terraform plan` again.

## Prevent It

- **Run `terraform validate` after every change**: Catch syntax and type errors before they reach the plan phase.
- **Use strict types in variables**: Declare `type = string`, `type = number`, or complex types explicitly to prevent type mismatches.
- **Review the provider changelog before upgrades**: Major provider versions often remove or rename arguments. Review the changelog and migration guide before running `terraform init -upgrade`.

## Related Pages

- [Terraform Validation Error](/tools/terraform/terraform-validation-error/) — Configuration syntax issues
- [Terraform Unknown Value Error](/tools/terraform/terraform-unknown-value/) — Known after apply warnings
- [Terraform Cycle Error](/tools/terraform/terraform-cycle-error/) — Circular dependency detection
