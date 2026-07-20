---
title: "[Solution] Workflow Invalid Event Trigger"
description: "Fix GitHub Actions invalid event trigger errors when the 'on' event is not recognized."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Invalid event trigger errors occur when the `on` key references an event GitHub Actions does not support:

```
Error: .github/workflows/ci.yml: on: Invalid event type 'pussh'
```

## Common Causes

- Misspelled event name in the `on` trigger.
- Using a custom event without defining a `repository_dispatch` properly.
- Capitalization errors (event names are case-sensitive in some contexts).

## How to Fix

**Use valid event names:**

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:
```

**Check available events:**

```bash
actionlint .github/workflows/ci.yml
```

## Examples

```yaml
# Wrong - 'pussh' is not a valid event
on:
  pussh:
    branches: [main]

# Correct
on:
  push:
    branches: [main]
```
