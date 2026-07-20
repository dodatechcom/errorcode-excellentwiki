---
title: "[Solution] Terraform Remote-exec Script Not Found"
description: "Fix Terraform remote-exec script not found errors when the script file is missing."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Remote-exec script not found errors occur when referencing a missing script:

```
Error: Script file not found

The script file "scripts/provision.sh" referenced in
remote-exec provisioner does not exist.
```

## Common Causes

- Script file deleted or not created.
- Path is wrong relative to working directory.

## How to Fix

**Use inline commands instead:**

```hcl
provisioner "remote-exec" {
  inline = [
    "sudo apt-get update",
    "sudo apt-get install -y nginx",
    "sudo systemctl enable nginx"
  ]
}
```

**Ensure script exists:**

```bash
mkdir -p scripts
cat > scripts/provision.sh << 'EOF'
#!/bin/bash
sudo apt-get update
sudo apt-get install -y nginx
EOF
```

## Examples

```hcl
provisioner "remote-exec" {
  inline = [
    "sudo systemctl start docker",
    "docker pull nginx:latest",
    "docker run -d -p 80:80 nginx"
  ]
}
```
