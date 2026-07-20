---
title: "[Solution] Ansible Requirements File Error"
description: "Fix Ansible requirements.yml syntax and format errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible fails to parse the requirements file.

```
ERROR! - AnsibleError: Error parsing requirements.yml
```

## Common Causes

- Invalid YAML syntax
- Missing required fields
- Wrong format version

## How to Fix

```yaml
# Correct requirements.yml format
---
roles:
  - name: nginx
    version: "3.1.0"
  - name: docker
    src: https://github.com/user/role.git
    version: master

collections:
  - name: community.general
    version: ">=5.0.0"
  - name: community.docker
```
