---
title: "[Solution] GitLab CI Release Asset URL Error"
description: "Fix GitLab CI release asset URL errors when release assets reference invalid or inaccessible download URLs."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Release Asset URL Error

Release asset URL errors occur when the `release-cli` command defines assets with URLs that are invalid, inaccessible, or point to non-existent resources.

## Common Causes

- Asset URL points to a build artifact that was not uploaded
- URL contains unencoded special characters
- Link type is not one of the supported values (`runbook`, `image`, `package`)
- Asset file path does not match the artifact path

## How to Fix

### Solution 1: Use CI variables for asset URLs

Construct URLs dynamically using pipeline variables:

```yaml
release:
  stage: release
  script:
    - release-cli create
      --tag-name $CI_COMMIT_TAG
      --name "Release $CI_COMMIT_TAG"
      --assets-link "{\"name\":\"binary\",\"url\":\"${CI_PROJECT_URL}/-/jobs/artifacts/${CI_COMMIT_TAG}/raw/dist/app?job=build\"}"
```

### Solution 2: Verify artifact upload first

Ensure the artifact is uploaded before referencing it:

```yaml
build_binary:
  stage: build
  artifacts:
    paths:
      - dist/app
  script:
    - make build

release:
  stage: release
  needs: [build_binary]
  script:
    - release-cli create --tag-name $CI_COMMIT_TAG
      --assets-link "{\"name\":\"binary\",\"url\":\"${CI_JOB_URL}/artifacts/raw/dist/app\"}"
```

### Solution 3: Validate URL format

```bash
# Test the URL before release
curl -sI "$ASSET_URL" | head -1
```

## Examples

```
Error: release asset URL is not valid
Release creation failed: asset file not found
```

## Prevent It

- Always use `needs` to ensure artifacts are available
- Test asset URLs with curl before release
- Use `direct_asset_path` for file-based assets
