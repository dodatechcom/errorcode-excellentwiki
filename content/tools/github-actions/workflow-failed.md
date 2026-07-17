---
title: "Workflow Not Valid: Job Failed"
description: "A GitHub Actions workflow is invalid or a specific job within the workflow has failed during execution."
tools: ["github-actions"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

This error indicates that either the workflow YAML is syntactically invalid or a job in the workflow failed. GitHub Actions will report which job and step failed.

## Common Causes

- Syntax error in the workflow YAML (indentation, missing keys, invalid expressions)
- A step command returned a non-zero exit code
- Required secrets or variables are not configured in the repository
- The runner environment lacks a needed tool or dependency

## How to Fix

Validate your workflow YAML with the `actionlint` tool:

```bash
actionlint .github/workflows/ci.yml
```

Check that all required secrets are set in the repository settings under **Settings > Secrets and variables > Actions**.

Ensure shell commands in steps handle errors properly:

```yaml
- name: Build
  run: |
    set -e
    npm ci
    npm run build
```

Reference the correct runner image with the tools you need:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
```

## Examples

```
Error: .github/workflows/ci.yml is not valid.
Error: jobs.build.steps[2].run: expected a string, got a mapping

Error: Job 'build' failed. Step 'test' exited with code 1.
```

## Related Errors

- [Action Not Found]({{< relref "/tools/github-actions/action-not-found" >}})
