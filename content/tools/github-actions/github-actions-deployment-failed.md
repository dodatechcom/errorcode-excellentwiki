---
title: "[Solution] GitHub Actions Deployment Failed"
description: "Fix GitHub Actions deployment failures in CI/CD pipeline."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Deployment failures occur when the deployment step fails:

```
Error: Deployment failed: exit code 127
Command not found: deploy.sh
```

## Common Causes

- Deploy script does not exist or is not executable.
- Missing credentials for deployment target.

## How to Fix

**Ensure deploy script is executable:**

```yaml
steps:
  - uses: actions/checkout@v4
  - run: chmod +x deploy.sh
  - run: ./deploy.sh
    env:
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

## Examples

```yaml
steps:
  - name: Deploy
    uses: peaceiris/actions-gh-pages@v3
    with:
      github_token: ${{ secrets.GITHUB_TOKEN }}
      publish_dir: ./dist
```
