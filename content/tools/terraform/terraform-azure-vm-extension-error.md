---
title: "[Solution] Terraform Azure VM Extension Error"
description: "Fix Terraform Azure VM extension errors when deploying VM extensions fails."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Azure VM extension errors occur when extensions fail to deploy:

```
Error: Error creating Virtual Machine Extension

compute.VirtualMachineExtensionsClient#CreateOrUpdate: Failure
Code: VMExtensionProvisioningError
```

## Common Causes

- Extension version not compatible with VM OS.
- VM not fully provisioned when extension runs.
- Required agent not installed on VM.

## How to Fix

**Add explicit dependency on VM:**

```hcl
resource "azurerm_virtual_machine_extension" "example" {
  name                 = "custom-script"
  virtual_machine_id   = azurerm_virtual_machine.example.id
  publisher            = "Microsoft.Azure.Extensions"
  type                 = "CustomScript"
  type_handler_version = "2.1"

  settings = jsonencode({
    commandToExecute = "echo 'Hello World'"
  })

  depends_on = [azurerm_virtual_machine.example]
}
```

## Examples

```hcl
resource "azurerm_virtual_machine_extension" "example" {
  name                 = "custom-script"
  virtual_machine_id   = azurerm_virtual_machine.example.id
  publisher            = "Microsoft.Azure.Extensions"
  type                 = "CustomScript"
  type_handler_version = "2.1"

  settings = jsonencode({
    commandToExecute = "apt-get update && apt-get install -y nginx"
  })
}
```
