---
title: "[Solution] Terraform Puppet Provisioner Error"
description: "Fix Terraform Puppet provisioner errors when Puppet agent fails during provisioning."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Puppet provisioner errors occur when the Puppet agent fails:

```
Error: Puppet provisioner error

Puppet agent run failed: Error: Could not find environment
'manifests' on server
```

## Common Causes

- Puppet server not configured.
- Puppet agent not installed.
- Module path incorrect.

## How to Fix

**Install Puppet before provisioning:**

```hcl
provisioner "remote-exec" {
  inline = [
    "wget https://apt.puppet.com/puppet-tools-release-focal.deb",
    "sudo dpkg -i puppet-tools-release-focal.deb",
    "sudo apt-get update",
    "sudo apt-get install -y puppet-agent"
  ]
}
```

**Configure provisioner correctly:**

```hcl
provisioner "puppet" {
  server       = "puppet.example.com"
  certname     = "web-${self.id}"
  module_paths = ["/etc/puppetlabs/code/environments/production/modules"]
}
```

## Examples

```hcl
provisioner "puppet" {
  server       = var.puppet_server
  certname     = self.private_dns
  module_paths = ["/etc/puppet/modules"]
}
```
