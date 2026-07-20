---
title: "[Solution] GitHub Actions PAT Not Configured"
description: "Fix GitHub Actions personal access token not configured errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

PAT errors occur when a workflow requires a personal access token but it is not set:

```
Error: HttpError: Not Found
Resource not accessible by personal access token
```

## Common Causes

- PAT not added as a repository secret.
- PAT has expired.
- PAT lacks required scopes.

## How to Fix

**Create and store a PAT:**

```bash
gh secret set PAT_TOKEN --body "ghp_xxxxxxxxxxxx"
```

**Use PAT in workflow:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      token: ${{ secrets.PAT_TOKEN }}
      fetch-depth: 0
```

## Examples

```yaml
# Required scopes for common operations
# repo - Full repository access
# workflow - Update workflows
```
