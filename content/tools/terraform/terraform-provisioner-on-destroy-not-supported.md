---
title: "[Solution] Terraform Provisioner On Destroy Not Supported"
description: "Fix Terraform provisioner on destroy errors when destroy-time provisioners fail."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Destroy-time provisioner errors occur during resource destruction:

```
Error: Error running provisioner

Provisioner "local-exec" with trigger "destroy" failed:
command exited with status 1
```

## Common Causes

- Cleanup script has errors.
- Resource already destroyed when provisioner runs.

## How to Fix

**Make destroy provisioner idempotent:**

```hcl
provisioner "local-exec" {
  when    = destroy
  command = "rm -f ${path.module}/state/${self.id}.json || true"
}
```

**Add error handling:**

```hcl
provisioner "local-exec" {
  when = destroy
  command = <<-EOT
    set -e || true
    aws s3 rm s3://bucket/${self.id}/ --recursive || true
  EOT
}
```

## Examples

```hcl
provisioner "remote-exec" {
  when = destroy
  inline = [
    "sudo systemctl stop nginx || true",
    "rm -rf /etc/nginx/conf.d/* || true"
  ]
}
```
