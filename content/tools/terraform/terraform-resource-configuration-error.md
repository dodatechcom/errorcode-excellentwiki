---
title: "[Solution] Terraform Resource Configuration Error"
description: "Fix Terraform resource configuration errors when resource blocks contain invalid settings."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Resource configuration errors indicate invalid resource block syntax:

```
Error: Invalid resource configuration

resource "aws_instance" "web" has an invalid argument "ami_id".
Did you mean "ami"?
```

## Common Causes

- Argument name typo.
- Deprecated attribute used.

## How to Fix

**Check provider documentation:**

```bash
terraform providers schema -json | jq '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.attributes | keys'
```

## Examples

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.main.id
}
```
