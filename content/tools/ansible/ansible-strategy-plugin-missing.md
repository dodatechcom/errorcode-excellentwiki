---
title: "[Solution] Ansible Strategy Plugin Missing"
description: "Fix Ansible strategy plugin not found errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot find the specified strategy plugin.

```
ERROR! the strategy plugin 'my_strategy' was not found
```

## Common Causes

- Plugin not installed
- Plugin path not configured
- Plugin name incorrect

## How to Fix

```ini
[defaults]
strategy_plugins = /path/to/custom/strategy/plugins
strategy = custom_strategy
```

```bash
ansible-doc -t strategy -l
ansible-doc -t strategy linear
```
