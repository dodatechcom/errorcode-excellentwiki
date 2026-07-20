---
title: "[Solution] Ansible Windows Reboot Timeout"
description: "Fix Ansible Windows reboot timeout errors during patch management"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible Windows reboot operation times out.

```
FAILED! => "Reboot timeout exceeded"
```

## Common Causes

- Windows update taking too long
- Service preventing reboot
- Timeout value too low
- System hanging during shutdown

## How to Fix

```yaml
- name: Reboot with extended timeout
  ansible.windows.win_reboot:
    reboot_timeout: 1200  # 20 minutes
    pre_reboot_delay: 5
    post_reboot_delay: 30
    msg: "Rebooting for updates"

# Or handle with async
- name: Reboot server
  ansible.windows.win_reboot:
    reboot_timeout: 3600
  async: 3600
  poll: 60
```
