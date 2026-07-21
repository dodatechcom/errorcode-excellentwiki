---
title: "[Solution] GitLab CI Registry Push Denied"
description: "Fix GitLab CI registry push denied errors. Learn why your pipeline cannot push images to the container registry."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Registry Push Denied

Pipeline jobs fail when they cannot push images to the GitLab Container Registry due to authentication or permission issues.

## Common Causes

- Deploy token lacks `write_registry` scope
- CI job token does not have registry access
- Project container registry is disabled
- Image tag already exists and immutable tags are enforced
- Namespace or project visibility restricts push access

## How to Fix

### Solution 1: Verify deploy token permissions

Ensure your deploy token includes `write_repository` and `read_registry` scopes:

```yaml
deploy_image:
  stage: deploy
  image: docker:24.0
  services:
    - docker:24.0-dind
  script:
    - docker login -u $CI_DEPLOY_USER -p $CI_DEPLOY_PASSWORD $CI_REGISTRY
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
```

### Solution 2: Use CI job token authentication

```bash
echo "$CI_JOB_TOKEN" | docker login -u ci-job-token --password-stdin $CI_REGISTRY
```

### Solution 3: Enable container registry

Navigate to **Settings > General > Visibility, project features, permissions** and ensure the container registry is enabled.

## Examples

```
denied: access forbidden or request has expired
unauthorized: authentication required
```

## Prevent It

- Verify deploy token scopes before pipeline runs
- Use `CI_JOB_TOKEN` for internal registry operations
- Check registry is enabled in project settings
