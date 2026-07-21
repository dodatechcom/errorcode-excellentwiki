---
title: "[Solution] Prometheus amtool Error"
description: "How to fix amtool command-line tool errors for Alertmanager"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Wrong Alertmanager URL in amtool config
- amtool version mismatch with Alertmanager version
- Network connectivity issue to Alertmanager
- Invalid alertmanager API request

## How to Fix

Configure amtool:

```bash
# Set Alertmanager URL
amtool --alertmanager.url=http://localhost:9093 alert query

# Or use configuration file
echo "alertmanager.url: http://localhost:9093" > ~/.config/amtool/config.yml
```

Check amtool version:

```bash
amtool --version
```

Test connectivity:

```bash
amtool --alertmanager.url=http://localhost:9093 config routes
```

## Examples

```bash
# List alerts
amtool --alertmanager.url=http://localhost:9093 alert query

# Add silence
amtool --alertmanager.url=http://localhost:9093 silence add alertname=HighErrorRate

# Check configuration
amtool --alertmanager.url=http://localhost:9093 config show
```
