---
title: "[Solution] GitLab CI Terraform State Lock"
description: "Fix GitLab CI Terraform state lock errors when concurrent pipelines lock the Terraform state file and block other runs."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Terraform State Lock

Terraform state lock errors occur when a pipeline acquires a lock on the remote state file and a concurrent pipeline cannot proceed.

## Common Causes

- Two pipelines run `terraform apply` simultaneously for the same environment
- Previous pipeline crashed without releasing the state lock
- Remote state backend has strict locking (S3 with DynamoDB)
- State lock timeout exceeded

## How to Fix

### Solution 1: Use resource groups to serialize deployments

```yaml
terraform_apply:
  stage: deploy
  resource_group: terraform-$CI_ENVIRONMENT_NAME
  script:
    - terraform apply -auto-approve
```

### Solution 2: Force-unlock a stuck state

```bash
# Get the lock ID
terraform state list

# Force unlock
terraform force-unlock LOCK_ID
```

### Solution 3: Use retry with backoff

```yaml
terraform_apply:
  stage: deploy
  retry:
    max: 2
    when:
      - runner_system_failure
      - stuck_or_timeout_failure
  script:
    - terraform init
    - terraform apply -auto-approve
```

## Examples

```
Error: Error acquiring the state lock
Error: state file is locked by another operation
```

## Prevent It

- Always use `resource_group` for Terraform jobs
- Set appropriate lock timeout values
- Monitor for abandoned locks after pipeline failures
