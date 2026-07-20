---
title: "[Solution] GitHub Actions Action Deprecation Warning"
description: "Fix GitHub Actions action deprecation warnings."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Action deprecation warnings indicate the action is using outdated features:

```
Warning: The 'set-output' command is deprecated
```

## Common Causes

- Action uses deprecated workflow commands.
- Action uses deprecated Node.js version.

## How to Fix

**Update workflow commands:**

```yaml
# Old (deprecated)
- run: echo "::set-output name=result::value"

# New
- run: echo "result=value" >> $GITHUB_OUTPUT
```

**Update the action version:**

```yaml
# Old
- uses: actions/checkout@v3

# New
- uses: actions/checkout@v4
```

## Examples

```yaml
# Modern output syntax
steps:
  - id: step1
    run: echo "result=success" >> $GITHUB_OUTPUT
  - run: echo ${{ steps.step1.outputs.result }}
```
