---
title: "[Solution] Terraform Output Value Not Set Error — How to Fix"
description: "Fix Terraform output value not set errors including undefined outputs, conditional logic gaps, and reference failures with clear solutions."
comments: true
---

A Terraform output value not set error occurs when an output block references a value that has not been computed, or when outputs depend on resources that were not created during the current operation. This prevents `terraform apply` from completing successfully.

## Why It Happens

Output errors typically surface when the relationship between resources and outputs is not properly defined or when conditional logic leaves outputs unset. Common causes include:

- **Referencing destroyed or conditional resources**: An output references a resource created inside a `count` or `for_each` block where the condition evaluated to zero or an empty map.
- **Circular dependencies**: Outputs and resources reference each other in a cycle, preventing Terraform from resolving the value.
- **Sensitive output handling**: Attempting to display or use outputs marked as `sensitive` in logs or scripts without proper handling.
- **Missing `depends_on`**: An output references a resource that Terraform has not yet fully created due to missing explicit dependency ordering.
- **Incorrect attribute path**: The output references an attribute that does not exist on the target resource or data source.

## Common Error Messages

**Error: Output refers to sensitive value**

```
Error: Output refers to sensitive attributes

The given output value refers to sensitive attributes held on
"aws_db_password.main". To declare an output value as sensitive,
set the sensitive attribute in the output block.
```

**Error: Value not set due to count**

```
Error: Invalid output reference

Output "instance_ip" references resource "aws_instance.web"
which has been removed by count = 0. Output values cannot
reference resources that have been removed.
```

**Error: Reference to undeclared resource**

```
Error: Reference to undeclared output

A managed resource "aws_subnet" "public" has not been declared
in module.root. Did you mean to reference module.root_output?
```

**Error: Output not set when condition is false**

```
Error: Missing output value

The output "db_endpoint" depends on aws_db_instance.main,
but aws_db_instance.main was not created due to
count = 0. Ensure the output is defined within a matching condition.
```

## How to Fix It

### Solution 1: Guard outputs with matching conditions

Ensure outputs respect the same `count` or `for_each` conditions as the resources they reference:

```hcl
resource "aws_instance" "web" {
  count = var.create_instance ? 1 : 0
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
}

output "instance_ip" {
  description = "The public IP of the web instance"
  value       = var.create_instance ? aws_instance.web[0].public_ip : null
}
```

For `for_each` resources:

```hcl
output "all_instance_ips" {
  description = "Map of instance names to public IPs"
  value = {
    for k, v in aws_instance.web : k => v.public_ip
  }
}
```

### Solution 2: Handle sensitive outputs properly

Mark outputs as sensitive or use `nonsensitive()` when you need to reference them in non-sensitive contexts:

```hcl
output "db_password" {
  description = "The database password"
  value       = random_password.db.result
  sensitive   = true
}

# Use nonsensitive() in local values when needed for non-secret processing
locals {
  db_conn_string = "postgres://admin:${nonsensitive(random_password.db.result)}@${aws_db_instance.main.address}"
}
```

### Solution 3: Add explicit dependencies

When outputs depend on resources that Terraform might not detect automatically, use `depends_on`:

```hcl
output "app_url" {
  description = "The URL of the application"
  value       = "https://${aws_lb.main.dns_name}"
  depends_on  = [aws_lb_listener.https]
}
```

For outputs depending on module results:

```hcl
output "vpc_id" {
  description = "VPC ID from network module"
  value       = module.network.vpc_id
  depends_on  = [module.network]
}
```

### Solution 4: Use `try()` and `lookup()` for safe attribute access

Prevent errors when resource attributes might not exist:

```hcl
output "instance_private_dns" {
  description = "Private DNS of the instance"
  value = try(aws_instance.web[0].private_dns, "not-available")
}

output "nat_gateway_ips" {
  description = "NAT gateway public IPs"
  value = {
    for k, v in aws_nat_gateway.main : k => try(v.public_ip, "pending")
  }
}
```

## Common Scenarios

**Scenario 1: Conditionally created database with unconditional output**

A module creates an RDS instance when `var.create_database = true`, but the output always references `aws_db_instance.main[0].endpoint`. When the database is not created, this output fails. The fix is to conditionally set the output value or use `try()`.

```hcl
# Wrong — fails when database is not created
output "db_endpoint" {
  value = aws_db_instance.main[0].endpoint
}

# Correct — handle the conditional case
output "db_endpoint" {
  value = var.create_database ? aws_db_instance.main[0].endpoint : null
}
```

**Scenario 2: Output referencing a module output that changed signature**

After upgrading a module, an output name was renamed or removed. The calling configuration's output block still references the old name, causing an undeclared reference error. Check the module's CHANGELOG for output changes after upgrades.

```bash
# Check module version and outputs
terraform state pull | jq '.values.root_module.outputs'

# Compare with the current module's outputs
cat modules/my-module/outputs.tf
```

**Scenario 3: Sensitive value exposed in plan output**

An output references a secret value like a database password. During `terraform plan`, Terraform warns that the value is sensitive. Marking the output block as `sensitive = true` suppresses the warning but requires careful handling in scripts that consume the output.

**Scenario 4: Output value shows "known after apply"**

An output references an attribute that Terraform cannot determine during planning. This is common with auto-generated IDs or IPs. Use `depends_on` or set the output in a `null_resource` with a `local-exec` provisioner that captures the value after apply.

```hcl
output "instance_public_ip" {
  description = "Public IP of the instance"
  value       = aws_instance.web.public_ip
  depends_on  = [aws_instance.web]
}
```

## Prevent It

- **Always match output conditions to resource conditions**: If a resource uses `count`, ensure outputs referencing it handle the `count = 0` case.
- **Use `try()` for defensive attribute access**: Prevent cascading failures by using `try()` or `lookup()` when accessing attributes that might not exist.
- **Test outputs with `terraform output` after plan**: Run `terraform plan -out=tfplan && terraform show -json tfplan | jq '.values.root_module.outputs'` to validate output values before applying.
- **Use `terraform output` to verify after apply**: After every apply, run `terraform output -json` to confirm outputs contain expected values.

## Related Pages

- [Terraform Variable Error](/tools/terraform/terraform-variable-error/) — Variable definition issues
- [Terraform Unknown Value Error](/tools/terraform/terraform-unknown-value/) — Known after apply warnings
- [Terraform Count Error](/tools/terraform/terraform-count-error/) — Count and for_each issues
