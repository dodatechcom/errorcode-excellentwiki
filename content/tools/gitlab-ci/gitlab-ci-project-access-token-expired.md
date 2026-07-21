---
title: "[Solution] GitLab CI Project Access Token Expired"
description: "Fix GitLab CI project access token expired errors when pipelines fail because authentication tokens have reached their expiration date."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Project Access Token Expired

Project access token expired errors occur when a token used for pipeline authentication has reached its expiration date and can no longer authenticate API or git operations.

## Common Causes

- Token was created with a fixed expiration date that has passed
- Token was created with no expiration but was manually revoked
- Token rotation process did not update CI/CD variables
- Group-level token expired affecting all child projects

## How to Fix

### Solution 1: Create a new project access token

Navigate to **Settings > Access Tokens** and create a new token:

```bash
# Test the new token
curl --header "PRIVATE-TOKEN: NEW_TOKEN" \
  "$CI_API_V4_URL/projects/$CI_PROJECT_ID"
```

### Solution 2: Update the CI/CD variable with the new token

```yaml
# In Settings > CI/CD > Variables, update DEPLOY_TOKEN
deploy_job:
  script:
    - echo $DEPLOY_TOKEN | docker login -u deploy-token --password-stdin $CI_REGISTRY
```

### Solution 3: Set up token rotation with API

```bash
# Create new token and update variable via API
NEW_TOKEN=$(curl -s --request POST \
  --header "PRIVATE-TOKEN: $ADMIN_TOKEN" \
  --data "name=ci-deploy" \
  --data "scopes[]=write_repository" \
  --data "expires_at=2026-12-31" \
  "$CI_API_V4_URL/projects/$CI_PROJECT_ID/access_tokens" | jq -r '.token')
```

## Examples

```
401 Unauthorized: token is expired
fatal: Authentication failed for 'https://gitlab.example.com/'
```

## Prevent It

- Set calendar reminders before token expiration
- Use long-lived tokens for CI/CD with periodic rotation
- Monitor token expiration in **Settings > Access Tokens**
