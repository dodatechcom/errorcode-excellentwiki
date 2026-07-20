---
title: "[Solution] Ansible Invalid Inventory Format"
description: "Fix Ansible inventory file format and syntax errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot parse the inventory file format.

```
ERROR! Failed to parse inventory file
```

## Common Causes

- YAML syntax errors in inventory
- INI format issues
- Mixed format not supported
- Missing required fields

## How to Fix

```ini
# INI format
[webservers]
web1 ansible_host=192.168.1.100
web2 ansible_host=192.168.1.101

[webservers:vars]
http_port=80
ansible_user=admin

# YAML format
---
all:
  children:
    webservers:
      hosts:
        web1:
          ansible_host: 192.168.1.100
        web2:
          ansible_host: 192.168.1.101
      vars:
        http_port: 80
```
