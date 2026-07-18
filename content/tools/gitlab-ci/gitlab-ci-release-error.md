---
title: "[Solution] GitLab CI Release Error"
description: "Fix GitLab CI release errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Release Error

Release errors occur when GitLab CI release jobs fail to create or publish releases.

## Why This Happens

- Tag does not exist
- release-cli not used
- Asset URLs inaccessible
- Release notes failed

## Common Error Messages

- `release_creation_failed`
- `release_asset_error`
- `release_tag_error`
- `release_auth_error`

## How to Fix It

### Solution 1: Ensure tag exists

Run release jobs on tag events:

```yaml
release:
  stage: release
  rules:
    - if: $CI_COMMIT_TAG
  script:
    - release-cli create --tag-name $CI_COMMIT_TAG --description "Release $CI_COMMIT_TAG"
```

### Solution 2: Install release-cli

Use the official release-cli Docker image or install it in before_script.

### Solution 3: Add release assets

Attach binaries and links to your release:

```yaml
  release:
    tag_name: $CI_COMMIT_TAG
    assets:
      links:
        - name: "Binary"
          url: "https://example.com/app-${CI_COMMIT_TAG}.tar.gz"
```


## Common Scenarios

- **Tag not found:** Push the tag before the release job.
- **Permission denied:** Ensure the CI job token has release permissions.

## Prevent It

- Run on tag events
- Use official release-cli
- Generate notes from changelogs
