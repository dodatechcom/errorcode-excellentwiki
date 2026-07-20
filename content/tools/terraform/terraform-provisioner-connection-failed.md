---
title: "[Solution] Terraform Provisioner Connection Failed"
description: "Fix Terraform provisioner connection failed errors when provisioners cannot reach the resource."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Connection failures occur when provisioners cannot connect:

```
Error: connection is shut down

dial tcp 52.1.2.3:22: connect: connection refused
```

## Common Causes

- Resource not fully booted when provisioner runs.
- SSH key not configured correctly.
- Firewall rules blocking connection.

## How to Fix

**Add connection timeout:**

```hcl
provisioner "remote-exec" {
  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    timeout     = "5m"
  }

  inline = ["sudo yum update -y"]
}
```

## Examples

```hcl
connection {
  type        = "ssh"
  host        = self.public_ip
  user        = "ubuntu"
  port        = 22
  private_key = file("~/.ssh/deploy_key")
  agent       = false
  timeout     = "3m"
}
```
