---
title: "[Solution] GitHub Actions Secret Name Invalid"
description: "Fix GitHub Actions secret name invalid errors when storing or referencing secrets."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Secret name invalid errors occur when the secret name contains invalid characters:

```
Error: Secret name 'MY-SECRET_NAME' is not valid
```

## Common Causes

- Secret name contains spaces or special characters.
- Secret name starts with GITHUB_ (reserved prefix).

## How to Fix

**Use valid secret names:**

```bash
gh secret set MY_SECRET_NAME --body "value"
```

## Examples

```bash
# Valid secret names
API_KEY
DATABASE_URL
DEPLOY_TOKEN_2024

# Invalid names
MY SECRET (space)
MY-SECRET (hyphen)
GITHUB_TOKEN (reserved)
```
