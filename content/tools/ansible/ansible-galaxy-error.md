---
title: "[Solution] Ansible Galaxy Error"
description: "Fix Ansible Galaxy errors when installing roles and collections"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible Galaxy fails to download or install roles/collections.

```
ERROR! - AnsibleError: Failed to install role/collection from Galaxy
```

## Common Causes

- Network connectivity issues
- Galaxy API rate limiting
- Authentication required
- Role/collection does not exist

## How to Fix

```bash
curl -I https://galaxy.ansible.com
ansible-galaxy role install nginx -vvv
ansible-galaxy login --github
```

```yaml
# requirements.yml
---
roles:
  - name: nginx
    version: "3.1.0"
  - src: https://github.com/user/role.git
    name: my-role
    version: master
```
