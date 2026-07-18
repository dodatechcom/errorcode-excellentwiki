---
title: "[Solution] CircleCI Retry Error"
description: "Fix CircleCI retry errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Retry Error

CircleCI retry errors occur when automatic or manual retries fail or behave unexpectedly.

## Why This Happens

- Retry limit exceeded
- State not preserved
- Resource conflict
- Orb not compatible

## Common Error Messages

- `retry_failed`
- `retry_limit`
- `state_lost`
- `retry_conflict`

## How to Fix It

### Solution 1: Configure automatic retries

Add retry to steps:

```yaml
- run:
    command: curl -f https://example.com
    retries: 3
```

### Solution 2: Manual retry

Click the retry button in the CircleCI UI.

### Solution 3: Handle resource conflicts

Use unique resource names to avoid conflicts.


## Common Scenarios

- **Retry fails immediately:** Check if the error is permanent (not transient).
- **State lost on retry:** Use workspace to preserve state between retries.

## Prevent It

- Retry transient failures
- Preserve state with workspace
- Set retry limits
