---
title: "[Solution] Terraform Resource Deletion Failed"
description: "Fix Terraform resource deletion failed errors when Terraform cannot destroy a resource."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Resource deletion failures occur during `terraform destroy`:

```
Error: Error deleting Security Group (sg-12345): DependencyViolation

Resource sg-12345 has a dependent object (eni-abc123)
```

## Common Causes

- Dependent resources not destroyed first.
- Resource has deletion protection enabled.

## How to Fix

**Destroy in correct order:**

```bash
terraform destroy -target=aws_instance.web
terraform destroy -target=aws_security_group.web
```

**Disable deletion protection:**

```hcl
resource "aws_db_instance" "main" {
  deletion_protection = false
}
```

## Examples

```bash
terraform graph | dot -Tpng > destroy-graph.png
terraform destroy -target=aws_network_interface.main
```
