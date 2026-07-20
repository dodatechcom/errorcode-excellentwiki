---
title: "[Solution] Ansible Mitogen Connection Error"
description: "Fix Ansible Mitogen strategy connection and compatibility errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible Mitogen connection plugin fails to establish connections.

```
ERROR! mitogen: ConnectionError: [Errno 111] Connection refused
```

## Common Causes

- Mitogen not installed
- Mitogen incompatible with Ansible version
- Python version mismatch
- Connection type not supported by Mitogen

## How to Fix

```bash
pip install mitogen
python3 -c "import mitogen; print(mitogen.__version__)"
```

```ini
# ansible.cfg
[defaults]
strategy = mitogen_linear
strategy_plugins = /path/to/mitogen/ansible_mitogen/plugins/strategy
```

```yaml
- name: Fast execution with Mitogen
  hosts: all
  strategy: mitogen_linear
```
