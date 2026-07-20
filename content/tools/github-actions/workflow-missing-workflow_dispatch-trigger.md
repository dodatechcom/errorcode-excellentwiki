---
title: "[Solution] Workflow Missing workflow_dispatch Trigger"
description: "Fix GitHub Actions missing workflow_dispatch trigger for manual workflow runs."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Workflows that need manual triggering require the `workflow_dispatch` event, but it is missing:

```
Error: Workflow does not support manual triggering.
Use 'on: workflow_dispatch' to enable manual runs.
```

## Common Causes

- The `workflow_dispatch` event was not added to the `on` trigger.
- Developer expects to trigger manually but only push/pull_request are defined.

## How to Fix

**Add workflow_dispatch to the on trigger:**

```yaml
on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deploy target'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production
```

## Examples

```yaml
# Without inputs
on:
  workflow_dispatch:

# With inputs
on:
  workflow_dispatch:
    inputs:
      debug:
        description: 'Enable debug logging'
        required: false
        default: 'false'
        type: boolean
```
