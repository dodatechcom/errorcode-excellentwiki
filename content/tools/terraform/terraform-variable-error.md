---
title: "[Solution] Terraform Variable Not Defined or Invalid Error — How to Fix"
description: "Fix Terraform variable errors including undefined variables, type mismatches, validation failures, and missing values with step-by-step fixes."
comments: true
---

A Terraform variable not defined or invalid error occurs when a variable is referenced in the configuration but has no value assigned, or when the provided value does not match the expected type or validation constraints. This halts planning and application of changes.

## Why It Happens

Variable errors are among the most common Terraform issues, especially as configurations grow in complexity. They occur because:

- **Missing variable definition**: A variable is referenced but not declared in a `variable` block or passed via a `.tfvars` file.
- **Type mismatch**: A string is passed where a number, list, or map is expected, or vice versa.
- **Validation constraint failure**: A custom validation rule rejects the provided value (e.g., the value is not in an allowed list).
- **No default and no value**: A variable without a default value is not provided in any `terraform.tfvars`, `*.auto.tfvars`, or CLI flag.
- **Sensitive variable handling**: Attempting to reference a sensitive variable in a context where Terraform requires a concrete value during planning.
- **Environment variable mismatch**: The `TF_VAR_*` environment variable name does not match the variable declaration.

## Common Error Messages

**Error: Required variable not set**

```
Error: Missing required argument

The argument "instance_type" is required, but no definition was found.

A module "ec2" requires a value for "instance_type" that was not
provided. Use the "-var" flag or a "*.tfvars" file to set it.
```

**Error: Invalid variable type**

```
Error: Invalid value for variable "port"

The variable "port" must be a number, but got a string value:
"8080"

  variable "port" {
    type = number
  }

  Provided value: port = "8080"
```

**Error: Variable validation failed**

```
Error: Invalid value for variable "environment"

The variable "environment" must be one of: dev, staging, prod.
Got value: "production"

  variable "environment" {
    type = string

    validation {
      condition     = contains(["dev", "staging", "prod"], var.environment)
      error_message = "Environment must be dev, staging, or prod."
    }
  }
```

**Error: Variable used before defined**

```
Error: Reference to undeclared variable

A variable named "vpc_cidr" has not been declared in module.root.
Check the variable block and ensure the name matches.
```

## How to Fix It

### Solution 1: Provide missing variable values

Create a `terraform.tfvars` file or pass values via the command line:

```bash
# Pass via command line
terraform plan -var="instance_type=t3.micro" -var="environment=prod"

# Pass via variable file
terraform plan -var-file="prod.tfvars"

# Set via environment variable
export TF_VAR_instance_type=t3.micro
export TF_VAR_environment=prod
terraform plan
```

Example `terraform.tfvars`:

```hcl
instance_type = "t3.micro"
environment   = "prod"
vpc_cidr      = "10.0.0.0/16"

tags = {
  Project = "web-app"
  Team    = "platform"
}
```

### Solution 2: Fix type mismatches

Ensure the value type matches the variable declaration:

```hcl
# Variable expects a number
variable "port" {
  type        = number
  description = "The port to expose"
  default     = 8080
}

# Correct — numeric value
port = 8080

# Wrong — string value
port = "8080"

# For complex types, use proper syntax
variable "subnets" {
  type = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "tags" {
  type = map(string)
  default = {
    Environment = "prod"
    Team        = "platform"
  }
}
```

### Solution 3: Fix validation constraints

Adjust the value to satisfy validation rules, or update the validation if the constraint is too strict:

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"

  validation {
    condition = contains(
      ["dev", "staging", "prod"],
      var.environment
    )
    error_message = "Must be dev, staging, or prod."
  }
}

# Correct values
environment = "prod"     # valid
environment = "dev"      # valid
environment = "staging"  # valid

# Invalid values
environment = "production"  # fails validation
environment = "PROD"        # fails validation (case-sensitive)
```

### Solution 4: Use optional variables with defaults for flexibility

Make variables optional by providing sensible defaults:

```hcl
variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t3.micro"
}

variable "enable_monitoring" {
  type        = bool
  description = "Enable detailed monitoring"
  default     = false
}

variable "custom_tags" {
  type        = map(string)
  description = "Additional tags to apply"
  default     = {}
}

# Usage — all optional, no errors when omitted
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type

  monitoring = var.enable_monitoring

  tags = merge(
    { Name = "web-server" },
    var.custom_tags
  )
}
```

## Common Scenarios

**Scenario 1: Module variable not passed from root**

A module declares `variable "db_password" { type = string }` without a default. The root module calls the module without passing this variable. Terraform errors during plan. The fix is to pass the variable in the module call or add a default.

**Scenario 2: Variable file not loaded due to naming**

A custom variable file `production.tfvars` is created but not referenced. Terraform only auto-loads `*.auto.tfvars` files. Either rename the file to `production.auto.tfvars` or pass it explicitly with `-var-file="production.tfvars"`.

**Scenario 3: Conditional variable defaults with validation**

A variable uses a validation rule that references another variable. If the referenced variable is not yet resolved, validation fails. Restructure the validation to only depend on the variable's own value.

## Prevent It

- **Declare defaults for all optional variables**: Avoid requiring values that have sensible defaults. Use `default` in variable blocks for non-critical settings.
- **Use `*.auto.tfvars` for environment configs**: Name environment-specific files like `dev.auto.tfvars` so they load automatically.
- **Run `terraform validate` before plan**: Catch variable declaration issues early by validating configuration before planning changes.

## Related Pages

- [Terraform Output Error](/tools/terraform/terraform-output-error/) — Output value issues
- [Terraform Validation Error](/tools/terraform/terraform-validation-error/) — Configuration syntax errors
- [Terraform Plan Error](/tools/terraform/terraform-plan-error/) — Plan-time failures
