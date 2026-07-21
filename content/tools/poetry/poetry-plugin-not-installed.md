---
title: "[Solution] Poetry Plugin Not Installed -- Fix Missing Poetry Plugin"
description: "Fix Poetry plugin not installed errors when a required Poetry plugin is missing. Install the plugin and verify it is loaded."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry tried to use a plugin that is not installed. Plugins extend Poetry's functionality but must be installed separately.

## Common Causes

- The plugin was never installed
- The plugin was removed during an upgrade
- The plugin is incompatible with the current Poetry version
- The plugin name is misspelled

## How to Fix

### 1. List Installed Plugins

```bash
poetry self show plugins
```

### 2. Install the Plugin

```bash
poetry self add poetry-plugin-name
```

### 3. Update the Plugin

```bash
poetry self add --upgrade poetry-plugin-name
```

### 4. Check Plugin Compatibility

```bash
poetry --version
# Check plugin docs for compatible versions
```

## Examples

```bash
$ poetry export -f requirements.txt
PluginNotFoundError: poetry-plugin-export is not installed

$ poetry self add poetry-plugin-export
$ poetry export -f requirements.txt -o requirements.txt
```
