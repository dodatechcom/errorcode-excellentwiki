---
title: "[Solution] GitHub Actions Composite Action Error"
description: "Fix GitHub Actions composite action configuration errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Composite action errors occur when the action YAML is malformed:

```
Error: Invalid composite action: 'runs' section is required
```

## Common Causes

- Missing `runs` section.
- Invalid `using` value.
- Incorrect step syntax in composite action.

## How to Fix

**Use proper composite action format:**

```yaml
name: 'My Composite Action'
description: 'A composite action'
inputs:
  node-version:
    description: 'Node.js version'
    required: true
    default: '20'
runs:
  using: 'composite'
  steps:
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}
    - run: npm ci
      shell: bash
```

## Examples

```yaml
# .github/actions/my-action/action.yml
name: 'Build and Test'
description: 'Runs build and tests'
inputs:
  config:
    required: false
    default: 'default'
runs:
  using: 'composite'
  steps:
    - run: echo "Config: ${{ inputs.config }}"
      shell: bash
```
