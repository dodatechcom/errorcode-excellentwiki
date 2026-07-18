---
title: "[Solution] CircleCI Trigger Pipeline Error"
description: "Fix CircleCI trigger pipeline errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Trigger Pipeline Error

CircleCI trigger pipeline errors occur when programmatically triggering pipelines fails.

## Why This Happens

- API token invalid
- Pipeline not triggered
- Parameter missing
- Rate limited

## Common Error Messages

- `trigger_api_error`
- `trigger_not_triggered_error`
- `trigger_parameter_error`
- `trigger_rate_error`

## How to Fix It

### Solution 1: Use API to trigger

Trigger a pipeline:

```bash
curl -X POST https://circleci.com/api/v2/project/gh/org/repo/pipeline \
  -H "Content-Type: application/json" \
  -H "Circle-Token: $TOKEN" \
  -d '{"branch": "main"}'
```

### Solution 2: Check API token

Verify the API token has trigger permissions.

### Solution 3: Pass parameters

Include pipeline parameters in the request.


## Common Scenarios

- **API token invalid:** Regenerate the API token.
- **Pipeline not triggered:** Check the API response for errors.

## Prevent It

- Use valid API tokens
- Handle rate limits
- Monitor trigger status
