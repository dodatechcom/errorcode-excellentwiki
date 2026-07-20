---
title: "[Solution] Ansible pip Module Failed"
description: "Fix Ansible pip module errors when installing Python packages"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible pip module fails to install Python packages.

```
FAILED! => "Could not find a version that satisfies the requirement"
```

## Common Causes

- Package name incorrect
- pip version mismatch
- Network issues (PyPI unreachable)
- Dependency conflicts

## How to Fix

```yaml
- name: Install Python packages
  ansible.builtin.pip:
    name:
      - django>=3.2
      - celery>=5.0
    state: present
    executable: pip3

- name: Install from requirements
  ansible.builtin.pip:
    requirements: /opt/app/requirements.txt
    virtualenv: /opt/app/venv
```
