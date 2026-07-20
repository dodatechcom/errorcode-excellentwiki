---
title: "[Solution] GitHub Actions Token Exchange Error"
description: "Fix GitHub Actions token exchange errors in OIDC workflows."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Token exchange errors occur when the OIDC token cannot be exchanged for cloud credentials:

```
Error: token exchange failed: invalid_grant
```

## Common Causes

- OIDC token expired.
- Audience claim does not match.
- Token format is invalid.

## How to Fix

**Verify audience configuration:**

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
      aws-region: us-east-1
```

## Examples

```yaml
# Verify the token is being requested correctly
- name: Debug OIDC
  run: |
    TOKEN=$(curl -s -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN"       "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=https://sts.amazonaws.com" | jq -r '.value')
    echo "Token length: ${#TOKEN}"
```
