---
title: "[Solution] GitLab CI Artifact Error"
description: "Fix GitLab CI artifact errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Artifact Error

Artifact errors occur when jobs cannot upload or download build artifacts between pipeline stages. This breaks dependency chains and prevents downstream jobs from accessing required build outputs. Artifacts are the primary mechanism for passing data between jobs in different stages.

## Why This Happens

- Artifact path does not match any files produced by the job
- Artifact exceeds the project's maximum artifact size limit
- Artifact expiration not configured, consuming excessive storage
- Downstream job cannot access artifacts from a previous stage
- Artifact download fails due to network or storage issues

## Common Error Messages

- `artifact_upload_failed: could not upload artifact`
- `artifact_download_failed: artifact not found`
- `artifact_not_found: no matching artifact`
- `artifact_too_large: artifact exceeds size limit`

## How to Fix It

### Solution 1: Verify artifact paths match actual files

Ensure paths match files the job produces:

```yaml
build_job:
  script: make build
  artifacts:
    paths:
      - build/
      - dist/
    expire_in: 1 week
```

Use `ls` in your script to verify files exist before the job ends. Artifact paths support glob patterns like `build/**/*.js`.

### Solution 2: Check and increase artifact size limits

Default max is 100MB. Increase in **Settings > CI/CD > Maximum artifact size**:

```yaml
heavy_build:
  artifacts:
    paths:
      - output/
    expire_in: 1 day
```

For very large artifacts, consider using external storage (S3, GCS) or splitting into smaller chunks.

### Solution 3: Use dependencies/needs for explicit artifact access

Specify which artifacts a job requires:

```yaml
deploy_job:
  dependencies:
    - build_job
  script:
    - ls build/
    - deploy build/
```

If `dependencies` is not specified, all artifacts from previous stages are downloaded, which wastes time and bandwidth.

### Solution 4: Set expiration to manage storage costs

Use `expire_in` to automatically clean up old artifacts:

```yaml
test_job:
  artifacts:
    paths:
      - test-results/
    expire_in: 3 days
    when: on_failure  # Only save on failure for debugging
```

Use `when: always` to save even on success, or `when: on_failure` to save only for debugging.


## Common Scenarios

- **Artifact download fails with 404 error:** Ensure the producing job ran successfully and the artifact paths are correct. Check job logs for upload errors.
- **Artifacts are too large to upload within timeout:** Split artifacts into smaller chunks, increase timeout, or use external storage like S3.

## Prevent It

- Use glob patterns in artifact paths to include only necessary files
- Set `expire_in` to manage artifact storage costs automatically
- Use `when: on_failure` to save artifacts only when debugging is needed
