---
title: "[Solution] GitLab CI Cross-Project Access Token"
description: "Fix GitLab CI cross-project access token errors when pipelines cannot access resources in other projects."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Cross-Project Access Token

Cross-project access token errors occur when a pipeline job tries to access another project's resources (artifacts, packages, registries) but the token lacks the required permissions.

## Common Causes

- Project access token does not have `read_api` or `write_repository` scope
- Target project is in a different group without cross-group access
- Token has expired or was revoked
- Personal access token used instead of project access token

## How to Fix

### Solution 1: Create a properly scoped project access token

Navigate to **Settings > Access Tokens** and create a token with:

- `read_api` scope for reading artifacts
- `write_repository` scope for pushing to registry
- `api` scope for full API access

### Solution 2: Use CI_JOB_TOKEN with explicit permissions

```yaml
cross_project_job:
  script:
    - |
      curl --header "JOB-TOKEN: $CI_JOB_TOKEN" \
        "$CI_API_V4_URL/projects/OTHER_PROJECT_ID/artifacts/main.zip" \
        -o artifacts.zip
```

### Solution 3: Use deploy tokens for cross-project access

```yaml
cross_project_job:
  script:
    - git clone https://deploy-token:${DEPLOY_TOKEN}@gitlab.example.com/group/other-project.git
```

## Examples

```
401 Unauthorized: access denied to project
403 Forbidden: token does not have required scope
```

## Prevent It

- Use least-privilege principle for token scopes
- Rotate tokens before expiration
- Use `CI_JOB_TOKEN` for intra-pipeline cross-project access
