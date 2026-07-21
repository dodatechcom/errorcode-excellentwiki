---
title: "[Solution] Grafana Plugin Unsigned Error"
description: "How to fix Grafana unsigned plugin errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Custom plugin not signed
- Plugin from third-party source
- Enterprise plugin without license

## How to Fix

```ini
[plugins]
allow_loading_unsigned_plugins = custom-plugin-1
disable_signature_validation = true
```

## Examples

```bash
ls -la /var/lib/grafana/plugins/my-plugin/
```
