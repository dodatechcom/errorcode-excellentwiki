---
title: "[Solution] Terraform Provisioner Timeout"
description: "Fix Terraform provisioner timeout errors when provisioner scripts take too long."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Provisioner timeout errors occur when scripts exceed timeout:

```
Error: timeout

The provisioner timed out after 5m0s while waiting for
the script to complete.
```

## Common Causes

- Script takes longer than expected.
- Network issues causing slow downloads.
- Interactive prompt hanging.

## How to Fix

**Increase the timeout:**

```hcl
provisioner "remote-exec" {
  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    timeout     = "15m"
  }

  inline = ["sudo yum update -y && sudo yum install -y docker"]
}
```

**Break into smaller steps:**

```hcl
provisioner "remote-exec" {
  inline = ["sudo yum update -y"]
}

provisioner "remote-exec" {
  inline = ["sudo yum install -y docker"]
}
```

## Examples

```hcl
provisioner "remote-exec" {
  connection {
    timeout = "30m"
  }
  inline = ["sudo apt-get update && sudo apt-get install -y build-essential"]
}
```
