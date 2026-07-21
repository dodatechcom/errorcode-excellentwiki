---
title: "[Solution] Ansible Role Dependency Missing"
description: "Fix Ansible role dependency errors when required dependent roles are not installed or found."
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

# Ansible Role Dependency Missing

Ansible cannot find a role listed as a dependency in `meta/main.yml`.

```
ERROR! the role 'geerlingguy.docker' was not found
```

## Common Causes

- Role not installed via ansible-galaxy
- Incorrect role name in dependencies
- Galaxy server unreachable
- Requirements file outdated
- Role version constraint not met

## How to Fix

### Install Dependencies Automatically

```bash
ansible-galaxy install -r requirements.yml
```

### Define Requirements File

```yaml
# requirements.yml
roles:
  - name: geerlingguy.docker
    version: "6.1.0"
  - name: geerlingguy.nginx
    version: "3.1.0"

collections:
  - name: community.general
    version: ">=5.0.0"
```

### Install from Galaxy and SCM

```yaml
# requirements.yml
roles:
  - name: custom-role
    src: https://github.com/example/custom-role.git
    version: main
    scm: git
```

### Check Role Path

```bash
# List installed roles
ansible-galaxy list

# Check role paths
ansible-config dump | grep ROLES_PATH
```

### Inline Dependencies in Playbook

```yaml
- name: Deploy with inline dependency
  hosts: webservers
  roles:
    - role: geerlingguy.docker
      vars:
        docker_users:
          - deploy
    - role: custom-app
      vars:
        app_port: 8080
```

## Examples

```bash
# Force reinstall all roles
ansible-galaxy install -r requirements.yml --force

# Install to custom path
ansible-galaxy install -r requirements.yml -p ./roles
```
