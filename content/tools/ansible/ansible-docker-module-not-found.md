---
title: "[Solution] Ansible Docker Module Not Found"
description: "Fix Ansible Docker module errors when Docker modules are not available"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find Docker-related modules.

```
ERROR! no action detected in task. The 'docker_container' module is not available.
```

## Common Causes

- Docker collection not installed
- Using old module names
- Missing Python Docker library

## How to Fix

```bash
ansible-galaxy collection install community.docker
pip install docker
```

```yaml
- name: Create container
  community.docker.docker_container:
    name: my-app
    image: nginx:latest
    state: started
    ports:
      - "8080:80"
```
