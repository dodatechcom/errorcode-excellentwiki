---
title: "[Solution] GitLab CI Pipeline Error"
description: "Fix GitLab CI pipeline errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Pipeline Error

GitLab CI pipeline errors occur when the CI/CD pipeline cannot be triggered, parsed, or executed. This typically happens due to misconfigured `.gitlab-ci.yml` files, unavailable runners, or permission issues.

## Why This Happens

- Misconfigured .gitlab-ci.yml file
- No runners with matching tags
- Invalid YAML syntax
- Permission denied

## Common Error Messages

- `pipeline_not_found: no such pipeline`
- `stuck_in_pending: no runners available`
- `yaml_invalid: syntax error`
- `pipeline_creation_failed`

## How to Fix It

### Solution 1: Validate YAML with CI Lint

Use the GitLab CI Lint tool to validate your `.gitlab-ci.yml` before pushing:

```bash
gitlab-ci-lint .gitlab-ci.yml
```

Navigate to CI/CD > Pipelines > CI Lint in the GitLab UI and paste your YAML content for interactive validation.

### Solution 2: Configure shared runners

Enable shared runners in Settings > CI/CD > Runner. For group-level runners, check Settings > CI/CD > Runners in the group.

### Solution 3: Fix permission issues

Ensure the project has CI/CD enabled in Settings > General > Visibility, project features, permissions.


## Common Scenarios

- **Pipeline stuck in pending:** No runners with matching tags — register or enable shared runners.
- **Pipeline not triggered:** Check if CI/CD is enabled in project settings and if the branch matches your rules.

## Prevent It

- Always validate with CI Lint before pushing
- Tag runners to match job requirements
- Enable CI/CD in project settings
