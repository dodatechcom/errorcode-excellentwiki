---
title: "[Solution] Terraform Ansible Provisioner Error"
description: "Fix Terraform Ansible provisioner errors when Ansible playbook execution fails."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible provisioner errors occur when Ansible cannot run the playbook:

```
Error: local-exec provisioner error

Error: playbook not found: playbooks/setup.yml
```

## Common Causes

- Playbook file path wrong.
- Ansible not installed locally.
- SSH connectivity issues.

## How to Fix

**Use correct playbook path:**

```hcl
provisioner "local-exec" {
  command = "ansible-playbook -i '${self.public_ip},' -u ec2-user ${path.module}/playbooks/setup.yml"
}
```

**Install Ansible locally:**

```bash
pip install ansible
```

## Examples

```hcl
provisioner "local-exec" {
  command = <<-EOT
    ansible-playbook
    -i '${self.public_ip},'
    -u ec2-user
    --private-key ~/.ssh/deploy_key
    -e 'env=production'
    playbooks/deploy.yml
  EOT
  working_dir = path.module
}
```
