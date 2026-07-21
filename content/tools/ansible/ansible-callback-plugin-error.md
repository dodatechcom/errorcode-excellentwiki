---
title: "[Solution] Ansible Callback Plugin Error"
description: "Fix Ansible callback plugin errors when custom callbacks fail to load or execute during playbook runs."
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

# Ansible Callback Plugin Error

Ansible callback plugin errors occur when custom or built-in callback plugins fail to initialize or execute.

```
ERROR! Failed to load callback plugin
```

## Common Causes

- Missing callback plugin file
- Incorrect plugin class inheritance
- Python dependency not installed
- Plugin path not configured in ansible.cfg
- Syntax error in the callback plugin code

## How to Fix

### Configure Plugin Path

```ini
# ansible.cfg
[defaults]
callback_plugins = ./plugins/callback
stdout_callback = yaml
```

### Minimal Callback Plugin

```python
# plugins/callback/custom_callback.py
from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'custom_callback'

    def v2_runner_on_ok(self, result):
        print(f"Task {result._task.get_name()} succeeded")
```

### Install Missing Dependencies

```bash
pip install <missing-dependency>
```

### Check Plugin Directory Structure

```bash
ls -la plugins/callback/
# Ensure __init__.py exists if using a package
touch plugins/callback/__init__.py
```

## Examples

```ini
# Enable multiple callbacks
[defaults]
callback_whitelist = timer, profile_tasks
stdout_callback = yaml
```

```python
# Disable a callback for specific plays
- name: Play without timer
  hosts: all
  vars:
    timer_enabled: false
  tasks:
    - debug:
        msg: "Timer disabled here"
```
