---
title: "[Solution] GitHub Actions JavaScript Action Missing"
description: "Fix GitHub Actions JavaScript action missing required files."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

JavaScript action missing errors occur when the action directory does not contain required files:

```
Error: Unable to find action 'my-action' in /github/workspace/
```

## Common Causes

- `action.yml` or `action.yaml` is missing.
- `index.js` entry point is missing.
- `node_modules` not committed.

## How to Fix

**Create proper action.yml:**

```yaml
name: 'My JavaScript Action'
description: 'Does something useful'
runs:
  using: 'node20'
  main: 'dist/index.js'
inputs:
  name:
    description: 'Input name'
    required: true
outputs:
  result:
    description: 'Output result'
```

**Build and commit dist:**

```bash
npm run build
git add dist/
git commit -m "Build action"
```

## Examples

```yaml
# action.yml structure
name: 'My Action'
runs:
  using: 'node20'
  main: 'dist/index.js'
inputs:
  input1:
    required: true
```
