---
title: "[Solution] GitHub Actions ID Token Permission Missing"
description: "Fix GitHub Actions id-token permission missing errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

ID token permission errors occur when the `id-token` permission is not granted:

```
Error: The id-token permission is required for OIDC
```

## Common Causes

- Workflow does not include `id-token: write` in permissions.

## How to Fix

**Add id-token permission:**

```yaml
permissions:
  id-token: write
  contents: read

jobs:
  authenticate:
    runs-on: ubuntu-latest
    steps:
      - name: Get OIDC token
        run: |
          TOKEN=$(curl -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN"             "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=https://example.com" | jq -r '.value')
          echo "Token: $TOKEN"
```

## Examples

```yaml
permissions:
  id-token: write
  contents: read
```
