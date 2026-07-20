---
title: "[Solution] GitHub Actions Download Artifact Not Found"
description: "Fix GitHub Actions download-artifact not found errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Download artifact not found errors occur when the artifact does not exist:

```
Error: Artifact 'my-artifact' not found
```

## Common Causes

- Artifact was not uploaded in a previous job.
- Artifact name is incorrect.
- Artifact expired (retention period exceeded).

## How to Fix

**Use correct artifact name:**

```yaml
steps:
  - uses: actions/download-artifact@v4
    with:
      name: my-artifact
      path: ./artifacts
```

## Examples

```yaml
# Download from specific workflow run
- uses: actions/download-artifact@v4
  with:
    name: build-output
    github-token: ${{ secrets.GITHUB_TOKEN }}
    run-id: ${{ github.event.workflow_run.id }}
```
