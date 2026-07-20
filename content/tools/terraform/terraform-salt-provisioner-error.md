---
title: "[Solution] Terraform Salt Provisioner Error"
description: "Fix Terraform Salt provisioner errors when Salt minion fails during provisioning."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Salt provisioner errors occur when the Salt minion fails:

```
Error: Salt provisioner error

Salt state apply failed: Error: Unable to locate configuration file
```

## Common Causes

- Salt minion not installed.
- Master not reachable.
- Pillar data missing.

## How to Fix

**Install Salt before provisioning:**

```hcl
provisioner "remote-exec" {
  inline = [
    "sudo apt-get update",
    "sudo apt-get install -y salt-minion",
    "echo 'master: ${var.salt_master}' | sudo tee /etc/salt/minion.d/master.conf",
    "sudo systemctl restart salt-minion"
  ]
}
```

**Use correct Salt provisioner config:**

```hcl
provisioner "salt" {
  salt_state     = "webserver"
  salt_master_ip = var.salt_master_ip
  temp_dir       = "/tmp/salt"
}
```

## Examples

```hcl
provisioner "salt" {
  salt_state     = "highstate"
  salt_master_ip = "10.0.1.100"
  environment    = "production"
}
```
