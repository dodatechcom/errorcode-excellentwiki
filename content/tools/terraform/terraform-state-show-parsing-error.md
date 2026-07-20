---
title: "[Solution] Terraform State Show Parsing Error"
description: "Fix Terraform state show parsing errors when displaying resource attributes from state."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

State show parsing errors occur when the output format cannot be parsed:

```
Error: Error reading state

Error: invalid resource address "aws_instance.web["
```

## Common Causes

- Malformed resource address.
- Special characters in resource names.

## How to Fix

**Use quotes for addresses:**

```bash
terraform state show 'aws_instance.web[0]'
```

**Use JSON output:**

```bash
terraform show -json | jq '.values.root_module.resources[]'
```

## Examples

```bash
terraform state show aws_instance.web
terraform show -json | jq '.values.root_module.resources[] | select(.type=="aws_instance")'
```
