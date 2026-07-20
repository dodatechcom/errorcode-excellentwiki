---
title: "[Solution] GitHub Actions Cross-Workflow Artifact Not Available"
description: "Fix GitHub Actions artifact not available across different workflow runs."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cross-workflow artifact errors occur when trying to access artifacts from a different workflow:

```
Error: Artifact from different workflow run is not accessible
```

## Common Causes

- Artifacts are scoped to the current workflow run by default.
- Different workflow trying to access artifacts.

## How to Fix

**Use workflow_run to access artifacts:**

```yaml
on:
  workflow_run:
    workflows: ["Build"]
    types: [completed]

jobs:
  download:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          github-token: ${{ secrets.GITHUB_TOKEN }}
          run-id: ${{ github.event.workflow_run.id }}
```

## Examples

```yaml
- uses: actions/download-artifact@v4
  with:
    name: build-output
    github-token: ${{ github.token }}
    run-id: 12345678
```
