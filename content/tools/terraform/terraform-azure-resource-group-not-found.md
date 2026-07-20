---
title: "[Solution] Terraform Azure Resource Group Not Found"
description: "Fix Terraform Azure resource group not found errors when the resource group doesn't exist."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Azure resource group not found errors occur when the RG doesn't exist:

```
Error: Error creating Resource Group

ResourceGroupNotFound: Resource group 'my-rg' could not be found.
```

## Common Causes

- Resource group was deleted.
- Wrong resource group name.
- Wrong subscription selected.

## How to Fix

**Create the resource group:**

```hcl
resource "azurerm_resource_group" "main" {
  name     = "my-rg"
  location = "East US"
}
```

**Use data source for existing RG:**

```hcl
data "azurerm_resource_group" "existing" {
  name = "my-rg"
}
```

**Check subscription:**

```bash
az account show
az account set --subscription="SUBSCRIPTION_ID"
```

## Examples

```hcl
resource "azurerm_resource_group" "main" {
  name     = "production-rg"
  location = "East US"

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```
