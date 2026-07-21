---
title: "[Solution] Grafana Plugin Signature Invalid"
description: "How to fix Grafana plugin signature errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Plugin not signed by Grafana
- Modified plugin files
- Plugin from unofficial repository

## How to Fix

```ini
[plugins]
allow_loading_unsigned_plugins = my-custom-plugin
```

## Examples

```bash
grafana-cli plugins install grafana-clock-panel --force
```
