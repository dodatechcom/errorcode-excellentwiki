---
title: "[Solution] GitLab CI Kaniko Registry Push Error"
description: "Fix GitLab CI Kaniko registry push errors when Kaniko cannot push built images to the container registry."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Kaniko Registry Push Error

Kaniko registry push errors occur when the Kaniko executor cannot push a built Docker image to the target container registry due to authentication, network, or configuration issues.

## Common Causes

- Kaniko `--destination` flag does not include the registry URL
- Registry credentials not passed via Docker config
- Kaniko snapshot mode incompatible with the base image
- Registry rate limiting blocks the push
- TLS certificate not trusted by Kaniko

## How to Fix

### Solution 1: Configure Kaniko with Docker config

```yaml
build_image:
  stage: build
  image:
    name: gcr.io/kaniko-project/executor:debug
    entrypoint: [""]
  before_script:
    - mkdir -p /kaniko/.docker
    - echo "{\"auths\":{\"$CI_REGISTRY\":{\"auth\":\"$(echo -n ${CI_REGISTRY_USER}:${CI_REGISTRY_PASSWORD} | base64)\"}}}" > /kaniko/.docker/config.json
  script:
    - /kaniko/executor
      --context $CI_PROJECT_DIR
      --dockerfile $CI_PROJECT_DIR/Dockerfile
      --destination $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
```

### Solution 2: Use cache for layer reuse

```yaml
build_image:
  script:
    - /kaniko/executor
      --context $CI_PROJECT_DIR
      --cache=true
      --cache-repo=$CI_REGISTRY_IMAGE/cache
      --destination $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
```

### Solution 3: Set snapshot mode for compatibility

```yaml
build_image:
  script:
    - /kaniko/executor
      --context $CI_PROJECT_DIR
      --snapshot-mode=redo
      --destination $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
```

## Examples

```
ERROR: push to registry failed: unauthorized
ERROR: error pushing image: TLS handshake timeout
```

## Prevent It

- Always configure the Docker config for Kaniko
- Use `--cache=true` for faster builds
- Set `--snapshot-mode=redo` for filesystem compatibility
