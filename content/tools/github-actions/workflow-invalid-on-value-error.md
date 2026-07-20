---
title: "[Solution] Workflow Invalid On Value Error"
description: "Fix GitHub Actions invalid 'on' value errors when the event trigger value is malformed."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Invalid `on` value errors occur when the event trigger is not a valid string, map, or list:

```
Error: .github/workflows/ci.yml: Invalid type for 'on'
```

## Common Causes

- `on` is set to a string instead of a map.
- `on` uses invalid YAML types.
- Mixed list and map syntax under `on`.

## How to Fix

**Use proper map syntax under `on`:**

```yaml
on:
  push:
    branches:
      - main
      - develop
  pull_request:
    types: [opened, synchronize]
```

## Examples

```yaml
# Wrong - 'on' is a string
on: push

# Correct - 'on' is a map
on:
  push:
    branches: [main]
```
