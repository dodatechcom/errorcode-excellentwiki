---
title: "[Solution] Ansible IIS Module Failed"
description: "Fix Ansible IIS management module errors on Windows"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible IIS module fails to manage IIS configuration.

```
FAILED! => "IIS module failed: WebAdministration module not available"
```

## Common Causes

- IIS not installed
- WebAdministration module missing
- Insufficient permissions

## How to Fix

```yaml
# Install IIS first
- name: Install IIS
  ansible.windows.win_feature:
    name: Web-Server
    state: present

# Then manage IIS
- name: Create IIS site
  community.windows.win_iis_webbinding:
    name: "Default Web Site"
    port: 80
    protocol: http
    state: present
```
