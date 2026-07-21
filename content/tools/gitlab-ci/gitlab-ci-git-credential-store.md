---
title: "[Solution] GitLab CI Git Credential Store Error"
description: "Fix GitLab CI git credential store errors when the pipeline cannot authenticate for git operations like clone or push."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Git Credential Store Error

Git credential store errors occur when the pipeline fails to authenticate for git operations such as cloning submodules, fetching private dependencies, or pushing artifacts.

## Common Causes

- `CI_JOB_TOKEN` lacks permission for the target repository
- Git credential helper not configured in the runner
- SSH key not added to the project or runner
- Access token used for authentication has expired

## How to Fix

### Solution 1: Use CI_JOB_TOKEN for clone operations

```yaml
variables:
  GIT_SUBMODULE_STRATEGY: recursive
  GIT_SUBMODULE_FORCE_HTTPS: "true"

build_job:
  script:
    - git clone https://gitlab-ci-token:${CI_JOB_TOKEN}@gitlab.example.com/group/project.git
```

### Solution 2: Configure SSH key for push operations

```yaml
deploy_job:
  before_script:
    - eval $(ssh-agent -s)
    - echo "$SSH_PRIVATE_KEY" | ssh-add -
    - mkdir -p ~/.ssh
    - ssh-keyscan gitlab.example.com >> ~/.ssh/known_hosts
  script:
    - git push origin main
```

### Solution 3: Use Git credential store

```yaml
build_job:
  before_script:
    - echo "https://gitlab-ci-token:${CI_JOB_TOKEN}@gitlab.example.com" > ~/.git-credentials
    - git config --global credential.helper store
```

## Examples

```
fatal: could not read Username for 'https://gitlab.example.com'
ERROR: Authentication failed for git clone
```

## Prevent It

- Use `CI_JOB_TOKEN` for most git operations
- Rotate SSH keys regularly
- Verify token scopes match required permissions
