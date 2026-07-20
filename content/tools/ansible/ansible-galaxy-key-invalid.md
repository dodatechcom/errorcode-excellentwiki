---
title: "[Solution] Ansible Galaxy API Key Invalid"
description: "Fix Ansible Galaxy authentication key errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible Galaxy rejects the API key for authentication.

```
ERROR! - AnsibleError: Invalid Galaxy API key
```

## Common Causes

- Expired API key
- Wrong key format
- Key copied incorrectly

## How to Fix

```bash
ansible-galaxy login --github
```

```ini
# ansible.cfg
[galaxy]
server_list = galaxy, automation_hub

[galaxy_server.galaxy]
url = https://galaxy.ansible.com/
token = your_galaxy_token
```
