---
title: "[Solution] Terraform State File Locked Error — How to Fix"
description: "Fix Terraform state file locked errors including lock conflicts, stale locks, and multi-process contention with reliable unlock methods."
comments: true
---

A Terraform state file locked error occurs when another Terraform process holds a lock on the state file, preventing the current operation from proceeding. This is a protective mechanism to prevent concurrent modifications that could corrupt the state.

## Why It Happens

Terraform locks the state file during `plan` and `apply` operations to ensure only one process modifies state at a time. Lock errors happen because:

- **Concurrent Terraform runs**: Two team members or CI/CD pipelines run `apply` simultaneously on the same workspace and backend.
- **Crashed previous run**: A previous Terraform process crashed, was killed, or lost network connectivity without releasing the lock.
- **Orphaned lock**: The lock was created but the process that created it is no longer running, leaving a stale lock behind.
- **Backend-specific locking**: The backend (S3 with DynamoDB, Terraform Cloud, Consul) has its own locking mechanism that may behave differently.
- **Slow operations**: Long-running applies hold the lock for extended periods, causing other processes to timeout waiting.
- **Workspace mismatch**: Running Terraform in different workspaces that share the same state file.

## Common Error Messages

**Error: State file is locked**

```
Error: Error acquiring the state lock

Error message: ConditionalCheckFailedException: The conditional
request failed

Terraform acquires a state lock to protect the state from being
written by multiple users at the same time. Please resolve the
issue above and try again.

Lock Info:
  ID:        a1b2c3d4-e5f6-7890-abcd-ef1234567890
  Path:      s3://my-tf-state/terraform.tfstate
  Operation: OperationTypeApply
```

**Error: Lock timeout**

```
Error: Timeout acquiring the state lock

Another process holds a lock on the state file for more than the
configured timeout (10s). The lock was created by process ID
12345 at 2025-01-15 10:30:00 UTC.

Lock Info:
  ID:        a1b2c3d4-e5f6-7890-abcd-ef1234567890
  Operation: OperationTypePlan
```

**Error: DynamoDB lock check failed**

```
Error: Error acquiring the state lock

ValidationException: The provided key element does not match the
schema. Check your DynamoDB table configuration for the lock table.

The lock table "tf-lock-table" may be misconfigured or the
region may be incorrect.
```

**Error: Lock stale after migration**

```
Error: State locked by stale process

The lock was acquired by process abc123 which is no longer
running. The lock has been held for 2 hours without release.
Consider force-unlocking if the original process crashed.
```

## How to Fix It

### Solution 1: Force-unlock the state

When the lock holder is no longer running, force-unlock:

```bash
# Force unlock with the lock ID from the error message
terraform force-unlock a1b2c3d4-e5f6-7890-abcd-ef1234567890

# If you do not have the lock ID, use -force flag
terraform force-unlock -force
```

Verify the lock is released:

```bash
# Check DynamoDB lock table (for S3 backend)
aws dynamodb get-item \
  --table-name tf-lock-table \
  --key '{"LockID": {"S": "s3://my-tf-state/terraform.tfstate"}}' \
  --region us-east-1

# Delete stale lock entry if needed
aws dynamodb delete-item \
  --table-name tf-lock-table \
  --key '{"LockID": {"S": "s3://my-tf-state/terraform.tfstate"}}' \
  --region us-east-1
```

### Solution 2: Prevent concurrent runs

Ensure only one Terraform process runs at a time on the same state:

```bash
# Use a lock file wrapper script
#!/bin/bash
LOCKFILE="/tmp/tf-apply.lock"

if [ -e ${LOCKFILE} ] && kill -0 $(cat ${LOCKFILE}); then
    echo "Terraform is already running (PID: $(cat ${LOCKFILE}))"
    exit 1
fi

trap "rm -f ${LOCKFILE}; exit" INT TERM EXIT
echo $$ > ${LOCKFILE}

terraform apply -auto-approve
```

For CI/CD pipelines, use a queue mechanism:

```yaml
# GitHub Actions example with concurrency groups
name: Terraform Apply
on:
  push:
    branches: [main]

concurrency:
  group: terraform-apply
  cancel-in-progress: false
```

### Solution 3: Configure lock timeout

Increase the lock timeout for environments with long-running operations:

```hcl
terraform {
  backend "s3" {
    bucket         = "my-tf-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tf-lock-table"
    encrypt        = true
  }
}
```

Set the lock timeout via CLI:

```bash
# Increase lock timeout to 30 seconds
terraform plan -lock-timeout=30s

terraform apply -lock-timeout=60s
```

### Solution 4: Verify DynamoDB lock table configuration

Ensure the DynamoDB table exists and has the correct schema:

```bash
# Check table exists
aws dynamodb describe-table \
  --table-name tf-lock-table \
  --region us-east-1

# Verify table has correct key schema
aws dynamodb describe-table \
  --table-name tf-lock-table \
  --query 'Table.KeySchema'
```

Create the lock table if missing:

```bash
aws dynamodb create-table \
  --table-name tf-lock-table \
  --attribute-definitions \
    AttributeName=LockID,AttributeType=S \
  --key-schema \
    AttributeName=LockID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST \
  --region us-east-1
```

Or use Terraform to manage the lock table:

```hcl
resource "aws_dynamodb_table" "terraform_lock" {
  name         = "tf-lock-table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

## Common Scenarios

**Scenario 1: Developer crashed during apply**

A developer ran `terraform apply` and their terminal disconnected. The lock persists in DynamoDB. The team cannot run any Terraform operations. Force-unlock with the lock ID from the error message, then verify the state file was not corrupted.

**Scenario 2: CI/CD pipeline and manual run conflict**

A pipeline starts `terraform plan` while a developer runs `terraform apply` manually. Both hit the lock. The pipeline should wait using retry logic, and the developer should complete first. Use concurrency groups in CI/CD to prevent this.

**Scenario 3: State lock after workspace migration**

After migrating state from one backend to another, the old backend still holds a lock. Clean up the old backend's lock entries before switching to the new one.

## Prevent It

- **Use CI/CD with concurrency controls**: Serialize Terraform runs in pipelines using concurrency groups or job queues.
- **Set `-lock-timeout` for all operations**: Prevent false lock failures by setting a reasonable timeout (30-60 seconds).
- **Monitor DynamoDB lock table**: Set up CloudWatch alarms for stale locks held longer than expected periods.

## Related Pages

- [Terraform Backend Error](/tools/terraform/terraform-backend-error/) — Backend connectivity issues
- [Terraform State Migration](/tools/terraform/terraform-state-mv/) — Moving state between backends
- [Terraform Workspace Error](/tools/terraform/terraform-workspace-error/) — Workspace selection issues
