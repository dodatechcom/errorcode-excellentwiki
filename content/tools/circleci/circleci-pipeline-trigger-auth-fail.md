---
title: "[Solution] CircleCI Pipeline Trigger Auth Fail"
description: "Fix CircleCI pipeline trigger authentication failures when the API token or trigger mechanism is invalid or expired."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Pipeline Trigger Auth Fail

Pipeline trigger authentication failures occur when the API token, trigger, or webhook mechanism used to start a pipeline is invalid, expired, or lacks the required permissions.

## Common Causes

- API token has been revoked or expired
- Trigger token does not match the project
- GitHub webhook secret is misconfigured
- Project-level API permissions are restricted
- Organization-level settings block external triggers

## How to Fix

### Solution 1: Generate a new personal API token

Navigate to **CircleCI > User Settings > Personal API Tokens** and create a new token.

```bash
# Test the new token
curl -H "Circle-Token: $NEW_TOKEN" \
  "https://circleci.com/api/v2/me"
```

### Solution 2: Update webhook configuration

```yaml
# In GitHub repository settings, verify webhook URL and secret
# Webhook URL: https://circleci.com/api/v2/project/gh/owner/repo/github
```

### Solution 3: Use pipeline triggers correctly

```bash
# Trigger a pipeline with a trigger token
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"branch":"main","tag":"v1.0.0"}' \
  "https://circleci.com/api/v2/project/gh/owner/repo/pipeline/trigger/$TRIGGER_TOKEN"
```

## Examples

```
Error: 401 Unauthorized - Invalid API token
Error: Trigger token is not valid for this project
```

## Prevent It

- Rotate API tokens regularly
- Store trigger tokens securely as environment variables
- Verify webhook configuration after project transfers
