---
title: "[Solution] Terraform Chef Provisioner Error"
description: "Fix Terraform Chef provisioner errors when Chef client fails during provisioning."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Chef provisioner errors occur when the Chef client fails:

```
Error: Chef provisioner error

Chef client failed to converge: runtime error: no Chef
client binary found in PATH
```

## Common Causes

- Chef client not installed on target.
- Chef server unreachable.
- Invalid run list or attributes.

## How to Fix

**Install Chef before provisioning:**

```hcl
provisioner "remote-exec" {
  inline = [
    "curl -L https://omnitruck.chef.io/install.sh | bash",
    "chef-client --version"
  ]
}
```

**Use correct Chef configuration:**

```hcl
provisioner "chef" {
  server_url          = "https://chef.example.com"
  validation_key_path = "~/.chef/validation.pem"
  node_name           = self.id
  run_list            = ["role[webserver]"]
}
```

## Examples

```hcl
provisioner "chef" {
  server_url          = var.chef_server_url
  validation_key_path = var.chef_validation_key
  node_name           = "web-${self.id}"
  run_list            = ["role[base]", "role[webserver]"]
  environment         = var.chef_environment
}
```
