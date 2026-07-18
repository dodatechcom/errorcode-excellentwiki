---
title: "[Solution] Terraform State Refresh Failed Error — How to Fix"
description: "Fix Terraform state refresh failures including stale state, API errors, and resource drift issues with reliable troubleshooting steps."
comments: true
---

A Terraform state refresh failed error occurs when Terraform cannot reconcile the real-world state of infrastructure with the state file during `plan` or `apply`. Terraform reads the current state of each managed resource to detect drift, and failures during this process block planning operations.

## Why It Happens

State refresh is a critical step where Terraform queries the cloud provider API to verify that each resource still exists and matches the state file. Failures arise from:

- **Resource deleted outside Terraform**: A resource managed in state was manually deleted via the console, CLI, or another tool. The API returns a 404 and Terraform cannot refresh its state.
- **API rate limiting**: During large state refreshes (hundreds of resources), the cloud provider API throttles requests, causing transient failures.
- **Provider version incompatibility**: After a provider upgrade, the refresh logic changed and the state file contains resource attributes the new provider cannot read.
- **Expired or invalid credentials**: The credentials used for state refresh have expired or lack permissions for the queried resource types.
- **Resource moved or renamed**: The resource was renamed or moved outside Terraform, causing the API lookup to fail.
- **Network timeout**: The provider API is slow or unreachable during state refresh, causing timeouts.

## Common Error Messages

**Error: Resource not found during refresh**

```
Error: Reference to deleted resource

  on main.tf line 15, in resource "aws_instance" "web":
  15: resource "aws_instance" "web" {

The Terraform state currently describes a resource instance
that was deleted outside of Terraform. To correct this, run
"terraform refresh" to update the state to match the real
infrastructure.
```

**Error: API throttling during refresh**

```
Error: Error refreshing state

Throttling: Rate exceeded forDescribeInstances for account
123456789012 in region us-east-1

Please wait a few minutes before you try again.
```

**Error: State refresh failed for provider**

```
Error: Error: Refreshing state failed

Error: aws_instance.web: Error reading instance: InvalidInstanceID.NotFound:
The instance 'i-0123456789abcdef0' does not exist

Terraform tried to refresh the state for this resource but the
resource was not found at the provider API.
```

**Error: State lock conflict during refresh**

```
Error: State file is locked

The state file is locked by another process. This may indicate
another Terraform run is in progress. Wait for it to complete
or force-unlock the state file.

Lock info:
  ID:        abc123-def456-ghi789
  Path:      terraform.tfstate
  Operation: OperationTypeRefresh
```

## How to Fix It

### Solution 1: Use terraform refresh to sync state

Run `terraform refresh` to update the state file with current infrastructure reality:

```bash
# Refresh state to match current infrastructure
terraform refresh

# If using a specific state file
terraform refresh -state=terraform.tfstate

# For remote state
terraform refresh -refresh=true
```

After refreshing, verify the state:

```bash
# List all managed resources
terraform state list

# Check specific resource state
terraform state show aws_instance.web

# Compare state with configuration
terraform plan
```

### Solution 2: Handle resources deleted outside Terraform

When resources were deleted externally, remove them from state and re-import if needed:

```bash
# Remove the deleted resource from state
terraform state rm aws_instance.web

# If the resource still exists but needs re-importing
terraform import aws_instance.web i-0123456789abcdef0

# For multiple resources
terraform state rm aws_instance.web[0]
terraform state rm aws_instance.web[1]
```

For bulk cleanup of missing resources:

```bash
# Show all resources and filter for errors
terraform plan 2>&1 | grep "does not exist"

# Remove each one
terraform state rm <resource_address>
```

### Solution 3: Handle API throttling with backoff

For large state files with many resources, implement retry logic:

```bash
# Set provider retry configuration
export TF_S3_RETRY_MAX_ATTEMPTS=10
export TF_S3_RETRY_MIN_WAIT_TIME=5

# For AWS provider, set retry in configuration
cat > provider_config.tf << 'EOF'
provider "aws" {
  region = "us-east-1"

  default_tags {
    tags = {
      Environment = "prod"
    }
  }
}
EOF
```

For repeated throttling, use the `-refresh=false` flag temporarily:

```bash
# Skip refresh if you know state is accurate (use carefully)
terraform plan -refresh=false

# Then refresh specific resources
terraform plan -refresh=true -target=aws_instance.web
```

### Solution 4: Upgrade provider and migrate state

After a provider upgrade, migrate state format:

```bash
# Update provider version
terraform init -upgrade

# If state migration is needed
terraform init -migrate-state

# If state format is incompatible
terraform state pull > backup.tfstate
terraform state push backup.tfstate
```

Check provider changelog for breaking changes:

```bash
# View current provider version
terraform version

# View available versions
terraform providers
```

## Common Scenarios

**Scenario 1: Large state refresh times out**

A state file with 500+ resources takes 10+ minutes to refresh. The default timeout causes a refresh failure. Use `-refresh=false` for quick planning, then do a targeted refresh of critical resources.

**Scenario 2: Resource recreated after external deletion**

A developer deleted an EC2 instance via AWS console. Terraform state still references it. Running `terraform plan` shows the instance will be recreated. Either re-import the instance or remove it from state and let Terraform recreate it.

**Scenario 3: Provider upgrade changes state format**

After upgrading the AWS provider from v4 to v5, state attributes changed format. Running `terraform init -migrate-state` converts the state to the new format, but some custom attributes may be lost. Back up state before migrating.

## Prevent It

- **Avoid modifying resources outside Terraform**: Use Terraform exclusively for all infrastructure changes. If manual changes are necessary, import them back immediately.
- **Back up state before major operations**: Run `terraform state pull > backup.tfstate` before any refresh, migration, or provider upgrade.
- **Monitor state file size**: Large state files slow down refresh. Split configurations into smaller workspaces or use Terraform Cloud's state partitioning.

## Related Pages

- [Terraform State Locked](/tools/terraform/terraform-state-locked/) — State lock conflicts
- [Terraform Plan Error](/tools/terraform/terraform-plan-error/) — Planning failures
- [Terraform Import Error](/tools/terraform/terraform-import-error/) — Importing existing resources
