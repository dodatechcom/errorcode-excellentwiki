---
title: "[Solution] CircleCI Artifact Error"
description: "Fix CircleCI artifact errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Artifact Error

CircleCI artifact errors occur when job artifacts fail to upload or be accessed.

## Why This Happens

- Path does not exist
- Artifact size exceeded
- Upload timeout
- Access denied

## Common Error Messages

- `artifact_upload_failed`
- `artifact_not_found`
- `artifact_too_large`
- `artifact_access_error`

## How to Fix It

### Solution 1: Store artifacts correctly

Use store_artifacts:

```yaml
- store_artifacts:
    path: test-results
    destination: results
```

### Solution 2: Store test results

Use store_test_results for test reporting:

```yaml
- store_test_results:
    path: test-results
```

### Solution 3: Set artifact retention

Configure retention policy in project settings.


## Common Scenarios

- **Artifact not found:** Verify the path exists when the step runs.
- **Cannot access artifacts:** Check project permissions and settings.

## Prevent It

- Verify paths exist
- Set appropriate retention
- Use store_test_results
