---
title: "[Solution] Ansible Windows Feature Not Found"
description: "Fix Ansible errors when Windows features cannot be found or installed"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find or install a Windows feature.

```
FAILED! => Feature 'Web-Server' not found
```

## Common Causes

- Feature name incorrect
- Feature not available on OS version
- Source files missing

## How to Fix

```yaml
- name: List Windows features
  ansible.windows.win_feature_info:
  register: features

- name: Install IIS
  ansible.windows.win_feature:
    name:
      - Web-Server
      - Web-Mgmt-Tools
    state: present
    include_sub_features: true
    include_management_tools: true
```
