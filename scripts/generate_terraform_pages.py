#!/usr/bin/env python3
"""Generate Terraform error pages"""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/terraform'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(title, desc, body):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["terraform"]',
        'error-types: ["tool-error"]',
        'severities: ["error"]',
        '---',
        '',
        body,
    ]
    return '\n'.join(lines)

def md(title, desc, body):
    return (title, desc, body)

PAGES = [
    # =========================================================================
    # 1. INIT/PROVIDER ERRORS
    # =========================================================================
    md("Terraform Provider Not Found", "Fix Terraform provider not found errors when the provider cannot be located.",
       """## Error Description

The `provider not found` error occurs when Terraform cannot locate the requested provider plugin during `terraform init`.

```
Error: Failed to install provider

Error: Failed to install hashicorp/aws: could not find package
for registry.terraform.io/hashicorp/aws 4.67.0
```

## Common Causes

- The provider name is misspelled in the `required_providers` block.
- The provider source address is incorrect (e.g., missing namespace).
- The requested version does not exist in the registry.
- Network connectivity issues prevent downloading.

## How to Fix

**Verify the provider source address:**

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

**Force re-download:**

```bash
terraform init -upgrade
```

## Examples

```hcl
# Wrong — missing namespace
terraform {
  required_providers {
    aws = {
      source  = "aws"
      version = "~> 5.0"
    }
  }
}

# Correct
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```
"""),

    md("Terraform Provider Registry Unavailable", "Fix Terraform provider registry unavailable errors when the registry cannot be reached.",
       """## Error Description

The provider registry unavailable error means Terraform cannot communicate with `registry.terraform.io`:

```
Error: Failed to query available provider packages

Could not retrieve the list of available versions for provider
"hashicorp/aws": could not connect to registry.terraform.io
```

## Common Causes

- Network firewall blocks outbound HTTPS to `registry.terraform.io`.
- Corporate proxy is not configured for Terraform.
- The registry is experiencing downtime.
- DNS resolution failure.

## How to Fix

**Configure proxy settings:**

```bash
export HTTPS_PROXY="http://proxy.example.com:8080"
terraform init
```

**Use a provider mirror:**

```hcl
# ~/.terraformrc
provider_installation {
  network_mirror {
    url     = "https://mirror.company.com/"
    include = ["registry.terraform.io/*/*"]
  }
  direct {
    exclude = ["registry.terraform.io/*/*"]
  }
}
```

## Examples

```bash
# Verify connectivity
curl -I https://registry.terraform.io/v1/providers/hashicorp/aws

# Use filesystem mirror
provider_installation {
  filesystem_mirror {
    path    = "/opt/terraform/mirror"
    include = ["registry.terraform.io/*/*"]
  }
}
```
"""),

    md("Terraform Provider Version Constraint Error", "Fix Terraform provider version constraint errors when no version satisfies all constraints.",
       """## Error Description

This error occurs when provider version constraints cannot all be satisfied:

```
Error: Failed to install provider

Constraint versions for hashicorp/aws cannot be satisfied:
  - required: >= 4.0, < 5.0
  - required by module.vpc: >= 5.0
```

## Common Causes

- Multiple modules specify conflicting version ranges for the same provider.
- Pinned version no longer available on the registry.
- Version constraint syntax errors.

## How to Fix

**Align version constraints across modules:**

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0, < 6.0"
    }
  }
}
```

**Override module constraints in root:**

```bash
terraform init -upgrade
```

## Examples

```hcl
# Module A: version = ">= 4.0, < 5.0"
# Module B: version = ">= 5.0"
# Fix: update both to version = ">= 4.0, < 6.0"
```
"""),

    md("Terraform Provider Lock File Error", "Fix Terraform provider lock file errors that prevent deterministic provider installation.",
       """## Error Description

Provider lock errors occur when `.terraform.lock.hcl` is out of sync:

```
Error: Missing dependency lock entry

The dependency lock file .terraform.lock.hcl does not include an
entry for provider "registry.terraform.io/hashicorp/azurerm".
```

## Common Causes

- New provider added without running `terraform init`.
- Lock file was deleted or modified manually.
- Platform or OS changed.

## How to Fix

**Reinitialize to update the lock file:**

```bash
terraform init -upgrade
```

**Commit lock file to version control:**

```bash
git add .terraform.lock.hcl
```

**Target a specific platform:**

```bash
terraform init -platform=linux_amd64
```

## Examples

```bash
rm .terraform.lock.hcl
terraform init
```
"""),

    md("Terraform Provider Initialization Failed", "Fix Terraform provider initialization failed errors during terraform init.",
       """## Error Description

Provider initialization fails when Terraform downloads the provider but cannot set it up:

```
Error: Failed to install provider

Error: failed to verify package signature for
"registry.terraform.io/hashicorp/aws": openpgp: signature verification failed
```

## Common Causes

- Corrupted provider download cache.
- Checksum verification failure.
- Insufficient disk space in the plugin directory.
- Antivirus software quarantining the binary.

## How to Fix

**Clear the provider cache and reinitialize:**

```bash
rm -rf .terraform/
terraform init
```

**Force re-download:**

```bash
terraform init -upgrade -force-copy
```

**Check disk space:**

```bash
df -h ~/.terraform.d/plugin-cache
```

## Examples

```bash
rm -rf .terraform .terraform.lock.hcl
terraform init -upgrade
terraform providers
```
"""),

    md("Terraform Backend Init Failed", "Fix Terraform backend initialization failures when configuring remote state backends.",
       """## Error Description

Backend init errors occur when Terraform cannot initialize the configured backend:

```
Error: Failed to get existing workspaces: S3 bucket does not exist.

The referenced bucket does not exist or you lack permission to access it.
```

## Common Causes

- Remote backend resource does not exist yet (chicken-and-egg problem).
- IAM permissions insufficient for the backend storage.
- Backend configuration has incorrect values.

## How to Fix

**Use the local backend for initial setup:**

```hcl
terraform {
  backend "local" {}
}
```

**Migrate to remote backend after initial apply:**

```bash
terraform init -migrate-state
```

**Create prerequisite resources first:**

```hcl
resource "aws_s3_bucket" "terraform_state" {
  bucket = "my-terraform-state"
}

resource "aws_dynamodb_table" "terraform_lock" {
  name         = "terraform-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

## Examples

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}
```
"""),

    md("Terraform Module Download Failed", "Fix Terraform module download failed errors when fetching modules from registries or Git.",
       """## Error Description

Module download failures prevent Terraform from retrieving required modules:

```
Error: Failed to download module

Error: could not download "git::https://github.com/org/module.git?ref=v1.0"
```

## Common Causes

- Invalid module source URL or Git reference.
- Repository is private without proper authentication.
- Network restrictions blocking Git access.

## How to Fix

**Verify the module source:**

```hcl
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = "~> 3.0"
}
```

**Configure Git credentials:**

```bash
export GIT_CREDENTIAL.helper=store
git config --global url."git@github.com:".insteadOf "https://github.com/"
```

**Check the Git ref:**

```bash
git ls-remote https://github.com/org/module.git refs/tags/v1.0
```

## Examples

```hcl
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = "3.2.1"
}
```
"""),

    md("Terraform Version Mismatch", "Fix Terraform version mismatch errors when your CLI version is incompatible with the configuration.",
       """## Error Description

Version mismatch errors occur when your Terraform CLI version is incompatible:

```
Error: Terraform CLI version 1.3.0 is incompatible with state
format version 4 (written by Terraform 1.5.0).
Please upgrade Terraform to at least version 1.5.0.
```

## Common Causes

- State file was created with a newer Terraform version.
- Configuration uses features from a newer version.
- CI/CD pipeline uses a different version.

## How to Fix

**Upgrade Terraform:**

```bash
# Using tfenv
tfenv install latest
tfenv use latest
terraform version
```

**Pin version in CI/CD:**

```yaml
- uses: hashicorp/setup-terraform@v3
  with:
    terraform_version: "1.7.0"
```

**Check required version:**

```hcl
terraform {
  required_version = ">= 1.5.0"
}
```

## Examples

```hcl
terraform {
  required_version = ">= 1.5.0, < 2.0.0"
}
```
"""),

    md("Terraform Plugin Cache Error", "Fix Terraform plugin cache errors when the local provider cache is corrupted or inaccessible.",
       """## Error Description

Plugin cache errors occur when Terraform cannot read or write its plugin cache:

```
Error: Failed to install provider

Error: open /home/user/.terraform.d/plugin-cache/.../linux_amd64:
permission denied
```

## Common Causes

- Permission issues on the cache directory.
- Corrupted cache entries from interrupted downloads.
- Multiple Terraform processes writing to cache simultaneously.

## How to Fix

**Fix permissions:**

```bash
chmod -R u+rw ~/.terraform.d/plugin-cache
```

**Clear and rebuild the cache:**

```bash
rm -rf ~/.terraform.d/plugin-cache
terraform init
```

**Set custom cache directory:**

```bash
export TF_PLUGIN_CACHE_DIR="/opt/terraform/cache"
terraform init
```

## Examples

```bash
ls -la ~/.terraform.d/plugin-cache/
export TF_PLUGIN_CACHE_DIR=""
terraform init
```
"""),

    md("Terraform Provider Checksum Mismatch", "Fix Terraform provider checksum mismatch errors when downloaded provider binary fails verification.",
       """## Error Description

Checksum mismatch errors indicate the downloaded binary does not match expected:

```
Error: Failed to install provider

Error: checksum for registry.terraform.io/hashicorp/aws/5.31.0/linux_amd64
did not match expected value
```

## Common Causes

- Incomplete or corrupted download.
- MITM proxy altering the downloaded binary.
- Network interruption during download.

## How to Fix

**Clear cache and re-download:**

```bash
rm -rf ~/.terraform.d/plugin-cache/registry.terraform.io/hashicorp/
terraform init -upgrade
```

**Check proxy/SSL:**

```bash
unset HTTPS_PROXY
terraform init
```

**Lock provider checksums:**

```bash
terraform providers lock -platform=linux_amd64 -platform=darwin_amd64
```

## Examples

```bash
rm -rf .terraform/
terraform init -upgrade
```
"""),

    md("Terraform Failed To Query Provider Registry", "Fix Terraform errors querying the provider registry for available versions.",
       """## Error Description

This error occurs when Terraform cannot query the provider registry API:

```
Error: Failed to query available provider packages

Could not retrieve the list of available versions for provider
"hashicorp/azurerm": rpc error: code = Unavailable
```

## Common Causes

- Registry API rate limiting.
- Network connectivity issues.
- Registry service degradation.

## How to Fix

**Wait and retry:**

```bash
sleep 30 && terraform init
```

**Use a registry mirror:**

```hcl
# ~/.terraformrc
provider_installation {
  network_mirror {
    url     = "https://mirror.company.com/"
    include = ["registry.terraform.io/*/*"]
  }
}
```

**Test registry API directly:**

```bash
curl "https://registry.terraform.io/v1/providers/hashicorp/aws/versions"
```

## Examples

```bash
terraform providers mirror ./local-mirror
```
"""),

    md("Terraform Unsupported Provider Protocol", "Fix Terraform unsupported provider protocol errors when provider uses incompatible gRPC protocol.",
       """## Error Description

Protocol version mismatch errors occur when the provider uses an unsupported gRPC protocol:

```
Error: Incompatible provider version

Provider "hashicorp/aws" uses protocol version 6, but this
version of Terraform only supports protocol version 5.
```

## Common Causes

- Terraform CLI is too old for the provider version.
- Mixed versions in CI/CD and local environments.

## How to Fix

**Upgrade Terraform CLI:**

```bash
tfenv install 1.7.0
tfenv use 1.7.0
```

**Pin provider to compatible version:**

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0, < 5.0"
    }
  }
}
```

## Examples

```bash
terraform version
tfenv install latest && tfenv use latest
```
"""),

    # =========================================================================
    # 2. PLAN ERRORS
    # =========================================================================
    md("Terraform Plan Output Changed", "Fix Terraform plan output changed errors when the plan differs from a previous preview.",
       """## Error Description

The plan output changed error occurs when a saved plan no longer matches:

```
Error: Plan output has changed since it was saved.
```

## Common Causes

- External changes to infrastructure outside Terraform.
- Configuration files modified between plan and apply.
- Data sources returning different values.

## How to Fix

**Re-run the plan:**

```bash
terraform plan -out=tfplan
```

**Use refresh-only mode:**

```bash
terraform plan -refresh-only
```

**Prevent external changes:**

```hcl
resource "aws_instance" "web" {
  lifecycle {
    prevent_destroy = true
  }
}
```

## Examples

```bash
terraform plan -out=tfplan && terraform apply tfplan
terraform plan -detailed-exitcode
```
"""),

    md("Terraform Resource Count Mismatch", "Fix Terraform resource count mismatch errors when planned and actual resource counts diverge.",
       """## Error Description

Resource count mismatch occurs when expected count doesn't match reality:

```
Error: Resource count mismatch

Plan to create 3 resources, but 2 exist in state.
```

## Common Causes

- Resources imported or deleted outside Terraform.
- `count` or `for_each` expressions changed.
- State file manually edited.

## How to Fix

**Refresh state:**

```bash
terraform plan -refresh-only
```

**Import orphaned resources:**

```bash
terraform import aws_instance.web i-0123456789abcdef0
```

**Use `moved` blocks for renames:**

```hcl
moved {
  from = aws_instance.old_name
  to   = aws_instance.new_name
}
```

## Examples

```hcl
resource "aws_instance" "web" {
  count = var.instance_count
}
```
"""),

    md("Terraform Attribute Is Empty", "Fix Terraform attribute is empty errors when referencing empty or null resource attributes.",
       """## Error Description

This error occurs when referencing an attribute that has no value:

```
Error: Attribute must not be empty

The attribute "arn" is empty, but was referenced by
resource "aws_instance" "example".
```

## Common Causes

- Referencing a computed attribute before resource is created.
- Data source returning empty or null values.
- Missing required argument.

## How to Fix

**Use `try()` or null checks:**

```hcl
locals {
  instance_arn = try(aws_instance.example.arn, "")
}
```

**Use conditional expressions:**

```hcl
output "instance_arn" {
  value = aws_instance.example.arn != null ? aws_instance.example.arn : "pending"
}
```

## Examples

```hcl
locals {
  safe_arn = try(aws_instance.example.arn, "unknown")
}
```
"""),

    md("Terraform Invalid for_each", "Fix Terraform invalid for_each errors when the for_each argument is not a valid map or set.",
       """## Error Description

Invalid for_each occurs when the expression doesn't produce a valid map or set:

```
Error: Invalid for_each argument

for_each can only be used with a map or set of strings, or a
list of strings. You provided a value of type string.
```

## Common Causes

- Passing a string instead of a map/list.
- Data source returns a list of objects (not strings).
- Variable is null or empty.

## How to Fix

**Convert to a map with stable keys:**

```hcl
resource "aws_instance" "example" {
  for_each = { for inst in var.instances : inst.name => inst }
  ami           = each.value.ami
  instance_type = each.value.type
}
```

**Ensure correct type:**

```hcl
variable "instances" {
  type = map(object({
    ami  = string
    type = string
  }))
}
```

## Examples

```hcl
resource "aws_instance" "good" {
  for_each = {
    web    = "t3.micro"
    api    = "t3.small"
    worker = "t3.medium"
  }
  instance_type = each.value
}
```
"""),

    md("Terraform Invalid Count Argument", "Fix Terraform invalid count argument errors when count is not a non-negative integer.",
       """## Error Description

Invalid count errors occur when the `count` expression is not valid:

```
Error: Invalid count argument

The "count" argument can only be used with a non-negative integer
value. You provided a value of type string.
```

## Common Causes

- `count` expression returns a non-integer value.
- `count` references an undefined variable.
- `count` expression returns null.

## How to Fix

**Use `length()` for collections:**

```hcl
resource "aws_instance" "web" {
  count         = length(var.instance_names)
  ami           = var.ami_id
  instance_type = "t3.micro"
}
```

**Use conditional:**

```hcl
resource "aws_instance" "web" {
  count = var.create_instance ? 1 : 0
}
```

## Examples

```hcl
variable "create" {
  type    = bool
  default = true
}

resource "aws_s3_bucket" "example" {
  count  = var.create ? 1 : 0
  bucket = "my-bucket"
}
```
"""),

    md("Terraform Depends_on Cycle", "Fix Terraform depends_on cycle errors when circular dependencies are detected.",
       """## Error Description

Dependency cycle errors occur when resources form a circular dependency:

```
Error: Cycle: aws_instance.web, aws_security_group.web, aws_instance.api
```

## Common Causes

- Resource A depends on B, and B depends on A.
- Implicit dependency through attribute references creates a loop.

## How to Fix

**Refactor to break the cycle:**

```hcl
resource "aws_security_group" "shared" {
  name = "shared-sg"
}

resource "aws_instance" "web" {
  vpc_security_group_ids = [aws_security_group.shared.id]
}

resource "aws_instance" "api" {
  vpc_security_group_ids = [aws_security_group.shared.id]
}
```

**Analyze the dependency graph:**

```bash
terraform graph | dot -Tpng > graph.png
```

## Examples

```bash
terraform graph > graph.dot
dot -Tpng graph.dot > graph.png
```
"""),

    md("Terraform Resource Address Parse Error", "Fix Terraform resource address parse errors when referencing resources with invalid syntax.",
       """## Error Description

Resource address parse errors occur when an address string is not valid:

```
Error: Invalid resource address

"aws_instance.web[0" is not a valid resource address syntax.
```

## Common Causes

- Typo in resource reference.
- Invalid characters in resource names.
- Incorrect index syntax.

## How to Fix

**Verify address syntax:**

```hcl
# Correct formats
aws_instance.web           # single resource
aws_instance.web[0]        # indexed resource
module.vpc.aws_instance.web  # module-scoped
```

## Examples

```hcl
aws_instance.web[count.index]
aws_instance.web["primary"]
```
"""),

    md("Terraform Missing Resource Key", "Fix Terraform missing resource key errors when accessing a non-existent map key on a resource.",
       """## Error Description

Missing resource key errors happen when accessing a map attribute that doesn't exist:

```
Error: Invalid index

This value does not have any attributes; you cannot index into
it using key "tags" on aws_instance.example.
```

## Common Causes

- Resource doesn't have the referenced attribute.
- Typo in attribute name.
- Accessing optional nested block that wasn't configured.

## How to Fix

**Use `try()` for safe access:**

```hcl
locals {
  name = try(aws_instance.example.tags.Name, "unnamed")
}
```

**Use `lookup()` with defaults:**

```hcl
locals {
  name = lookup(aws_instance.example.tags, "Name", "unnamed")
}
```

## Examples

```hcl
locals {
  environment = try(aws_instance.example.tags.Environment, "unknown")
}
```
"""),

    md("Terraform Data Source Not Available", "Fix Terraform data source not available errors when a data source cannot find matching resources.",
       """## Error Description

Data source not available errors occur when a data source query returns no results:

```
Error: DataSource "aws_ami" not found

No AMI matching filters was found in the specified region.
```

## Common Causes

- Resource doesn't exist in the target region/account.
- Filter criteria are too restrictive.
- Wrong region or account configured.

## How to Fix

**Use `try()` for optional data sources:**

```hcl
locals {
  ami_id = try(data.aws_ami.selected.id, null)
}
```

**Relax filter criteria:**

```hcl
data "aws_ami" "latest" {
  most_recent = true
  owners      = ["self"]

  filter {
    name   = "name"
    values = ["my-ami-*"]
  }
}
```

## Examples

```hcl
data "aws_caller_identity" "current" {}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}
```
"""),

    md("Terraform Plan Does Not Match", "Fix Terraform plan does not match errors when actual resource state differs from the plan.",
       """## Error Description

Plan mismatch errors occur during apply when reality differs from the plan:

```
Error: Provider produced inconsistent result after apply

When applying changes to aws_instance.example, provider
produced an unexpected new value: attribute "ami" changed.
```

## Common Causes

- Another process modified the resource between plan and apply.
- Cloud provider auto-modified attributes.

## How to Fix

**Retry the apply:**

```bash
terraform apply
```

**Use `-refresh-only`:**

```bash
terraform plan -refresh-only
```

**Add lifecycle ignore:**

```hcl
resource "aws_instance" "example" {
  ami = var.ami_id

  lifecycle {
    ignore_changes = [tags]
  }
}
```

## Examples

```hcl
lifecycle {
  ignore_changes = [tags, user_data]
}
```
"""),

    md("Terraform Planned Changes Conflict", "Fix Terraform planned changes conflict errors when multiple changes target the same resource.",
       """## Error Description

Planned changes conflict occurs when Terraform has contradictory operations:

```
Error: Planned changes conflict

Resource aws_instance.example is planned to be both created
and destroyed in the same plan.
```

## Common Causes

- `count` expression changes between plan iterations.
- Resource naming changed in configuration.

## How to Fix

**Use moved blocks:**

```hcl
moved {
  from = aws_instance.old
  to   = aws_instance.new
}
```

**Separate operations:**

```bash
terraform apply -destroy -target=aws_instance.old
terraform apply
```

## Examples

```bash
terraform plan 2>&1 | grep "will be"
```
"""),

    md("Terraform Sensitive Value In Plan", "Fix Terraform sensitive value in plan errors when sensitive attributes appear in plan output.",
       """## Error Description

Sensitive value warnings occur when sensitive data appears in plan output:

```
Warning: Value is sensitive

The value of output "db_password" is marked as sensitive.
```

## Common Causes

- Output marked as sensitive but referenced in plain text.
- Sensitive variable used in non-sensitive context.

## How to Fix

**Mark outputs as sensitive:**

```hcl
output "db_password" {
  value     = random_password.db.result
  sensitive = true
}
```

**Use `nonsensitive()` when needed:**

```hcl
output "db_endpoint" {
  value = nonsensitive(aws_db_instance.main.endpoint)
}
```

## Examples

```hcl
variable "api_key" {
  type      = string
  sensitive = true
}

output "connection_string" {
  value     = "postgres://user:${var.api_key}@host/db"
  sensitive = true
}
```
"""),
    # =========================================================================
    # 3. APPLY ERRORS
    # =========================================================================
    md("Terraform Resource Creation Failed", "Fix Terraform resource creation failed errors during terraform apply.",
       """## Error Description

Resource creation failed when Terraform cannot create a new resource:

```
Error: Error creating EC2 Instance: InvalidParameterValue

The value 't3.micro' for parameter instanceType is not valid.
```

## Common Causes

- Invalid parameter values.
- Insufficient permissions.
- Resource quotas exceeded.

## How to Fix

**Add retry logic with timeouts:**

```hcl
resource "aws_instance" "web" {
  instance_type = var.instance_type
  ami           = data.aws_ami.latest.id

  timeouts {
    create = "10m"
  }
}
```

## Examples

```hcl
data "aws_ami" "latest" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}
```
"""),

    md("Terraform Resource Update Failed", "Fix Terraform resource update failed errors when modifying an existing resource.",
       """## Error Description

Resource update failures occur when Terraform cannot modify a resource:

```
Error: Error updating Security Group (sg-12345): InvalidGroupPerm

The rule you specified already exists in this security group.
```

## Common Causes

- Resource in a state that prevents modification.
- API rejects the update due to constraints.

## How to Fix

**Check current state:**

```bash
terraform state show aws_security_group.example
```

**Force replacement:**

```bash
terraform apply -replace=aws_security_group.example
```

## Examples

```hcl
resource "aws_security_group" "web" {
  name = "web-sg"

  lifecycle {
    create_before_destroy = true
  }
}
```
"""),

    md("Terraform Resource Deletion Failed", "Fix Terraform resource deletion failed errors when Terraform cannot destroy a resource.",
       """## Error Description

Resource deletion failures occur during `terraform destroy`:

```
Error: Error deleting Security Group (sg-12345): DependencyViolation

Resource sg-12345 has a dependent object (eni-abc123)
```

## Common Causes

- Dependent resources not destroyed first.
- Resource has deletion protection enabled.

## How to Fix

**Destroy in correct order:**

```bash
terraform destroy -target=aws_instance.web
terraform destroy -target=aws_security_group.web
```

**Disable deletion protection:**

```hcl
resource "aws_db_instance" "main" {
  deletion_protection = false
}
```

## Examples

```bash
terraform graph | dot -Tpng > destroy-graph.png
terraform destroy -target=aws_network_interface.main
```
"""),

    md("Terraform Error Acquiring State Lock", "Fix Terraform error acquiring state lock when the state file is locked by another operation.",
       """## Error Description

State lock acquisition failures prevent Terraform from modifying state:

```
Error: Error acquiring the state lock

Error message: ConditionalCheckFailedException: The conditional
request failed Lock Info: ID: abc-123
```

## Common Causes

- Another Terraform process is running.
- Previous process crashed without releasing the lock.
- DynamoDB lock entry is stale.

## How to Fix

**Force-unlock:**

```bash
terraform force-unlock abc-123
```

**Manually delete the lock entry:**

```bash
aws dynamodb delete-item \
  --table-name terraform-lock \
  --key '{"LockID": {"S": "my-bucket/terraform.tfstate"}}'
```

## Examples

```bash
aws dynamodb scan --table-name terraform-lock
terraform force-unlock <LOCK_ID>
```
"""),

    md("Terraform State Lock Info Timeout", "Fix Terraform state lock info timeout errors when the lock service is unreachable.",
       """## Error Description

Lock info timeout errors occur when Terraform cannot retrieve lock info:

```
Error: Error acquiring the state lock

timeout while waiting for state lock to become 'not held'
```

## Common Causes

- Backend service (DynamoDB, GCS) is unreachable.
- Network latency or timeout.

## How to Fix

**Check backend connectivity:**

```bash
aws dynamodb describe-table --table-name terraform-lock
```

**Force-unlock:**

```bash
terraform force-unlock <LOCK_ID>
```

**Increase timeout:**

```bash
terraform plan -lock-timeout=300s
```

## Examples

```bash
aws dynamodb scan --table-name terraform-lock --limit 5
```
"""),

    md("Terraform State Backup Failed", "Fix Terraform state backup failed errors when creating state backup before modification.",
       """## Error Description

State backup failures occur when Terraform cannot create a backup:

```
Error: Failed to backup state

Error: AccessDeniedException: User is not authorized to perform:
s3:PutObject
```

## Common Causes

- S3 bucket permissions don't allow writes.
- Bucket policy blocks the backup path.

## How to Fix

**Grant write permissions:**

```json
{
  "Effect": "Allow",
  "Action": ["s3:PutObject", "s3:GetObject"],
  "Resource": "arn:aws:s3:::my-bucket/terraform.tfstate*"
}
```

**Configure backup path:**

```hcl
terraform {
  backend "s3" {
    bucket     = "my-bucket"
    key        = "prod/terraform.tfstate"
    backup_key = "backup/prod/terraform.tfstate"
  }
}
```

## Examples

```bash
terraform state pull > terraform.tfstate.backup
```
"""),

    md("Terraform Permission Denied Writing State", "Fix Terraform permission denied errors when writing to the state backend.",
       """## Error Description

Permission denied writing state errors prevent Terraform from saving state:

```
Error: Error writing state

AccessDenied: Access Denied
status code: 403
```

## Common Causes

- IAM role/user lacks `s3:PutObject` permission.
- S3 bucket policy restricts writes.

## How to Fix

**Check current identity:**

```bash
aws sts get-caller-identity
```

**Grant required permissions:**

```hcl
data "aws_iam_policy_document" "terraform_state" {
  statement {
    actions = [
      "s3:PutObject",
      "s3:GetObject",
      "s3:DeleteObject",
    ]
    resources = ["arn:aws:s3:::my-bucket/terraform/*"]
  }

  statement {
    actions   = ["s3:ListBucket"]
    resources = ["arn:aws:s3:::my-bucket"]
  }
}
```

## Examples

```hcl
resource "aws_s3_bucket_policy" "terraform" {
  bucket = aws_s3_bucket.terraform.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { AWS = "arn:aws:iam::123456789012:role/terraform" }
      Action    = ["s3:PutObject", "s3:GetObject"]
      Resource  = "arn:aws:s3:::my-bucket/terraform/*"
    }]
  })
}
```
"""),

    md("Terraform State Serial Mismatch", "Fix Terraform state serial mismatch errors when concurrent state modifications are detected.",
       """## Error Description

State serial mismatch errors occur when state has been modified since last read:

```
Error: State serial mismatch

The state has serial 45, but the last known serial is 44.
```

## Common Causes

- Multiple Terraform runs modifying the same state.
- State was manually edited.
- CI/CD and local CLI running simultaneously.

## How to Fix

**Refresh and re-run:**

```bash
terraform plan -refresh-only
terraform apply
```

**Use workspaces:**

```bash
terraform workspace new feature-x
terraform apply
```

## Examples

```bash
terraform state pull | jq '.serial'
```
"""),

    md("Terraform Operation Not Supported", "Fix Terraform operation not supported errors when the backend doesn't support the requested operation.",
       """## Error Description

Operation not supported errors occur when the backend cannot perform the action:

```
Error: Operation not supported

The "remote" backend does not support "terraform state mv".
```

## Common Causes

- Using state commands with remote backend.
- Feature not supported by backend type.

## How to Fix

**Switch to local backend for state operations:**

```hcl
terraform {
  backend "local" {}
}
```

**Use `-migrate-state`:**

```bash
terraform init -migrate-state
```

## Examples

```bash
terraform init -migrate-state -backend-config="bucket=new-bucket"
```
"""),

    md("Terraform API Rate Limit Exceeded", "Fix Terraform API rate limit exceeded errors when cloud provider throttles requests.",
       """## Error Description

API rate limit errors occur when too many API calls are made:

```
Error: Error creating instance: Throttling

Request limit exceeded (429)
```

## Common Causes

- Bulk resource creation exceeding API limits.
- Multiple Terraform runs in parallel.

## How to Fix

**Add parallelism limits:**

```bash
terraform apply -parallelism=2
```

**Use `-target` to batch:**

```bash
terraform apply -target=module.vpc
terraform apply -target=module.compute
```

## Examples

```hcl
provider "aws" {
  region      = "us-east-1"
  max_retries = 5
}
```
"""),

    # =========================================================================
    # 4. STATE ERRORS
    # =========================================================================
    md("Terraform State File Corrupted", "Fix Terraform state file corrupted errors when the state file is unreadable or malformed.",
       """## Error Description

State corruption errors indicate the state file is damaged:

```
Error: Error reading state

Error: unexpected end of JSON input
```

## Common Causes

- Write interrupted by process crash.
- State file manually edited incorrectly.
- Concurrent writes corrupted the file.

## How to Fix

**Restore from S3 versioning:**

```bash
aws s3api list-object-versions --bucket my-bucket --prefix terraform.tfstate
aws s3api get-object --bucket my-bucket --key terraform.tfstate \
  --version-id abc123 terraform.tfstate.restored
```

**Pull and fix state:**

```bash
terraform state pull > current-state.json
# Edit carefully
terraform state push current-state.json
```

## Examples

```bash
cat terraform.tfstate | python3 -m json.tool
```
"""),

    md("Terraform State Version Conflict", "Fix Terraform state version conflict errors when state format versions don't match.",
       """## Error Description

State version conflict errors occur when the state format is incompatible:

```
Error: Unsupported state version

State format version 4 cannot be read by Terraform 1.3.0.
```

## Common Causes

- State written by newer Terraform version.
- Mixed Terraform versions in team environments.

## How to Fix

**Upgrade Terraform CLI:**

```bash
tfenv install 1.7.0
tfenv use 1.7.0
```

**Standardize team version:**

```hcl
terraform {
  required_version = ">= 1.5.0"
}
```

## Examples

```bash
cat terraform.tfstate | jq '.version'
tfenv install latest
```
"""),

    md("Terraform State Not Found", "Fix Terraform state not found errors when the state file doesn't exist at the expected location.",
       """## Error Description

State not found errors occur when Terraform cannot locate the state file:

```
Error: Backend initialization required

Backend configuration has changed since the last initialization.
```

## Common Causes

- First-time initialization with remote backend.
- State key/path changed in backend configuration.

## How to Fix

**Verify backend configuration:**

```hcl
terraform {
  backend "s3" {
    bucket = "my-bucket"
    key    = "prod/terraform.tfstate"
    region = "us-east-1"
  }
}
```

**Check if state exists:**

```bash
aws s3 ls s3://my-bucket/terraform.tfstate
```

## Examples

```bash
aws s3 ls s3://my-bucket/ --recursive | grep terraform
terraform init
```
"""),

    md("Terraform State Locked By Another Operation", "Fix Terraform state locked errors when another Terraform process holds the lock.",
       """## Error Description

The state is locked by another process:

```
Error: Error acquiring the state lock

Error message: ConditionalCheckFailedException: Lock ID
"is already held by Terraform process (PID: 12345)
```

## Common Causes

- Another developer running Terraform simultaneously.
- CI/CD pipeline has a running job.
- Previous process crashed without releasing lock.

## How to Fix

**Check if the other process is running:**

```bash
ps aux | grep terraform
```

**Force-unlock if process is dead:**

```bash
terraform force-unlock <LOCK_ID>
```

## Examples

```bash
aws dynamodb scan --table-name terraform-lock
terraform force-unlock abc-123-def-456
```
"""),

    md("Terraform State Migration Failed", "Fix Terraform state migration failed errors when migrating state between backends.",
       """## Error Description

State migration errors occur when moving state from one backend to another:

```
Error: Error migrating state

Error: terraform state pull failed: AccessDenied
```

## Common Causes

- Insufficient permissions on new backend.
- New backend resource doesn't exist.

## How to Fix

**Migrate manually:**

```bash
terraform state pull > terraform.tfstate
terraform init -migrate-state
terraform state push terraform.tfstate
```

**Ensure both backends are accessible:**

```bash
terraform state pull > /dev/null
aws s3 ls s3://new-bucket/terraform.tfstate
```

## Examples

```bash
terraform state pull > state-backup.json
terraform init -migrate-state -backend-config="bucket=new-bucket"
terraform state push state-backup.json
```
"""),

    md("Terraform State Push Rejected", "Fix Terraform state push rejected errors when the state file is rejected by the backend.",
       """## Error Description

State push rejected errors occur when `terraform state push` fails:

```
Error: Error pushing state

Error: state serial 45 is not newer than current serial 45.
```

## Common Causes

- State serial not incremented.
- State is stale (behind current version).

## How to Fix

**Increment the state serial:**

```bash
terraform state pull > state.json
# Edit the "serial" field to be one higher
terraform state push state.json
```

**Use `-force` to overwrite (dangerous):**

```bash
terraform state push -force state.json
```

## Examples

```bash
terraform state pull | jq '.serial'
cat state.json | jq '.serial += 1' > state-new.json
terraform state push state-new.json
```
"""),

    md("Terraform State Pull Failed", "Fix Terraform state pull failed errors when downloading state from the backend.",
       """## Error Description

State pull failures occur when Terraform cannot retrieve the state:

```
Error: Failed to pull state

Error:NoSuchKey: The specified key does not exist.
```

## Common Causes

- State file doesn't exist (first run).
- Wrong S3 bucket or key configured.

## How to Fix

**Check state file existence:**

```bash
aws s3 ls s3://my-bucket/terraform.tfstate
```

**Initialize fresh state:**

```bash
terraform init -migrate-state
```

## Examples

```bash
aws s3 ls s3://my-bucket/ --recursive | grep tfstate
terraform state pull | jq '.resources | length'
```
"""),

    md("Terraform State Mv Resource Not Found", "Fix Terraform state mv resource not found errors when moving resources between addresses.",
       """## Error Description

State mv fails when the source resource is not in the state:

```
Error: Resource not found

A resource with the address "aws_instance.old" was not found.
```

## Common Causes

- Resource address typo.
- Resource was already moved.

## How to Fix

**List resources in state:**

```bash
terraform state list
```

**Move with correct address:**

```bash
terraform state mv aws_instance.old[0] aws_instance.new[0]
```

## Examples

```bash
terraform state list
terraform state mv 'module.vpc.aws_subnet.public[0]' 'aws_subnet.public'
```
"""),

    md("Terraform State Rm Resource Not Found", "Fix Terraform state rm resource not found errors when removing resources from state.",
       """## Error Description

State rm fails when the resource is not found in state:

```
Error: Resource not found

A resource with the address "aws_instance.removed" was not
found in the current state.
```

## Common Causes

- Resource address is incorrect.
- Resource already removed from state.

## How to Fix

**List current state:**

```bash
terraform state list
```

**Remove with correct address:**

```bash
terraform state rm aws_instance.web[0]
```

## Examples

```bash
terraform state list | grep web
terraform state rm 'module.vpc.aws_subnet.public[0]'
```
"""),

    md("Terraform State Show Parsing Error", "Fix Terraform state show parsing errors when displaying resource attributes from state.",
       """## Error Description

State show parsing errors occur when the output format cannot be parsed:

```
Error: Error reading state

Error: invalid resource address "aws_instance.web["
```

## Common Causes

- Malformed resource address.
- Special characters in resource names.

## How to Fix

**Use quotes for addresses:**

```bash
terraform state show 'aws_instance.web[0]'
```

**Use JSON output:**

```bash
terraform show -json | jq '.values.root_module.resources[]'
```

## Examples

```bash
terraform state show aws_instance.web
terraform show -json | jq '.values.root_module.resources[] | select(.type=="aws_instance")'
```
"""),

    md("Terraform Backend State Unreachable", "Fix Terraform backend state unreachable errors when the remote state endpoint is inaccessible.",
       """## Error Description

Backend unreachable errors prevent Terraform from connecting to state:

```
Error: Error loading state

Error: timeout connecting to remote state backend
```

## Common Causes

- VPN or firewall blocking access.
- Backend service is down.
- Authentication token expired.

## How to Fix

**Check network connectivity:**

```bash
curl -I https://app.terraform.io
```

**Refresh authentication:**

```bash
export TFE_TOKEN="valid-token"
terraform init
```

**Use a local fallback:**

```hcl
terraform {
  backend "local" {
    path = "fallback.tfstate"
  }
}
```

## Examples

```bash
terraform init 2>&1 | head -20
terraform init -backend=false
```
"""),

    md("Terraform State Encryption Error", "Fix Terraform state encryption errors when the state backend encryption is misconfigured.",
       """## Error Description

State encryption errors occur when encrypted state cannot be read or written:

```
Error: Error decrypting state

Error: KMS access denied: arn:aws:kms:us-east-1:123456789012:key/abc-123
```

## Common Causes

- KMS key doesn't exist or is in different region.
- IAM role lacks `kms:Decrypt`/`kms:Encrypt` permission.

## How to Fix

**Verify KMS key:**

```bash
aws kms describe-key --key-id abc-123
```

**Grant KMS permissions:**

```hcl
{
  "Effect": "Allow",
  "Action": [
    "kms:Decrypt",
    "kms:Encrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "arn:aws:kms:us-east-1:123456789012:key/abc-123"
}
```

## Examples

```hcl
terraform {
  backend "s3" {
    bucket     = "my-encrypted-bucket"
    key        = "terraform.tfstate"
    encrypt    = true
    kms_key_id = "arn:aws:kms:us-east-1:123456789012:key/abc-123"
  }
}
```
"""),

    md("Terraform Sensitive State Shown", "Fix Terraform sensitive state shown warnings when sensitive values appear in state output.",
       """## Error Description

Sensitive state visibility warnings occur when sensitive data appears in state:

```
Warning: sensitive attribute "password" is displayed in plan output
because it was set in configuration.
```

## Common Causes

- Marked outputs as sensitive but referenced in other resources.
- Provider doesn't mark computed sensitive attributes.

## How to Fix

**Mark sensitive attributes:**

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

**Encrypt state at rest:**

```hcl
terraform {
  backend "s3" {
    encrypt = true
  }
}
```

## Examples

```hcl
output "api_key" {
  value     = var.api_key
  sensitive = true
}
```
"""),
    # =========================================================================
    # 5. RESOURCE ERRORS
    # =========================================================================
    md("Terraform Address Not Found", "Fix Terraform address not found errors when referencing a non-existent resource address.",
       """## Error Description

Address not found errors occur when referencing a resource that doesn't exist:

```
Error: Reference to undeclared resource

A managed resource "aws_instance" "web" has not been declared.
```

## Common Causes

- Resource was not created due to `count = 0`.
- Resource address typo.
- Resource defined in a different module.

## How to Fix

**Use conditional reference:**

```hcl
locals {
  web_ip = try(aws_instance.web[0].private_ip, "N/A")
}
```

## Examples

```hcl
locals {
  ip = try(aws_instance.web[0].private_ip, "not-created")
}
```
"""),

    md("Terraform Resource Configuration Error", "Fix Terraform resource configuration errors when resource blocks contain invalid settings.",
       """## Error Description

Resource configuration errors indicate invalid resource block syntax:

```
Error: Invalid resource configuration

resource "aws_instance" "web" has an invalid argument "ami_id".
Did you mean "ami"?
```

## Common Causes

- Argument name typo.
- Deprecated attribute used.

## How to Fix

**Check provider documentation:**

```bash
terraform providers schema -json | jq '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.attributes | keys'
```

## Examples

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.main.id
}
```
"""),

    md("Terraform Required Field Missing", "Fix Terraform required field missing errors when a mandatory resource argument is omitted.",
       """## Error Description

Missing required field errors occur when a resource lacks a mandatory argument:

```
Error: Missing required argument

The argument "ami" is required, but no definition was found.
```

## Common Causes

- Forgot to include a required argument.
- Module input variable not set.

## How to Fix

**Add the required argument:**

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
}
```

**Use variables with defaults:**

```hcl
variable "ami_id" {
  type    = string
  default = "ami-0c55b159cbfafe1f0"
}
```

## Examples

```hcl
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
}
```
"""),

    md("Terraform Invalid Or Unknown Key", "Fix Terraform invalid or unknown key errors when an unrecognized argument is used.",
       """## Error Description

Unknown key errors occur when an unrecognized argument is present:

```
Error: Invalid or unknown key

on main.tf line 5, in resource "aws_instance" "web":
   5:   ami_name = "my-ami"
```

## Common Causes

- Typo in argument name.
- Argument from wrong provider version.

## How to Fix

**Check available attributes:**

```bash
terraform providers schema -json | jq \
  '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.attributes | keys'
```

## Examples

```bash
terraform providers schema -json > schema.json
cat schema.json | jq '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.attributes | keys'
```
"""),

    md("Terraform Unsupported Argument", "Fix Terraform unsupported argument errors when an argument is not supported by the resource.",
       """## Error Description

Unsupported argument errors occur when using an unsupported argument:

```
Error: Unsupported argument

An argument named "access_key" is not expected here.
```

## Common Causes

- Argument was removed in newer provider version.
- Mixing provider-level and resource-level arguments.

## How to Fix

**Remove or replace the argument:**

```hcl
# Wrong — "access_key" moved to provider
resource "aws_instance" "web" {
  access_key = "AKIA..."
}

# Correct — use provider block
provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  region     = "us-east-1"
}
```

## Examples

```hcl
provider "aws" {
  region     = var.region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}
```
"""),

    md("Terraform Conflicting Configuration", "Fix Terraform conflicting configuration errors when mutually exclusive settings are used.",
       """## Error Description

Conflicting configuration errors occur when mutually exclusive arguments are set:

```
Error: Conflicting configuration arguments

"cidr_block" and "ipv6_cidr_block" cannot both be set.
```

## Common Causes

- Using both inline and external security group rules.
- Setting count and for_each simultaneously.

## How to Fix

**Use dynamic blocks for conditional config:**

```hcl
resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ingress.value.cidrs
    }
  }
}
```

## Examples

```hcl
resource "aws_subnet" "main" {
  vpc_id          = var.vpc_id
  cidr_block      = var.ipv6_only ? null : var.cidr_block
  ipv6_cidr_block = var.ipv6_only ? var.ipv6_cidr_block : null
}
```
"""),

    md("Terraform Computed Field Cant Be Set", "Fix Terraform computed field can't be set errors when trying to assign values to read-only attributes.",
       """## Error Description

Computed field errors occur when trying to set a read-only attribute:

```
Error: Invalid attribute in config

The attribute "arn" is computed by the provider and cannot be
set in configuration.
```

## Common Causes

- Trying to set a provider-computed value.
- Copying values from state output into config.

## How to Fix

**Remove the computed attribute:**

```hcl
# Wrong
resource "aws_instance" "web" {
  ami = "ami-123"
  arn = "arn:aws:ec2:..."  # computed, cannot set
}

# Correct
resource "aws_instance" "web" {
  ami = "ami-123"
}
```

## Examples

```hcl
output "instance_arn" {
  value = aws_instance.web.arn  # computed, valid to read
}
```
"""),

    md("Terraform Undeclared Variable Used", "Fix Terraform undeclared variable used errors when referencing an undefined variable.",
       """## Error Description

Undeclared variable errors occur when referencing a variable not defined:

```
Error: Reference to undeclared variable

A variable "db_password" has not been declared.
```

## Common Causes

- Variable was deleted from variables.tf.
- Typo in variable name.

## How to Fix

**Declare the variable:**

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

**Or use terraform.tfvars:**

```bash
terraform apply -var="db_password=secret123"
```

## Examples

```hcl
variable "db_password" {
  type      = string
  sensitive = true
  description = "Database password"
}

resource "aws_db_instance" "main" {
  password = var.db_password
}
```
"""),

    md("Terraform Resource Instance Key Conflict", "Fix Terraform resource instance key conflict errors when multiple instances share the same key.",
       """## Error Description

Instance key conflicts occur when `for_each` creates duplicate keys:

```
Error: Duplicate resource instance key

Resource "aws_instance" has two instances with key "web".
Keys must be unique.
```

## Common Causes

- Input list has duplicate entries.
- Map keys collide after transformation.

## How to Fix

**Deduplicate input data:**

```hcl
locals {
  unique_instances = { for inst in var.instances : inst.name => inst }
}
```

## Examples

```hcl
variable "instances" {
  type = map(object({
    type = string
  }))
}
```
"""),

    md("Terraform Invalid Type For Attribute", "Fix Terraform invalid type for attribute errors when the wrong type is assigned.",
       """## Error Description

Type mismatch errors occur when assigning the wrong type:

```
Error: Incorrect attribute type

On main.tf line 15, in resource "aws_instance" "web":
  15:   tags = "Name=web"

Attribute "tags" must be a map of string, not a string.
```

## Common Causes

- Passing a string where a map is expected.
- Wrong type in variable definition.

## How to Fix

**Convert types using functions:**

```hcl
resource "aws_instance" "web" {
  tags = {
    Name = "web"
  }
}
```

**Use `tomap()` or `tolist()`:**

```hcl
locals {
  tag_map = tomap({ Name = "web", Environment = "prod" })
}
```

## Examples

```hcl
resource "aws_instance" "web" {
  instance_type = "t3.micro"
  ami           = "ami-12345"
  tags = {
    Name = "web"
  }
}
```
"""),

    md("Terraform Block Type Not Expected", "Fix Terraform block type not expected errors when using an incorrect nested block.",
       """## Error Description

Block type errors occur when an unexpected nested block is used:

```
Error: Block type "option" is not expected here

Only "tags", "root_block_device", "ebs_block_device" are
expected here.
```

## Common Causes

- Wrong block type name.
- Block is deprecated in current provider version.

## How to Fix

**Check available block types:**

```bash
terraform providers schema -json | jq \
  '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.block_types | keys'
```

**Use correct block syntax:**

```hcl
resource "aws_instance" "web" {
  ami = "ami-12345"

  root_block_device {
    volume_size = 50
    volume_type = "gp3"
  }
}
```

## Examples

```bash
terraform providers schema -json | jq \
  '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.block_types | keys'
```
"""),

    # =========================================================================
    # 6. MODULE ERRORS
    # =========================================================================
    md("Terraform Module Source Error", "Fix Terraform module source errors when the module source URL or path is invalid.",
       """## Error Description

Module source errors occur when Terraform cannot locate the module:

```
Error: Invalid module source address

"git::https://github.com/org/module.git?ref=v1.0" is not
a valid module source address.
```

## Common Causes

- Malformed source URL.
- Missing required parameters (ref, version).
- Local path doesn't exist.

## How to Fix

**Verify module source syntax:**

```hcl
# Registry
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = "~> 3.0"
}

# Git
module "vpc" {
  source = "git::https://github.com/org/module.git?ref=v1.0"
}

# Local
module "vpc" {
  source = "../modules/vpc"
}
```

## Examples

```hcl
module "vpc" {
  source  = "hashicorp/consul/aws"
  version = "0.1.0"
}
```
"""),

    md("Terraform Module Version Not Found", "Fix Terraform module version not found errors when a specific version doesn't exist.",
       """## Error Description

Module version not found errors occur when the requested version doesn't exist:

```
Error: Failed to download module

Could not find module version "2.0.0" for module "vpc".
Available: 1.0.0, 1.1.0, 1.2.0
```

## Common Causes

- Typo in version number.
- Version was yanked from registry.

## How to Fix

**Relax version constraints:**

```hcl
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = "~> 1.0"  # allows 1.x.x
}
```

## Examples

```hcl
module "vpc" {
  source  = "hashicorp/vpc/aws"
  version = ">= 1.0, < 2.0"
}
```
"""),

    md("Terraform Module Output Not Available", "Fix Terraform module output not available errors when referencing a non-existent module output.",
       """## Error Description

Module output not available errors occur when referencing a missing output:

```
Error: Reference to undeclared output

Module "vpc" does not output "subnet_ids". Available outputs:
"vpc_id", "cidr_block"
```

## Common Causes

- Output name typo in the module.
- Module was updated and output was removed.

## How to Fix

**Check available module outputs:**

```bash
cat modules/vpc/outputs.tf
```

**Use correct output name:**

```hcl
output "subnet_ids" {
  value = module.vpc.vpc_id
}
```

## Examples

```hcl
output "vpc_id" {
  value = module.vpc.vpc_id
}
```
"""),

    md("Terraform Module Variable Not Set", "Fix Terraform module variable not set errors when required module variables are missing.",
       """## Error Description

Module variable not set errors occur when a required variable has no value:

```
Error: Missing required argument

Module "vpc" requires argument "cidr_block" which was not provided.
```

## Common Causes

- Forgot to pass required variable to module.
- Variable in module has no default.

## How to Fix

**Pass the required variable:**

```hcl
module "vpc" {
  source     = "../modules/vpc"
  cidr_block = "10.0.0.0/16"
}
```

**Add defaults in the module:**

```hcl
variable "cidr_block" {
  type    = string
  default = "10.0.0.0/16"
}
```

## Examples

```hcl
module "vpc" {
  source     = "hashicorp/vpc/aws"
  cidr_block = var.vpc_cidr
  name       = "production"
}
```
"""),

    md("Terraform Module Count On Module", "Fix Terraform module count on module errors when using count with module blocks.",
       """## Error Description

Module count errors occur when the `count` expression is invalid:

```
Error: Invalid count argument

The "count" value for module "vpc" depends on resource
attributes that cannot be determined until apply.
```

## Common Causes

- Count expression depends on computed values.
- Variable used in count is not known at plan time.

## How to Fix

**Use boolean variables:**

```hcl
module "vpc" {
  source     = "../modules/vpc"
  count      = var.create_vpc ? 1 : 0
  cidr_block = var.vpc_cidr
}
```

## Examples

```hcl
variable "create_vpc" {
  type    = bool
  default = true
}

module "vpc" {
  source = "../modules/vpc"
  count  = var.create_vpc ? 1 : 0
}
```
"""),

    md("Terraform Module for_each Error", "Fix Terraform module for_each errors when iterating over a module with for_each.",
       """## Error Description

Module for_each errors occur when the iteration expression is invalid:

```
Error: Invalid for_each argument

The for_each value depends on resource attributes that cannot
be determined until apply.
```

## Common Causes

- for_each depends on computed values.
- Input map contains null or empty values.

## How to Fix

**Use variables with known values:**

```hcl
module "vpc" {
  source     = "../modules/vpc"
  for_each = var.environments
  name     = each.key
}

variable "environments" {
  type = map(object({
    cidr = string
  }))
  default = {
    prod = { cidr = "10.0.0.0/16" }
    dev  = { cidr = "10.1.0.0/16" }
  }
}
```

## Examples

```hcl
module "vpc" {
  for_each = {
    prod = "10.0.0.0/16"
    dev  = "10.1.0.0/16"
  }
  source     = "../modules/vpc"
  cidr_block = each.value
}
```
"""),

    md("Terraform Recursive Module Call", "Fix Terraform recursive module call errors when a module calls itself.",
       """## Error Description

Recursive module call errors occur when modules form circular references:

```
Error: Module "a" calls module "b" which calls module "a"

Cycle detected: module.a -> module.b -> module.a
```

## Common Causes

- Module A references Module B and vice versa.
- Self-referencing module.

## How to Fix

**Break the cycle:**

```hcl
module "shared" {
  source = "../modules/shared"
}

module "a" {
  source    = "../modules/a"
  shared_id = module.shared.id
}

module "b" {
  source    = "../modules/b"
  shared_id = module.shared.id
}
```

## Examples

```bash
terraform graph -type=module | dot -Tpng > modules.png
```
"""),

    md("Terraform Module Depends_on Error", "Fix Terraform module depends_on errors when module-level depends_on causes issues.",
       """## Error Description

Module depends_on errors occur when module-level dependencies cause problems:

```
Error: Module depends on resource not yet created

Module "compute" depends on module.database which has not
been created yet.
```

## Common Causes

- Implicit dependencies not sufficient.
- depends_on creates hidden dependency chains.

## How to Fix

**Use explicit variable references:**

```hcl
module "compute" {
  source = "../modules/compute"

  # Use variable references instead of depends_on
  db_host = module.database.host
  db_port = module.database.port
}
```

## Examples

```hcl
module "app" {
  source     = "../modules/app"
  db_host    = module.database.endpoint
  db_name    = module.database.name
  subnet_ids = module.vpc.private_subnets
}
```
"""),

    md("Terraform Module Registry Error", "Fix Terraform module registry errors when accessing modules from a private registry.",
       """## Error Description

Module registry errors occur when Terraform cannot access the registry:

```
Error: Failed to download module

Error: could not download module from
"registry.terraform.io/my-org/module": 401 Unauthorized
```

## Common Causes

- Invalid or expired authentication token.
- Module doesn't exist in the registry.

## How to Fix

**Configure registry credentials:**

```hcl
# ~/.terraformrc
credentials "app.terraform.io" {
  token = "your-api-token"
}
```

**Use Git source instead:**

```hcl
module "app" {
  source = "git::https://gitlab.com/my-org/module.git?ref=v1.0"
}
```

## Examples

```bash
export TFE_TOKEN="your-api-token"
terraform init
```
"""),

    md("Terraform Module Directory Not Found", "Fix Terraform module directory not found errors when local module path is invalid.",
       """## Error Description

Module directory not found errors occur when a local path doesn't exist:

```
Error: Module directory not found

Module directory "../modules/vpc" does not exist.
```

## Common Causes

- Directory path is wrong.
- Directory was deleted or moved.

## How to Fix

**Verify directory exists:**

```bash
ls -la ../modules/vpc/
```

**Use absolute path:**

```hcl
module "vpc" {
  source = "/opt/terraform/modules/vpc"
}
```

## Examples

```bash
find . -name "*.tf" -path "*/modules/*" | head -20
```
"""),

    md("Terraform Module Submodule Error", "Fix Terraform module submodule errors when calling nested or child modules.",
       """## Error Description

Submodule errors occur when calling nested modules incorrectly:

```
Error: Module not found

Module "vpc/subnets" was not found in the module directory.
```

## Common Causes

- Submodule directory structure is wrong.
- Module source path incorrect.

## How to Fix

**Verify submodule structure:**

```
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
    subnets/
      main.tf
      variables.tf
```

**Reference submodule correctly:**

```hcl
module "vpc_subnets" {
  source = "../modules/vpc/subnets"
  vpc_id = module.vpc.vpc_id
}
```

## Examples

```hcl
module "database" {
  source = "../../modules/database"
  vpc_id = module.vpc.id
}
```
"""),
    # =========================================================================
    # 7. WORKSPACE ERRORS
    # =========================================================================
    md("Terraform Workspace Not Found", "Fix Terraform workspace not found errors when selecting a non-existent workspace.",
       """## Error Description

Workspace not found errors occur when trying to select a workspace that doesn't exist:

```
Error: Workspace "production" not found.

Use "terraform workspace list" to see available workspaces.
```

## Common Causes

- Workspace was deleted.
- Typo in workspace name.

## How to Fix

**List available workspaces:**

```bash
terraform workspace list
```

**Create the workspace:**

```bash
terraform workspace new production
terraform workspace select production
```

## Examples

```bash
terraform workspace new staging
terraform workspace select staging
terraform workspace list
```
"""),

    md("Terraform Workspace Already Exists", "Fix Terraform workspace already exists errors when creating a workspace that already exists.",
       """## Error Description

Workspace already exists errors occur when trying to create a duplicate:

```
Error: Workspace "staging" already exists.

A workspace with this name already exists.
```

## Common Causes

- Workspace was created previously.
- CI/CD pipeline creates workspace without checking.

## How to Fix

**Check if workspace exists first:**

```bash
terraform workspace list | grep staging
```

**Use conditional creation in scripts:**

```bash
if ! terraform workspace list | grep -q "staging"; then
  terraform workspace new staging
fi
terraform workspace select staging
```

## Examples

```bash
terraform workspace new staging 2>/dev/null || terraform workspace select staging
```
"""),

    md("Terraform Workspace Delete Failed", "Fix Terraform workspace delete failed errors when removing a workspace.",
       """## Error Description

Workspace delete errors occur when Terraform cannot remove a workspace:

```
Error: Error deleting workspace "staging"

Cannot delete workspace with existing resources.
```

## Common Causes

- Workspace contains resources that must be destroyed first.
- Cannot delete the currently selected workspace.

## How to Fix

**Destroy resources first:**

```bash
terraform workspace select staging
terraform destroy
```

**Switch to default workspace before deleting:**

```bash
terraform workspace select default
terraform workspace delete staging
```

## Examples

```bash
terraform workspace select default
terraform workspace delete staging
```
"""),

    md("Terraform Workspace To Non-existent Target", "Fix Terraform workspace errors when moving or copying to a non-existent workspace.",
       """## Error Description

This error occurs when referencing a workspace that doesn't exist:

```
Error: Target workspace "deploy" does not exist

The workspace "deploy" referenced by state push does not exist.
```

## Common Causes

- Typo in target workspace name.
- Workspace not yet created.

## How to Fix

**Create the target workspace:**

```bash
terraform workspace new deploy
```

**Verify workspace list:**

```bash
terraform workspace list
```

## Examples

```bash
terraform workspace new deploy
terraform workspace select deploy
terraform init
```
"""),

    md("Terraform Workspace State Not Found", "Fix Terraform workspace state not found errors when the workspace state file is missing.",
       """## Error Description

Workspace state not found errors occur when state for a workspace is missing:

```
Error: State not found for workspace "staging"

The state file for workspace "staging" was not found.
```

## Common Causes

- Workspace was created but never initialized.
- State file was deleted from backend.

## How to Fix

**Initialize the workspace:**

```bash
terraform workspace select staging
terraform init
```

**Import resources into workspace:**

```bash
terraform workspace select staging
terraform import aws_instance.web i-0123456789
```

## Examples

```bash
aws s3 ls s3://my-bucket/env:/staging/terraform.tfstate
```
"""),

    md("Terraform Workspace Select Failed", "Fix Terraform workspace select failed errors when switching between workspaces.",
       """## Error Description

Workspace select errors occur when switching to a different workspace fails:

```
Error: Error selecting workspace

Workspace "production" has uncommitted changes.
```

## Common Causes

- Uncommitted state changes.
- State lock held by another process.

## How to Fix

**Commit or discard changes:**

```bash
terraform plan -refresh-only
```

**Force-select workspace:**

```bash
terraform workspace select -force production
```

## Examples

```bash
terraform workspace select default
terraform plan -refresh-only
terraform workspace select production
terraform plan
```
"""),

    md("Terraform Workspace List Error", "Fix Terraform workspace list errors when listing available workspaces fails.",
       """## Error Description

Workspace list errors occur when Terraform cannot enumerate workspaces:

```
Error: Error listing workspaces

AccessDenied: Access denied to workspace list endpoint
```

## Common Causes

- Backend permissions insufficient.
- Backend service unavailable.

## How to Fix

**Check backend permissions:**

```bash
aws s3 ls s3://my-bucket/env:/
```

**Use local backend for debugging:**

```hcl
terraform {
  backend "local" {}
}
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  "https://app.terraform.io/api/v2/organizations/my-org/workspaces" | jq
```
"""),

    md("Terraform Current Workspace Deleted", "Fix Terraform current workspace deleted errors when the active workspace was removed.",
       """## Error Description

This error occurs when the currently selected workspace no longer exists:

```
Error: Current workspace "staging" no longer exists

The workspace has been deleted.
```

## Common Causes

- Workspace deleted by another user or automation.
- CI/CD pipeline deleted the workspace.

## How to Fix

**Switch to default workspace:**

```bash
terraform workspace select default
```

**Recreate the workspace:**

```bash
terraform workspace new staging
terraform init
```

## Examples

```bash
terraform workspace select default
terraform workspace new staging
terraform init -migrate-state
```
"""),

    md("Terraform Workspace Name Invalid", "Fix Terraform workspace name invalid errors when workspace name contains invalid characters.",
       """## Error Description

Invalid workspace name errors occur when the name doesn't match requirements:

```
Error: Invalid workspace name "my staging"

Workspace names can only contain letters, numbers, hyphens,
and underscores.
```

## Common Causes

- Spaces in workspace name.
- Special characters not allowed.
- Name too long.

## How to Fix

**Use valid characters only:**

```bash
terraform workspace new my-staging
terraform workspace new my_staging
```

**Naming requirements:**

- Only letters, numbers, `-`, and `_`
- Max 64 characters
- Cannot start with `global` (reserved)

## Examples

```bash
terraform workspace new prod-us-east-1
terraform workspace new staging_2024
terraform workspace new feature-xyz
```
"""),

    md("Terraform Workspace Show Error", "Fix Terraform workspace show errors when displaying current workspace information.",
       """## Error Description

Workspace show errors occur when Terraform cannot display workspace info:

```
Error: Error showing current workspace

Unable to retrieve workspace information from backend.
```

## Common Causes

- Backend is unreachable.
- State file is corrupted.

## How to Fix

**Check backend connectivity:**

```bash
terraform workspace show 2>&1
```

**Reinitialize:**

```bash
terraform init -reconfigure
```

## Examples

```bash
terraform workspace show
terraform workspace show -json 2>/dev/null || echo "default"
```
"""),

    # =========================================================================
    # 8. OUTPUT ERRORS
    # =========================================================================
    md("Terraform Output Not Found", "Fix Terraform output not found errors when referencing a non-existent output.",
       """## Error Description

Output not found errors occur when referencing an output that doesn't exist:

```
Error: Reference to undeclared output

A named output "vpc_id" has not been declared in the root module.
```

## Common Causes

- Output was removed from configuration.
- Typo in output name.

## How to Fix

**Check available outputs:**

```bash
terraform output
```

**Declare the output:**

```hcl
output "vpc_id" {
  value = aws_vpc.main.id
}
```

**Use `try()` for optional outputs:**

```hcl
locals {
  vpc_id = try(module.vpc.vpc_id, "N/A")
}
```

## Examples

```bash
terraform output
terraform output -raw vpc_id
```
"""),

    md("Terraform Output Value Not Available", "Fix Terraform output value not available errors when output value cannot be determined.",
       """## Error Description

Output value not available errors occur when output depends on uncreated resources:

```
Error: Output value not available

The output "instance_ip" depends on resource
"aws_instance.web" which has not been created yet.
```

## Common Causes

- Output references a resource with `count = 0`.
- Resource creation failed.

## How to Fix

**Use `try()` for safe reference:**

```hcl
output "instance_ip" {
  value = try(aws_instance.web[0].public_ip, "N/A")
}
```

## Examples

```hcl
output "db_endpoint" {
  value = try(aws_db_instance.main[0].endpoint, "pending")
}
```
"""),

    md("Terraform Sensitive Output Leaked", "Fix Terraform sensitive output leaked warnings when sensitive output values are exposed.",
       """## Error Description

Sensitive output leaks occur when a sensitive output value is displayed:

```
Warning: Output "db_password" is marked as sensitive, but
its value is shown because it is referenced elsewhere.
```

## Common Causes

- Sensitive output referenced in non-sensitive output.
- Sensitive value passed to `nonsensitive()`.

## How to Fix

**Keep sensitive outputs marked:**

```hcl
output "db_password" {
  value     = random_password.db.result
  sensitive = true
}
```

## Examples

```hcl
output "api_key" {
  value     = var.api_key
  sensitive = true
}
```
"""),

    md("Terraform Output Dependency Missing", "Fix Terraform output dependency missing errors when outputs reference non-existent resources.",
       """## Error Description

Output dependency missing errors occur when outputs reference missing resources:

```
Error: Reference to undeclared resource

Output "endpoint" references "aws_db_instance.main" which
has not been declared.
```

## Common Causes

- Resource was removed from configuration.

## How to Fix

**Use module outputs properly:**

```hcl
output "endpoint" {
  value = module.database.endpoint
}
```

**Add explicit dependency:**

```hcl
output "endpoint" {
  value     = aws_db_instance.main.endpoint
  depends_on = [aws_db_instance.main]
}
```

## Examples

```hcl
output "vpc_id" {
  value     = module.vpc.vpc_id
  depends_on = [module.vpc]
}
```
"""),

    md("Terraform Output Cross-workspace Reference", "Fix Terraform output cross-workspace reference errors when referencing outputs across workspaces.",
       """## Error Description

Cross-workspace reference errors occur when trying to access outputs from a different workspace:

```
Error: Cross-workspace references are not supported

Cannot reference output "vpc_id" from workspace "staging"
in workspace "production".
```

## Common Causes

- Terraform doesn't support cross-workspace references.

## How to Fix

**Use `terraform_remote_state`:**

```hcl
data "terraform_remote_state" "staging" {
  backend = "s3"
  config = {
    bucket = "my-terraform-state"
    key    = "staging/terraform.tfstate"
    region = "us-east-1"
  }
}

output "staging_vpc_id" {
  value = data.terraform_remote_state.staging.outputs.vpc_id
}
```

## Examples

```hcl
data "terraform_remote_state" "staging" {
  backend = "s3"
  config = {
    bucket = "my-state-bucket"
    key    = "staging/terraform.tfstate"
    region = "us-east-1"
  }
}
```
"""),

    md("Terraform Output Module Not Found", "Fix Terraform output module not found errors when referencing a non-existent module output.",
       """## Error Description

Output module not found errors occur when an output references a missing module:

```
Error: Reference to undeclared module

An undeclared module named "vpc" has been referenced.
```

## Common Causes

- Module was removed from configuration.
- Typo in module name.

## How to Fix

**Verify module exists:**

```bash
ls -la modules/vpc/
```

**Check module declaration:**

```hcl
module "vpc" {
  source = "../modules/vpc"
}
```

## Examples

```hcl
output "vpc_id" {
  value = module.vpc.vpc_id
}
```
"""),

    md("Terraform Output Interpolation Error", "Fix Terraform output interpolation errors when interpolating values in output strings.",
       """## Error Description

Interpolation errors occur when string interpolation syntax is wrong:

```
Error: Invalid template interpolation

Expected a valid value for expression: ${aws_instance.web.ip}
- did you mean "private_ip"?
```

## Common Causes

- Typo in attribute name.
- Wrong interpolation syntax.

## How to Fix

**Use correct interpolation syntax:**

```hcl
output "connection_string" {
  value = "postgres://user:pass@${aws_db_instance.main.address}:5432/db"
}
```

**Use `format()`:**

```hcl
output "endpoint" {
  value = format("%s:%d", aws_db_instance.main.address, aws_db_instance.main.port)
}
```

## Examples

```hcl
output "instance_info" {
  value = "Instance ${aws_instance.web.id} is at ${aws_instance.web.private_ip}"
}
```
"""),

    md("Terraform Output Value Type Mismatch", "Fix Terraform output value type mismatch errors when output type doesn't match declaration.",
       """## Error Description

Type mismatch errors occur when the output value doesn't match its type:

```
Error: Incorrect output type

Output "instance_ids" is declared as list(string) but value
is of type list(number).
```

## Common Causes

- Output type declaration doesn't match actual value.

## How to Fix

**Correct the type or convert value:**

```hcl
output "instance_ids" {
  value = [for inst in aws_instance.web : inst.id]
}
```

**Use type conversion:**

```hcl
output "port" {
  value = tostring(aws_db_instance.main.port)
}
```

## Examples

```hcl
output "instance_ids" {
  type  = list(string)
  value = [for i in aws_instance.web : i.id]
}

output "endpoint" {
  type  = string
  value = aws_db_instance.main.endpoint
}
```
"""),

    # =========================================================================
    # 9. VARIABLE ERRORS
    # =========================================================================
    md("Terraform Variable Not Declared", "Fix Terraform variable not declared errors when referencing undefined variables.",
       """## Error Description

Variable not declared errors occur when using an undeclared variable:

```
Error: Reference to undeclared variable

A variable "environment" has not been declared.
```

## Common Causes

- Variable definition was deleted.
- Typo in variable name.

## How to Fix

**Declare the variable:**

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"
}
```

**Or pass via CLI:**

```bash
terraform apply -var="environment=production"
```

## Examples

```hcl
variable "environment" {
  type        = string
  description = "Environment name"
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```
"""),

    md("Terraform Variable Default Type Mismatch", "Fix Terraform variable default type mismatch errors when the default value doesn't match the type.",
       """## Error Description

Default type mismatch errors occur when default value doesn't match type:

```
Error: Invalid default value for variable

The variable "instance_count" has type "number" but the
default value "three" is not a valid number.
```

## Common Causes

- Default value doesn't match declared type.
- String used where number is expected.

## How to Fix

**Use correct default types:**

```hcl
variable "instance_count" {
  type    = number
  default = 3  # not "three"
}

variable "tags" {
  type = map(string)
  default = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```

## Examples

```hcl
variable "enabled" {
  type    = bool
  default = true
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}
```
"""),

    md("Terraform Variable Validation Failed", "Fix Terraform variable validation failed errors when input doesn't pass validation.",
       """## Error Description

Validation errors occur when variable values don't pass validation:

```
Error: Invalid value for variable "environment"

Variable "environment" must be one of ["dev", "staging", "prod"],
but got "test".
```

## Common Causes

- Input value doesn't meet validation criteria.
- Validation rule is too restrictive.

## How to Fix

**Use appropriate validation rules:**

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_count" {
  type = number

  validation {
    condition     = var.instance_count > 0 && var.instance_count <= 100
    error_message = "Instance count must be between 1 and 100."
  }
}
```

## Examples

```hcl
variable "email" {
  type = string

  validation {
    condition     = can(regex("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", var.email))
    error_message = "Must be a valid email address."
  }
}
```
"""),

    md("Terraform Variable Environment Not Set", "Fix Terraform variable environment not set errors when expected environment variables are missing.",
       """## Error Description

Missing environment variable errors occur when Terraform expects env vars:

```
Error: Missing required variable

Variable "AWS_ACCESS_KEY_ID" is required but not set in environment.
```

## Common Causes

- Environment variables not exported.
- Shell session doesn't have the variables.

## How to Fix

**Set environment variables:**

```bash
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."
terraform plan
```

**Source before running:**

```bash
source .env && terraform plan
```

## Examples

```bash
# AWS credentials
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."

# GCP credentials
export GOOGLE_CREDENTIALS="$(cat service-account.json)"

# Azure
export ARM_CLIENT_ID="..."
export ARM_CLIENT_SECRET="..."
```
"""),

    md("Terraform Variable File Not Found", "Fix Terraform variable file not found errors when the specified tfvars file doesn't exist.",
       """## Error Description

Variable file not found errors occur when a referenced tfvars file is missing:

```
Error: Failed to read file

The file "production.tfvars" cannot be read: no such file or directory.
```

## Common Causes

- Typo in filename.
- Wrong directory path.

## How to Fix

**Check file exists:**

```bash
ls -la *.tfvars
```

**Create the file:**

```bash
cat > production.tfvars << EOF
environment    = "production"
instance_count = 5
instance_type  = "t3.large"
EOF
```

## Examples

```bash
# Auto-loaded files
terraform.tfvars
*.auto.tfvars

# Explicit file
terraform plan -var-file="production.tfvars"
```
"""),

    md("Terraform Variable Type Constraint Error", "Fix Terraform variable type constraint errors when the value doesn't match the type constraint.",
       """## Error Description

Type constraint errors occur when a variable value doesn't match type:

```
Error: Invalid value for variable "ports"

Variable "ports" must be a list of numbers, but got
["80", "443"] which contains strings.
```

## Common Causes

- Input type doesn't match variable type.
- Variable type definition is wrong.

## How to Fix

**Use correct type definitions:**

```hcl
variable "ports" {
  type    = list(number)
  default = [80, 443]
}

variable "config" {
  type = object({
    name    = string
    port    = number
    enabled = bool
  })
}
```

**Convert types in calling code:**

```hcl
module "app" {
  source = "../modules/app"
  ports  = [for p in var.port_strings : tonumber(p)]
}
```

## Examples

```hcl
variable "instances" {
  type = map(object({
    type = string
    ami  = string
    tags = map(string)
  }))
}
```
"""),

    md("Terraform Variable Sensitive Value Exposed", "Fix Terraform variable sensitive value exposed warnings when sensitive variables appear in output.",
       """## Error Description

Sensitive value exposure warnings appear when sensitive variables appear in plain text:

```
Warning: Sensitive variable "db_password" is used in
non-sensitive output "connection_string".
```

## Common Causes

- Sensitive variable used in string interpolation.
- Variable passed to non-sensitive output.

## How to Fix

**Keep sensitive variables marked:**

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

**Mark outputs containing sensitive values:**

```hcl
output "connection_string" {
  value     = "postgres://admin:${var.db_password}@host/db"
  sensitive = true
}
```

## Examples

```hcl
variable "api_key" {
  type      = string
  sensitive = true
}

output "api_config" {
  value = {
    key = var.api_key
  }
  sensitive = true
}
```
"""),

    md("Terraform Variable Nullable Conflict", "Fix Terraform variable nullable conflicts when null values conflict with type constraints.",
       """## Error Description

Nullable conflicts occur when null is used with non-nullable types:

```
Error: Invalid value for variable "name"

Variable "name" is not nullable but received null value.
```

## Common Causes

- Variable is non-nullable but null is passed.
- Module passes null for required variable.

## How to Fix

**Use nullable = true (default):**

```hcl
variable "name" {
  type    = string
  default = "default-name"
}
```

**Handle null with conditionals:**

```hcl
resource "aws_instance" "web" {
  instance_type = var.instance_type != null ? var.instance_type : "t3.micro"
}
```

## Examples

```hcl
variable "environment" {
  type     = string
  default  = "dev"
  nullable = true
}

locals {
  env = var.environment != null ? var.environment : "dev"
}
```
"""),

    md("Terraform Variable Required But Not Set", "Fix Terraform variable required but not set errors when mandatory variables have no value.",
       """## Error Description

Required variable errors occur when a variable with no default is not provided:

```
Error: Required variable not set

Variable "vpc_cidr" is required but was not provided.
```

## Common Causes

- Variable has no default and wasn't provided.
- tfvars file missing the variable.

## How to Fix

**Provide via tfvars:**

```hcl
# terraform.tfvars
vpc_cidr    = "10.0.0.0/16"
environment = "production"
```

**Provide via CLI:**

```bash
terraform apply -var="vpc_cidr=10.0.0.0/16"
```

**Add a default if appropriate:**

```hcl
variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}
```

## Examples

```bash
terraform apply -var-file="production.tfvars"
```
"""),

    md("Terraform Variable Value Too Long", "Fix Terraform variable value too long errors when a variable exceeds maximum length.",
       """## Error Description

Value too long errors occur when input exceeds length constraints:

```
Error: Invalid value for variable "instance_name"

The value exceeds the maximum length of 63 characters.
```

## Common Causes

- Generated name exceeds provider limits.
- Concatenation produces overly long strings.

## How to Fix

**Add validation for length:**

```hcl
variable "instance_name" {
  type = string

  validation {
    condition     = length(var.instance_name) <= 63
    error_message = "Instance name must be 63 characters or less."
  }
}
```

**Truncate names using functions:**

```hcl
locals {
  safe_name = substr(var.instance_name, 0, 63)
}

resource "aws_instance" "web" {
  tags = {
    Name = local.safe_name
  }
}
```

## Examples

```hcl
variable "name" {
  type = string

  validation {
    condition     = length(var.name) >= 3 && length(var.name) <= 63
    error_message = "Name must be between 3 and 63 characters."
  }
}
```
"""),

    # =========================================================================
    # 10. PROVISIONER ERRORS
    # =========================================================================
    md("Terraform Provisioner Connection Failed", "Fix Terraform provisioner connection failed errors when provisioners cannot reach the resource.",
       """## Error Description

Connection failures occur when provisioners cannot connect:

```
Error: connection is shut down

dial tcp 52.1.2.3:22: connect: connection refused
```

## Common Causes

- Resource not fully booted when provisioner runs.
- SSH key not configured correctly.
- Firewall rules blocking connection.

## How to Fix

**Add connection timeout:**

```hcl
provisioner "remote-exec" {
  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    timeout     = "5m"
  }

  inline = ["sudo yum update -y"]
}
```

## Examples

```hcl
connection {
  type        = "ssh"
  host        = self.public_ip
  user        = "ubuntu"
  port        = 22
  private_key = file("~/.ssh/deploy_key")
  agent       = false
  timeout     = "3m"
}
```
"""),

    md("Terraform Provisioner Timeout", "Fix Terraform provisioner timeout errors when provisioner scripts take too long.",
       """## Error Description

Provisioner timeout errors occur when scripts exceed timeout:

```
Error: timeout

The provisioner timed out after 5m0s while waiting for
the script to complete.
```

## Common Causes

- Script takes longer than expected.
- Network issues causing slow downloads.
- Interactive prompt hanging.

## How to Fix

**Increase the timeout:**

```hcl
provisioner "remote-exec" {
  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    timeout     = "15m"
  }

  inline = ["sudo yum update -y && sudo yum install -y docker"]
}
```

**Break into smaller steps:**

```hcl
provisioner "remote-exec" {
  inline = ["sudo yum update -y"]
}

provisioner "remote-exec" {
  inline = ["sudo yum install -y docker"]
}
```

## Examples

```hcl
provisioner "remote-exec" {
  connection {
    timeout = "30m"
  }
  inline = ["sudo apt-get update && sudo apt-get install -y build-essential"]
}
```
"""),

    md("Terraform File Provisioner Not Found", "Fix Terraform file provisioner not found errors when the source file doesn't exist.",
       """## Error Description

File provisioner errors occur when the source file is missing:

```
Error: File source not found

Source file "scripts/deploy.sh" does not exist.
```

## Common Causes

- File path is incorrect.
- File was deleted or not committed.

## How to Fix

**Verify source file exists:**

```bash
ls -la scripts/deploy.sh
```

**Use file function for templates:**

```hcl
provisioner "file" {
  content     = templatefile("scripts/deploy.sh.tpl", { env = "prod" })
  destination = "/tmp/deploy.sh"
}
```

## Examples

```hcl
provisioner "file" {
  source      = "scripts/setup.sh"
  destination = "/tmp/setup.sh"
}
```
"""),

    md("Terraform Remote-exec Script Not Found", "Fix Terraform remote-exec script not found errors when the script file is missing.",
       """## Error Description

Remote-exec script not found errors occur when referencing a missing script:

```
Error: Script file not found

The script file "scripts/provision.sh" referenced in
remote-exec provisioner does not exist.
```

## Common Causes

- Script file deleted or not created.
- Path is wrong relative to working directory.

## How to Fix

**Use inline commands instead:**

```hcl
provisioner "remote-exec" {
  inline = [
    "sudo apt-get update",
    "sudo apt-get install -y nginx",
    "sudo systemctl enable nginx"
  ]
}
```

**Ensure script exists:**

```bash
mkdir -p scripts
cat > scripts/provision.sh << 'EOF'
#!/bin/bash
sudo apt-get update
sudo apt-get install -y nginx
EOF
```

## Examples

```hcl
provisioner "remote-exec" {
  inline = [
    "sudo systemctl start docker",
    "docker pull nginx:latest",
    "docker run -d -p 80:80 nginx"
  ]
}
```
"""),

    md("Terraform Local-exec Command Failed", "Fix Terraform local-exec command failed errors when local commands fail.",
       """## Error Description

Local-exec command failures occur when the locally executed command fails:

```
Error: local-exec provisioner error

Error running command: exit status 127
Output: bash: my-script.sh: command not found
```

## Common Causes

- Command or script not in PATH.
- Script not executable.
- Missing dependencies on local machine.

## How to Fix

**Use absolute paths:**

```hcl
provisioner "local-exec" {
  command = "/bin/bash ${path.module}/scripts/setup.sh"
}
```

**Make script executable:**

```bash
chmod +x scripts/setup.sh
```

## Examples

```hcl
provisioner "local-exec" {
  command     = "./scripts/deploy.sh"
  working_dir = "${path.module}"
  environment = {
    INSTANCE_ID = self.id
  }
}
```
"""),

    md("Terraform Chef Provisioner Error", "Fix Terraform Chef provisioner errors when Chef client fails during provisioning.",
       """## Error Description

Chef provisioner errors occur when the Chef client fails:

```
Error: Chef provisioner error

Chef client failed to converge: runtime error: no Chef
client binary found in PATH
```

## Common Causes

- Chef client not installed on target.
- Chef server unreachable.
- Invalid run list or attributes.

## How to Fix

**Install Chef before provisioning:**

```hcl
provisioner "remote-exec" {
  inline = [
    "curl -L https://omnitruck.chef.io/install.sh | bash",
    "chef-client --version"
  ]
}
```

**Use correct Chef configuration:**

```hcl
provisioner "chef" {
  server_url          = "https://chef.example.com"
  validation_key_path = "~/.chef/validation.pem"
  node_name           = self.id
  run_list            = ["role[webserver]"]
}
```

## Examples

```hcl
provisioner "chef" {
  server_url          = var.chef_server_url
  validation_key_path = var.chef_validation_key
  node_name           = "web-${self.id}"
  run_list            = ["role[base]", "role[webserver]"]
  environment         = var.chef_environment
}
```
"""),

    md("Terraform Puppet Provisioner Error", "Fix Terraform Puppet provisioner errors when Puppet agent fails during provisioning.",
       """## Error Description

Puppet provisioner errors occur when the Puppet agent fails:

```
Error: Puppet provisioner error

Puppet agent run failed: Error: Could not find environment
'manifests' on server
```

## Common Causes

- Puppet server not configured.
- Puppet agent not installed.
- Module path incorrect.

## How to Fix

**Install Puppet before provisioning:**

```hcl
provisioner "remote-exec" {
  inline = [
    "wget https://apt.puppet.com/puppet-tools-release-focal.deb",
    "sudo dpkg -i puppet-tools-release-focal.deb",
    "sudo apt-get update",
    "sudo apt-get install -y puppet-agent"
  ]
}
```

**Configure provisioner correctly:**

```hcl
provisioner "puppet" {
  server       = "puppet.example.com"
  certname     = "web-${self.id}"
  module_paths = ["/etc/puppetlabs/code/environments/production/modules"]
}
```

## Examples

```hcl
provisioner "puppet" {
  server       = var.puppet_server
  certname     = self.private_dns
  module_paths = ["/etc/puppet/modules"]
}
```
"""),

    md("Terraform Salt Provisioner Error", "Fix Terraform Salt provisioner errors when Salt minion fails during provisioning.",
       """## Error Description

Salt provisioner errors occur when the Salt minion fails:

```
Error: Salt provisioner error

Salt state apply failed: Error: Unable to locate configuration file
```

## Common Causes

- Salt minion not installed.
- Master not reachable.
- Pillar data missing.

## How to Fix

**Install Salt before provisioning:**

```hcl
provisioner "remote-exec" {
  inline = [
    "sudo apt-get update",
    "sudo apt-get install -y salt-minion",
    "echo 'master: ${var.salt_master}' | sudo tee /etc/salt/minion.d/master.conf",
    "sudo systemctl restart salt-minion"
  ]
}
```

**Use correct Salt provisioner config:**

```hcl
provisioner "salt" {
  salt_state     = "webserver"
  salt_master_ip = var.salt_master_ip
  temp_dir       = "/tmp/salt"
}
```

## Examples

```hcl
provisioner "salt" {
  salt_state     = "highstate"
  salt_master_ip = "10.0.1.100"
  environment    = "production"
}
```
"""),

    md("Terraform Ansible Provisioner Error", "Fix Terraform Ansible provisioner errors when Ansible playbook execution fails.",
       """## Error Description

Ansible provisioner errors occur when Ansible cannot run the playbook:

```
Error: local-exec provisioner error

Error: playbook not found: playbooks/setup.yml
```

## Common Causes

- Playbook file path wrong.
- Ansible not installed locally.
- SSH connectivity issues.

## How to Fix

**Use correct playbook path:**

```hcl
provisioner "local-exec" {
  command = "ansible-playbook -i '${self.public_ip},' -u ec2-user ${path.module}/playbooks/setup.yml"
}
```

**Install Ansible locally:**

```bash
pip install ansible
```

## Examples

```hcl
provisioner "local-exec" {
  command = <<-EOT
    ansible-playbook
    -i '${self.public_ip},'
    -u ec2-user
    --private-key ~/.ssh/deploy_key
    -e 'env=production'
    playbooks/deploy.yml
  EOT
  working_dir = path.module
}
```
"""),

    md("Terraform Provisioner On Destroy Not Supported", "Fix Terraform provisioner on destroy errors when destroy-time provisioners fail.",
       """## Error Description

Destroy-time provisioner errors occur during resource destruction:

```
Error: Error running provisioner

Provisioner "local-exec" with trigger "destroy" failed:
command exited with status 1
```

## Common Causes

- Cleanup script has errors.
- Resource already destroyed when provisioner runs.

## How to Fix

**Make destroy provisioner idempotent:**

```hcl
provisioner "local-exec" {
  when    = destroy
  command = "rm -f ${path.module}/state/${self.id}.json || true"
}
```

**Add error handling:**

```hcl
provisioner "local-exec" {
  when = destroy
  command = <<-EOT
    set -e || true
    aws s3 rm s3://bucket/${self.id}/ --recursive || true
  EOT
}
```

## Examples

```hcl
provisioner "remote-exec" {
  when = destroy
  inline = [
    "sudo systemctl stop nginx || true",
    "rm -rf /etc/nginx/conf.d/* || true"
  ]
}
```
"""),
    # =========================================================================
    # 11. CLOUD-SPECIFIC ERRORS
    # =========================================================================
    md("Terraform AWS Credentials Not Found", "Fix Terraform AWS credentials not found errors when AWS provider cannot authenticate.",
       """## Error Description

AWS credentials errors occur when the provider cannot find valid credentials:

```
Error: error configuring Terraform AWS Provider

no valid credential sources for Terraform AWS Provider found.
```

## Common Causes

- `AWS_ACCESS_KEY_ID` not set.
- `~/.aws/credentials` doesn't exist.
- IAM role not attached to EC2/ECS.
- SSO session expired.

## How to Fix

**Set environment variables:**

```bash
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_DEFAULT_REGION="us-east-1"
```

**Configure AWS CLI:**

```bash
aws configure
```

**Use IAM roles (recommended):**

```hcl
provider "aws" {
  region = "us-east-1"
  # No credentials needed — uses instance role
}
```

## Examples

```bash
aws sts get-caller-identity
aws sso login --profile production
export AWS_PROFILE=production
```
"""),

    md("Terraform EC2 Instance Not Found", "Fix Terraform EC2 instance not found errors when referencing a non-existent EC2 instance.",
       """## Error Description

EC2 instance not found errors occur when referencing a deleted or non-existent instance:

```
Error: Error finding instance

no matching EC2 instance found
```

## Common Causes

- Instance was manually terminated.
- Wrong instance ID.
- Wrong region.

## How to Fix

**Check instance status:**

```bash
aws ec2 describe-instances --instance-ids i-0123456789abcdef0
```

**Use data source with filters:**

```hcl
data "aws_instances" "web" {
  filter {
    name   = "tag:Environment"
    values = ["production"]
  }

  filter {
    name   = "instance-state-name"
    values = ["running"]
  }
}
```

## Examples

```hcl
data "aws_instance" "web" {
  filter {
    name   = "tag:Name"
    values = ["web-server"]
  }

  filter {
    name   = "instance-state-name"
    values = ["running"]
  }
}
```
"""),

    md("Terraform S3 Bucket Already Exists", "Fix Terraform S3 bucket already exists errors when the bucket name is taken globally.",
       """## Error Description

S3 bucket already exists errors occur when the bucket name is not globally unique:

```
Error: error creating S3 Bucket: BucketAlreadyExists

The requested bucket name is not available.
```

## Common Causes

- Bucket name already taken by another AWS account.
- Previously created bucket not cleaned up.

## How to Fix

**Use a unique naming convention:**

```hcl
resource "random_string" "bucket_suffix" {
  length  = 8
  special = false
  upper   = false
}

resource "aws_s3_bucket" "main" {
  bucket = "my-app-${var.environment}-${random_string.bucket_suffix.result}"
}
```

**Check if bucket exists:**

```bash
aws s3api head-bucket --bucket my-bucket-name 2>&1
```

## Examples

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "${var.project}-${var.environment}-logs-${random_id.suffix.hex}"
}
```
"""),

    md("Terraform Security Group Not Found", "Fix Terraform security group not found errors when referencing a non-existent security group.",
       """## Error Description

Security group not found errors occur when the referenced SG doesn't exist:

```
Error: Error: SecurityGroupNotFound

The security group 'sg-12345' does not exist in VPC 'vpc-abc123'
```

## Common Causes

- Security group was manually deleted.
- Wrong security group ID.
- Wrong VPC specified.

## How to Fix

**Create the security group in Terraform:**

```hcl
resource "aws_security_group" "web" {
  name   = "web-sg"
  vpc_id = aws_vpc.main.id
}
```

**Use data source for existing SG:**

```hcl
data "aws_security_group" "existing" {
  filter {
    name   = "group-name"
    values = ["web-sg"]
  }

  vpc_id = aws_vpc.main.id
}
```

## Examples

```hcl
resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```
"""),

    md("Terraform VPC Limit Exceeded", "Fix Terraform VPC limit exceeded errors when the account VPC quota is reached.",
       """## Error Description

VPC limit exceeded errors occur when you hit the account VPC quota:

```
Error: Error creating VPC: VpcLimitExceeded

The maximum number of VPCs has been reached.
```

## Common Causes

- Account VPC limit reached.
- Old VPCs not cleaned up.

## How to Fix

**Check current VPC count:**

```bash
aws ec2 describe-vpcs --query 'Vpcs[*].{ID:VpcId,Name:Tags[?Key==`Name`].Value|[0]}' --output table
```

**Request a quota increase:**

```bash
aws service-quotas request-service-quota-increase \
  --service-code ec2 \
  --quota-code L-0263D0A6 \
  --desired-value 10
```

**Clean up unused VPCs:**

```bash
aws ec2 describe-vpcs --query 'Vpcs[*].VpcId' --output text
terraform destroy -target=aws_vpc.unused
```

## Examples

```bash
aws service-quotas get-service-quota --service-code ec2 --quota-code L-0263D0A6
```
"""),

    md("Terraform Route53 Zone Not Found", "Fix Terraform Route53 zone not found errors when referencing a non-existent hosted zone.",
       """## Error Description

Route53 zone not found errors occur when the DNS zone doesn't exist:

```
Error: Error reading Route53 Zone

HostedZoneNotFound: The specified hosted zone does not exist.
```

## Common Causes

- Zone was deleted.
- Wrong zone ID.

## How to Fix

**Create the zone in Terraform:**

```hcl
resource "aws_route53_zone" "main" {
  name = "example.com"
}
```

**Use data source for existing zone:**

```hcl
data "aws_route53_zone" "main" {
  name         = "example.com"
  private_zone = false
}
```

## Examples

```hcl
resource "aws_route53_zone" "main" {
  name    = "example.com"
  comment = "Managed by Terraform"
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "www.example.com"
  type    = "A"
  ttl     = 300
  records = [aws_eip.web.public_ip]
}
```
"""),

    md("Terraform GCP Project Not Found", "Fix Terraform GCP project not found errors when the specified GCP project doesn't exist.",
       """## Error Description

GCP project not found errors occur when the project doesn't exist:

```
Error: Error reading Project "my-project"

googleapi: Error 403: The caller does not have permission,
project not found or access denied.
```

## Common Causes

- Project ID is incorrect.
- Project was deleted.
- IAM permissions insufficient.

## How to Fix

**Verify project exists:**

```bash
gcloud projects describe my-project
```

**Check permissions:**

```bash
gcloud projects get-iam-policy my-project
```

**Create the project in Terraform:**

```hcl
resource "google_project" "main" {
  name            = "My Project"
  project_id      = "my-project-123"
  billing_account = var.billing_account
}
```

## Examples

```hcl
provider "google" {
  project = "my-project-123"
  region  = "us-central1"
}
```
"""),

    md("Terraform GCS Bucket Access Denied", "Fix Terraform GCS bucket access denied errors when accessing Google Cloud Storage.",
       """## Error Description

GCS access denied errors occur when the bucket cannot be accessed:

```
Error: Error creating bucket

googleapi: Error 403: Access Not Configured. Cloud Storage
API has not been used in project before or disabled.
```

## Common Causes

- Cloud Storage API not enabled.
- IAM permissions insufficient.

## How to Fix

**Enable the Cloud Storage API:**

```bash
gcloud services enable storage-api.googleapis.com --project=my-project
```

**Grant required permissions:**

```hcl
resource "google_project_iam_member" "storage_admin" {
  project = var.project_id
  role    = "roles/storage.admin"
  member  = "serviceAccount:${var.service_account_email}"
}
```

## Examples

```hcl
resource "google_storage_bucket" "terraform_state" {
  name          = "${var.project_id}-terraform-state"
  location      = "US"
  force_destroy = false

  versioning {
    enabled = true
  }
}
```
"""),

    md("Terraform Azure Resource Group Not Found", "Fix Terraform Azure resource group not found errors when the resource group doesn't exist.",
       """## Error Description

Azure resource group not found errors occur when the RG doesn't exist:

```
Error: Error creating Resource Group

ResourceGroupNotFound: Resource group 'my-rg' could not be found.
```

## Common Causes

- Resource group was deleted.
- Wrong resource group name.
- Wrong subscription selected.

## How to Fix

**Create the resource group:**

```hcl
resource "azurerm_resource_group" "main" {
  name     = "my-rg"
  location = "East US"
}
```

**Use data source for existing RG:**

```hcl
data "azurerm_resource_group" "existing" {
  name = "my-rg"
}
```

**Check subscription:**

```bash
az account show
az account set --subscription="SUBSCRIPTION_ID"
```

## Examples

```hcl
resource "azurerm_resource_group" "main" {
  name     = "production-rg"
  location = "East US"

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```
"""),

    md("Terraform Azure VM Extension Error", "Fix Terraform Azure VM extension errors when deploying VM extensions fails.",
       """## Error Description

Azure VM extension errors occur when extensions fail to deploy:

```
Error: Error creating Virtual Machine Extension

compute.VirtualMachineExtensionsClient#CreateOrUpdate: Failure
Code: VMExtensionProvisioningError
```

## Common Causes

- Extension version not compatible with VM OS.
- VM not fully provisioned when extension runs.
- Required agent not installed on VM.

## How to Fix

**Add explicit dependency on VM:**

```hcl
resource "azurerm_virtual_machine_extension" "example" {
  name                 = "custom-script"
  virtual_machine_id   = azurerm_virtual_machine.example.id
  publisher            = "Microsoft.Azure.Extensions"
  type                 = "CustomScript"
  type_handler_version = "2.1"

  settings = jsonencode({
    commandToExecute = "echo 'Hello World'"
  })

  depends_on = [azurerm_virtual_machine.example]
}
```

## Examples

```hcl
resource "azurerm_virtual_machine_extension" "example" {
  name                 = "custom-script"
  virtual_machine_id   = azurerm_virtual_machine.example.id
  publisher            = "Microsoft.Azure.Extensions"
  type                 = "CustomScript"
  type_handler_version = "2.1"

  settings = jsonencode({
    commandToExecute = "apt-get update && apt-get install -y nginx"
  })
}
```
"""),

    # =========================================================================
    # 12. TERRAFORM CLOUD/ENTERPRISE
    # =========================================================================
    md("Terraform Cloud Workspace Not Found", "Fix Terraform Cloud workspace not found errors when the workspace doesn't exist.",
       """## Error Description

TFC workspace not found errors occur when referencing a non-existent workspace:

```
Error: Workspace "my-workspace" not found

The workspace could not be found in the organization.
```

## Common Causes

- Workspace was deleted.
- Wrong workspace name in configuration.
- Wrong organization configured.

## How to Fix

**Create the workspace:**

```bash
curl -X POST \
  -H "Authorization: Bearer $TFE_TOKEN" \
  -H "Content-Type: application/vnd.api+json" \
  https://app.terraform.io/api/v2/organizations/my-org/workspaces \
  -d '{"data":{"type":"workspaces","attributes":{"name":"my-workspace"}}}'
```

**Use Terraform to create workspace:**

```hcl
resource "tfe_workspace" "main" {
  name         = "my-workspace"
  organization = "my-org"
}
```

## Examples

```hcl
terraform {
  cloud {
    workspaces {
      name = "my-workspace"
    }
  }
}
```
"""),

    md("Terraform Cloud Run Failed", "Fix Terraform Cloud run failed errors when a TFC run completes with errors.",
       """## Error Description

TFC run failed errors occur when a remote run fails:

```
Error: Run failed

The run exited with errors. Check the run details in
Terraform Cloud for more information.
```

## Common Causes

- Configuration errors detected during plan.
- Policy check failures.
- Sentinel policy violations.

## How to Fix

**Check run logs via API:**

```bash
curl -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/runs/run-123 | jq '.data.attributes'
```

**Re-trigger run after fixing issues:**

```bash
curl -X POST \
  -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/runs/run-123/actions/confirm \
  -d '{}'
```

## Examples

```bash
curl -H "Authorization: Bearer $TFE_TOKEN" \
  "https://app.terraform.io/api/v2/workspaces/ws-id/runs" | jq '.data[].id'
```
"""),

    md("Terraform Cloud API Error", "Fix Terraform Cloud API errors when TFC API calls fail.",
       """## Error Description

TFC API errors occur when the Terraform Cloud API returns errors:

```
Error: TFC API Error 422: Validation Failed

The request body contains invalid fields.
```

## Common Causes

- Invalid API request format.
- Missing required fields.
- Rate limiting.

## How to Fix

**Check API request format:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  -H "Content-Type: application/vnd.api+json" \
  https://app.terraform.io/api/v2/organizations/my-org/workspaces \
  -d '{"data":{"type":"workspaces","attributes":{"name":"test"}}}' \
  | jq .
```

**Handle rate limiting:**

```bash
# Add delay between requests
sleep 1
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/organizations/my-org | jq '.data.attributes'
```
"""),

    md("Terraform Cloud Token Invalid", "Fix Terraform Cloud token invalid errors when authentication fails.",
       """## Error Description

TFC token invalid errors occur when the API token is not accepted:

```
Error: Unauthorized

The provided API token is invalid or has been revoked.
```

## Common Causes

- Token was revoked.
- Token expired.
- Wrong token for the organization.

## How to Fix

**Re-authenticate:**

```bash
terraform login app.terraform.io
```

**Generate new API token:**

1. Go to Terraform Cloud > User Settings > Tokens
2. Create a new API token
3. Set environment variable:

```bash
export TFE_TOKEN="new-api-token"
```

**Use organization-scoped token:**

```bash
export TFE_TOKEN="atlasv1-xxx"
export TFE_ORG="my-org"
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/users/me | jq '.data.attributes.username'
```
"""),

    md("Terraform Cloud Organization Not Found", "Fix Terraform Cloud organization not found errors when the organization doesn't exist.",
       """## Error Description

TFC organization not found errors occur when referencing a non-existent org:

```
Error: Organization not found

The organization "my-org" does not exist or you do not
have permission to access it.
```

## Common Causes

- Organization name is incorrect.
- Organization was deleted.
- User not a member of the organization.

## How to Fix

**Verify organization name:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/organizations/my-org | jq '.data.attributes.name'
```

**Check organization membership:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/organizations/my-org/users | jq '.data[].attributes.username'
```

## Examples

```hcl
terraform {
  cloud {
    organization = "my-correct-org"
    workspaces {
      name = "my-workspace"
    }
  }
}
```
"""),

    md("Terraform Cloud Policy Check Failed", "Fix Terraform Cloud policy check failed errors when Sentinel policies reject the plan.",
       """## Error Description

Policy check failures occur when Sentinel policies block the run:

```
Error: Policy check failed

The following policies failed:
- enforce-mandatory-tags: Resource missing required tags
```

## Common Causes

- Resource missing required tags.
- Instance type not in allowed list.
- Region restriction violated.

## How to Fix

**Fix the configuration to pass policies:**

```hcl
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Environment = "production"
    Team        = "platform"
    CostCenter  = "12345"
  }
}
```

## Examples

```hcl
tags = {
  Environment = "production"
  ManagedBy   = "terraform"
  CostCenter  = var.cost_center
}
```
"""),

    md("Terraform Cloud Cost Estimation Failed", "Fix Terraform Cloud cost estimation failed errors when cost estimation cannot be calculated.",
       """## Error Description

Cost estimation failures occur when TFC cannot estimate costs:

```
Error: Cost estimation failed

Unable to estimate costs for the given plan. Some resources
may not be supported.
```

## Common Causes

- Provider not supported for cost estimation.
- Custom resources without pricing data.

## How to Fix

**Check cost estimation settings:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/organizations/my-org/cost-estimation | jq '.data.attributes'
```

**Skip cost estimation for unsupported providers:**

```hcl
cost_estimation_enabled = false
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/runs/run-123/cost-estimate | jq '.data.attributes'
```
"""),

    md("Terraform Cloud Run Queue Error", "Fix Terraform Cloud run queue errors when runs are stuck or failing in the queue.",
       """## Error Description

Run queue errors occur when TFC runs are stuck in the queue:

```
Error: Run is pending

The run is waiting to be processed. It may be queued behind
other runs.
```

## Common Causes

- Run queue is full.
- Concurrent run limit reached.

## How to Fix

**Check run queue status:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  "https://app.terraform.io/api/v2/runs?filter[status]=pending" | jq '.data[].id'
```

**Cancel stuck runs:**

```bash
curl -X POST \
  -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/runs/run-123/actions/cancel \
  -d '{}'
```

**Increase concurrency limit:**

```bash
curl -X PATCH \
  -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/organizations/my-org \
  -d '{"data":{"attributes":{"concurrency":10}}}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  "https://app.terraform.io/api/v2/workspaces/ws-id/runs" | jq '.data[].attributes.status'
```
"""),

    md("Terraform Cloud OAuth Token Error", "Fix Terraform Cloud OAuth token errors when VCS integration fails.",
       """## Error Description

OAuth token errors occur when TFC cannot authenticate with the VCS:

```
Error: OAuth token error

The OAuth token for VCS connection is invalid or expired.
```

## Common Causes

- OAuth token was revoked on VCS side.
- VCS app permissions changed.

## How to Fix

**Re-create OAuth token:**

1. Go to Terraform Cloud > Organization Settings > VCS Providers
2. Remove old connection
3. Create new OAuth token

**Update workspace VCS connection:**

```bash
curl -X PATCH \
  -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/workspaces/ws-id \
  -d '{"data":{"relationships":{"oauth-token":{"data":{"type":"oauth-tokens","id":"ot-new-id"}}}}}'
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/organizations/my-org/oauth-tokens | jq '.data[].id'
```
"""),

    md("Terraform Cloud Agent Not Connected", "Fix Terraform Cloud agent not connected errors when the remote agent is offline.",
       """## Error Description

Agent not connected errors occur when TFC agent pool is unreachable:

```
Error: Agent pool not connected

The agent pool "my-pool" has no connected agents. Runs will
be queued until an agent becomes available.
```

## Common Causes

- Agent process stopped on the machine.
- Network connectivity issue.
- Agent token expired.

## How to Fix

**Check agent status:**

```bash
# On the agent machine
ps aux | grep terraform-agent
```

**Restart the agent:**

```bash
# Using systemd
sudo systemctl restart terraform-agent

# Or run directly
terraform-agent run --token $AGENT_TOKEN
```

**Verify agent is registered:**

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/agent-pools/pool-id/agents | jq '.data[].attributes'
```

## Examples

```bash
curl -s -H "Authorization: Bearer $TFE_TOKEN" \
  https://app.terraform.io/api/v2/agent-pools/pool-id/agents \
  | jq '.data[] | {id: .id, status: .attributes.status, last_ping: .attributes.last-ping-at}'
```
"""),

    # =========================================================================
    # 13. CLI ERRORS
    # =========================================================================
    md("Terraform Command Not Found", "Fix Terraform command not found errors when the terraform binary is not in PATH.",
       """## Error Description

Command not found errors occur when the `terraform` binary is not accessible:

```
bash: terraform: command not found
```

## Common Causes

- Terraform not installed.
- Binary not in PATH.

## How to Fix

**Install Terraform:**

```bash
# Using tfenv
git clone https://github.com/tfutils/tfenv.git ~/.tfenv
ln -s ~/.tfenv/bin/* /usr/local/bin/
tfenv install latest
tfenv use latest
```

**Verify PATH:**

```bash
which terraform
echo $PATH
```

**Add to PATH:**

```bash
export PATH="$PATH:/opt/terraform"
echo 'export PATH="$PATH:/opt/terraform"' >> ~/.bashrc
```

## Examples

```bash
terraform version
find / -name terraform -type f 2>/dev/null
```
"""),

    md("Terraform Missing Required Flag", "Fix Terraform missing required flag errors when a mandatory flag is not provided.",
       """## Error Description

Missing required flag errors occur when a command requires a flag that's not provided:

```
Error: Required flag not provided

The "-var" flag is required when using "-var-file".
```

## Common Causes

- Forgot to include required flag.
- Script doesn't pass all required flags.

## How to Fix

**Add the required flag:**

```bash
terraform apply -var="environment=production"
```

**Use variable files:**

```bash
terraform apply -var-file="production.tfvars"
```

**Check flag requirements:**

```bash
terraform plan -help
```

## Examples

```bash
terraform plan -var="env=prod" -out=tfplan
terraform apply -auto-approve -var-file="prod.tfvars"
terraform import aws_instance.web i-12345678
```
"""),

    md("Terraform Invalid Flag", "Fix Terraform invalid flag errors when an unrecognized flag is used.",
       """## Error Description

Invalid flag errors occur when an unrecognized flag is passed:

```
Error: Invalid flag

"-option" is not a valid flag. Did you mean "-out"?
```

## Common Causes

- Typo in flag name.
- Flag from wrong Terraform version.

## How to Fix

**Check available flags:**

```bash
terraform plan -help
```

**Use correct flag syntax:**

```bash
# Correct
terraform plan -out=tfplan

# Wrong
terraform plan -output=tfplan
```

## Examples

```bash
terraform plan -out=tfplan
terraform apply -auto-approve
terraform destroy -target=aws_instance.web
```
"""),

    md("Terraform Working Directory Error", "Fix Terraform working directory errors when terraform is run in the wrong directory.",
       """## Error Description

Working directory errors occur when Terraform can't find configuration:

```
Error: No configuration files found

No .tf files are present in the current working directory.
```

## Common Causes

- Not in the correct directory.
- Configuration files in a subdirectory.

## How to Fix

**Navigate to the correct directory:**

```bash
cd /path/to/terraform/config
terraform plan
```

**Use the `-chdir` flag:**

```bash
terraform -chdir=/path/to/config plan
```

**Check current directory:**

```bash
pwd
ls *.tf
```

## Examples

```bash
ls -la *.tf
terraform -chdir=./environments/prod plan
```
"""),

    md("Terraform Hook Error", "Fix Terraform hook errors when pre-commit or hook scripts fail.",
       """## Error Description

Hook errors occur when pre-commit hooks or hook scripts fail:

```
Error: Hook pre-commit failed

The pre-commit hook exited with status 1.
```

## Common Causes

- Hook script has errors.
- Required tools not installed.
- Configuration validation fails.

## How to Fix

**Check hook script:**

```bash
cat .git/hooks/pre-commit
```

**Run hook manually:**

```bash
pre-commit run --all-files
```

**Skip hooks temporarily:**

```bash
git commit --no-verify -m "message"
```

**Install required tools:**

```bash
# tflint
brew install tflint

# tfsec
brew install tfsec
```

## Examples

```bash
# Install pre-commit hooks
pre-commit install

# Run all hooks
pre-commit run --all-files

# Skip specific hook
SKIP=terraform_validate git commit -m "message"
```
"""),

    md("Terraform Init Upgrade Error", "Fix Terraform init upgrade errors when upgrading providers or modules fails.",
       """## Error Description

Init upgrade errors occur when upgrading dependencies during init:

```
Error: Failed to install provider

Error: could not download provider hashicorp/aws version 5.0.0
```

## Common Causes

- Network issues during download.
- Provider version no longer available.
- Corrupted cache.

## How to Fix

**Clear cache and retry:**

```bash
rm -rf .terraform/
terraform init -upgrade
```

**Force re-download:**

```bash
terraform init -upgrade -force-copy
```

**Check provider availability:**

```bash
curl -s "https://registry.terraform.io/v1/providers/hashicorp/aws/versions" | jq '.versions[].version' | head -5
```

## Examples

```bash
# Clean init
rm -rf .terraform .terraform.lock.hcl
terraform init -upgrade

# Verify providers installed
terraform providers
```
"""),

    md("Terraform Force Copy Warning", "Fix Terraform force copy warning when backend configuration changes require state migration.",
       """## Error Description

Force copy warnings occur when backend configuration changes:

```
Terraform has detected that the configuration specified for the
backend has changed, which may result in data being lost or
moved. Would you like to copy the existing state to the new backend?
```

## Common Causes

- Backend configuration changed.
- Moving from local to remote backend.
- Changing S3 bucket or key.

## How to Fix

**Review the changes carefully:**

```bash
terraform init -migrate-state
```

**Force copy if intentional:**

```bash
terraform init -migrate-state -force-copy
```

**Backup first:**

```bash
terraform state pull > state-backup.json
```

## Examples

```bash
# Safe migration workflow
terraform state pull > backup.json
terraform init -migrate-state
# Verify state
terraform state list
```
"""),

    md("Terraform Import Id Required", "Fix Terraform import id required errors when the resource ID is not provided.",
       """## Error Description

Import ID required errors occur when importing without specifying the ID:

```
Error: Required argument missing

To import a resource, you must provide the resource ID.
```

## Common Causes

- Forgot to specify resource ID in import command.
- Import syntax is wrong.

## How to Fix

**Provide the correct ID:**

```bash
terraform import aws_instance.web i-0123456789abcdef0
```

**Import with module path:**

```bash
terraform import module.vpc.aws_vpc.main vpc-abc123
```

**Check resource ID first:**

```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].{ID:InstanceId,Name:Tags[?Key==`Name`].Value|[0]}' --output table
```

## Examples

```bash
# Import EC2 instance
terraform import aws_instance.web i-0123456789abcdef0

# Import S3 bucket
terraform import aws_s3_bucket.main my-bucket-name

# Import with module
terraform import module.vpc.aws_vpc.main vpc-abc123
```
"""),

    md("Terraform Refresh Only Flag", "Fix Terraform refresh only flag errors when using -refresh-only mode incorrectly.",
       """## Error Description

Refresh only mode errors occur when the flag is misused:

```
Error: -refresh-only is not supported with this command

The -refresh-only flag can only be used with "terraform plan".
```

## Common Causes

- Used `-refresh-only` with wrong command.
- Used with `apply` instead of `plan`.

## How to Fix

**Use with plan only:**

```bash
terraform plan -refresh-only
```

**Review changes:**

```bash
terraform plan -refresh-only -detailed-exitcode
```

**Apply the refresh:**

```bash
terraform apply -refresh-only
```

## Examples

```bash
# Detect drift
terraform plan -refresh-only

# Apply drift detection
terraform apply -refresh-only

# Check exit code
terraform plan -refresh-only -detailed-exitcode
```
"""),

    md("Terraform Validate Warning As Error", "Fix Terraform validate warning as error when warnings are treated as errors in CI/CD.",
       """## Error Description

Validate warning as error occurs when CI/CD fails on warnings:

```
Warning: Value for undeclared variable

Variable "unused_var" is not declared. It will be ignored.

Error: warnings treated as errors
```

## Common Causes

- CI/CD configured to fail on warnings.
- Warnings from legacy configurations.

## How to Fix

**Fix the warnings:**

```bash
# Remove unused variables from variables.tf
# Or add them to usage
```

**Configure CI/CD to allow warnings:**

```yaml
# GitHub Actions
- name: Terraform Validate
  run: terraform validate
  continue-on-error: true
```

**Use `-json` for structured output:**

```bash
terraform validate -json | jq '.diagnostics[] | select(.severity == "warning")'
```

## Examples

```bash
# Ignore warnings in CI
terraform validate 2>&1 | grep -v "Warning:"

# Or use -no-color for machine parsing
terraform validate -no-color 2>&1 | tee validate-output.txt
```
"""),

]

count = 0
for title, desc, body in PAGES:
    # Create slug from title
    slug_name = title.lower().replace(" ", "-").replace("_", "-")
    slug_name = slug_name.replace("'", "").replace('"', '').replace("(", "").replace(")", "")
    # Remove the word "terraform " from start if present (we'll add our own prefix)
    for prefix in ["terraform-", "terraform "] :
        if slug_name.startswith(prefix):
            slug_name = slug_name[len(prefix):]
    slug_name = f"terraform-{slug_name}"
    
    if slug_name in EXISTING:
        print(f"SKIP (exists): {slug_name}")
        continue
    
    content = make_page(title, desc, body)
    path = os.path.join(BASE, f"{slug_name}.md")
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug_name}")

print(f"\nTotal created: {count}")
print(f"Total skipped (existing): {len(PAGES) - count}")
