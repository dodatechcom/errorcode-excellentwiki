---
title: "[Solution] Terraform Depends_on Cycle"
description: "Fix Terraform depends_on cycle errors when circular dependencies are detected."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Dependency cycle errors occur when resources form a circular dependency:

```
Error: Cycle: aws_instance.web, aws_security_group.web, aws_instance.api
```

## Common Causes

- Resource A depends on B, and B depends on A.
- Implicit dependency through attribute references creates a loop.

## How to Fix

**Refactor to break the cycle:**

```hcl
resource "aws_security_group" "shared" {
  name = "shared-sg"
}

resource "aws_instance" "web" {
  vpc_security_group_ids = [aws_security_group.shared.id]
}

resource "aws_instance" "api" {
  vpc_security_group_ids = [aws_security_group.shared.id]
}
```

**Analyze the dependency graph:**

```bash
terraform graph | dot -Tpng > graph.png
```

## Examples

```bash
terraform graph > graph.dot
dot -Tpng graph.dot > graph.png
```
