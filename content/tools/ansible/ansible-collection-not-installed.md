---
title: "[Solution] Ansible Collection Not Installed"
description: "Fix Ansible errors when required collections are not installed"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find the specified collection.

```
ERROR! couldn't resolve module/action 'community.docker.docker_container'
```

## Common Causes

- Collection not installed
- Collection version mismatch
- Collection from different namespace

## How to Fix

```bash
ansible-galaxy collection install community.docker
ansible-galaxy collection install -r requirements.yml
```

```yaml
# requirements.yml
---
collections:
  - name: community.docker
    version: ">=3.0.0"
  - name: community.general
  - name: amazon.aws
```
