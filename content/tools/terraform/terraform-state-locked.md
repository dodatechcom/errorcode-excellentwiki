---
title: "[Solution] Terraform State Lock Error — Fix and Prevent"
description: "Fix Terraform state lock errors fast. Learn to safely unlock state, prevent conflicts, and configure locking for team workflows."
---

## What This Error Means

The `Error acquiring the state lock` message appears when Terraform cannot acquire a lock on the state file. Terraform uses state locking to prevent concurrent modifications that could corrupt infrastructure state. When another process or teammate already holds the lock, your operation is blocked.

A typical error output looks like:

```
Error: Error acquiring the state lock

Error message: ConditionalCheckFailedException: The conditional request failed
Lock Info:
  ID:        a1b2c3d4-e5f6-7890-abcd-ef1234567890
  Path:      my-bucket/terraform.tfstate
  Operation: OperationTypeApply
  Who:       user@machine
  Version:   1.5.7
  Created:   2024-01-15 10:30:00.123456 +0000 UTC
```

## Why It Happens

State lock errors occur in several scenarios:

- **Concurrent operations**: Two team members running `terraform apply` simultaneously on the same environment.
- **Crashed previous run**: A prior Terraform process was killed or crashed without releasing the lock.
- **CI/CD pipeline conflicts**: Multiple pipeline jobs targeting the same state file.
- **Network issues**: Temporary connectivity problems to the backend (S3, GCS, Consul) caused the lock not to release properly.
- **Slow state operations**: Large state files taking too long to read/write, causing lock timeouts.

## How to Fix It

**Step 1: Verify the lock holder is no longer running**

Check if the person or process listed in the lock info is still active:

```bash
# If using remote backend, check via CLI
terraform force-unlock <LOCK_ID>
```

**Step 2: Force unlock the state**

Only force unlock after confirming no other process is actively modifying state:

```bash
terraform force-unlock a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

For S3 backends with DynamoDB locking, you can also delete the lock entry directly:

```bash
aws dynamodb delete-item \
  --table-name terraform-locks \
  --key '{"LockID":{"S":"my-bucket/terraform.tfstate"}}'
```

**Step 3: Retry your operation**

After unlocking, retry the failed command:

```bash
terraform plan
terraform apply
```

**Step 4: Implement proper locking configuration**

Ensure your backend has locking enabled:

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

## Common Mistakes

- **Force unlocking during an active apply**: This can corrupt state. Always verify the lock holder first.
- **Not using DynamoDB locking with S3**: S3 alone does not provide true state locking. Always pair S3 with DynamoDB.
- **Running Terraform locally instead of CI/CD**: Local runs increase the chance of lock conflicts. Centralize Terraform in pipelines.
- **Ignoring lock timeout settings**: Increase the lock timeout for large states by using `-lock-timeout=300s`.

## Related Pages

- [Terraform Backend Error](/tools/terraform/terraform-backend-error/) — Backend configuration failures
- [Terraform Plan Changed](/tools/terraform/terraform-plan-changed/) — Plan drift detection
- [Kubectl Connection Refused](/tools/kubectl/kubectl-connection-refused/) — API server connection issues
