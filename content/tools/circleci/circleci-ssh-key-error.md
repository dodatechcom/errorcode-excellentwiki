---
title: "[Solution] CircleCI SSH Key Error"
description: "Fix CircleCI ssh key errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI SSH Key Error

CircleCI SSH key errors occur when SSH keys are not configured correctly for deployment or access.

## Why This Happens

- Key not added
- Fingerprint mismatch
- Permissions denied
- Key format invalid

## Common Error Messages

- `ssh_key_not_found`
- `ssh_fingerprint_error`
- `ssh_permission_denied`
- `ssh_key_invalid`

## How to Fix It

### Solution 1: Add SSH key

Add in Project Settings > SSH Keys.

### Solution 2: Use fingerprints

Reference keys by fingerprint:

```yaml
add_ssh_keys:
  fingerprints:
    - "ab:cd:ef:12:34:56:78:90"
```

### Solution 3: Fix permissions

Ensure the key has appropriate permissions on the target server.


## Common Scenarios

- **Key not found:** Verify the key is added in project settings.
- **Permission denied:** Check the key has access to the target repository.

## Prevent It

- Use fingerprints
- Add deploy keys
- Verify key permissions
