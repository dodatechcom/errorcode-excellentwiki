---
title: "[Solution] Terraform Module Source Not Found Error — How to Fix"
description: "Fix Terraform module source not found errors including private registry access, version constraints, and Git path issues with practical fixes."
comments: true
---

A Terraform module source not found error occurs when Terraform cannot download, locate, or access a module referenced in the configuration. This blocks all operations that depend on the module, including `init`, `plan`, and `apply`.

## Why It Happens

Modules are loaded from various sources (registries, Git repositories, local paths, S3 buckets) and each source type has unique failure modes. Common causes include:

- **Incorrect source path**: A local module path contains a typo, uses an incorrect relative path, or references a directory that does not exist.
- **Private registry access**: The module is hosted on a private registry (Terraform Cloud, GitLab, GitHub Packages) and credentials are missing or expired.
- **Git authentication failure**: A module sourced from a private Git repository cannot be cloned due to missing SSH keys or token authentication.
- **Version constraint not satisfied**: The module exists on the registry but no version matches the constraint specified in the configuration.
- **Network restrictions**: Firewall rules or proxy settings block Terraform from reaching the module source URL.
- **Module not published**: The module has been removed, renamed, or never published to the registry.

## Common Error Messages

**Error: Module not found locally**

```
Error: Failed to download module

Could not find module "modules/vpc" in the following search paths:
  - ./modules/vpc
  - ../modules/vpc

Make sure the module source path is correct relative to the
root module directory.
```

**Error: Private registry authentication failed**

```
Error: Failed to install provider

Error: Error accessing registry.terraform.io

The returned response was: 401 Unauthorized

To sign in, set the credentials for the Terraform Cloud
registry hostname using "terraform login".
```

**Error: No matching module version**

```
Error: Version constraint not satisfied

Module "vpc" (source "app.terraform.io/my-org/vpc/aws") has
no version matching ">= 3.0.0, < 4.0.0".

Available versions: 1.0.0, 1.1.0, 2.0.0, 2.1.0
```

**Error: Git clone failed**

```
Error: Error downloading Git module

error: cannot run ssh: No such file or directory
Failed to clone "git@github.com:org/terraform-modules.git"

Ensure git and ssh are installed and accessible in PATH.
```

## How to Fix It

### Solution 1: Fix local module paths

Ensure local module directories exist and are referenced correctly:

```hcl
# Root module structure
# .
# ├── main.tf
# ├── modules/
# │   ├── vpc/
# │   │   ├── main.tf
# │   │   ├── variables.tf
# │   │   └── outputs.tf
# │   └── ecs/
# │       ├── main.tf
# │       ├── variables.tf
# │       └── outputs.tf
# └── environments/
#     └── prod/
#         └── main.tf

# In environments/prod/main.tf — reference relative to root
module "vpc" {
  source = "../../modules/vpc"

  cidr_block = "10.0.0.0/16"
}

module "ecs" {
  source = "../../modules/ecs"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids
}
```

Verify the path exists:

```bash
# Check module directory exists
ls -la modules/vpc/

# Should contain: main.tf, variables.tf, outputs.tf
```

### Solution 2: Configure private registry access

For Terraform Cloud or private registries, set up authentication:

```bash
# Log in to Terraform Cloud
terraform login app.terraform.io

# Set registry credentials via environment variables
export TF_TOKEN_app_terraform_io="your-api-token"

# For GitLab private registry
export TF_TOKEN_gitlab_com="your-gitlab-token"

# For GitHub Packages
export TF_TOKEN_terraform_github_com="your-github-token"
```

Use a `.terraformrc` credentials file:

```hcl
credentials "app.terraform.io" {
  token = "your-api-token-here"
}
```

### Solution 3: Fix Git source configuration

Ensure Git and SSH are available, and use proper Git source syntax:

```hcl
# GitHub HTTPS (requires token for private repos)
module "vpc" {
  source = "git::https://oauth2:TOKEN@github.com/org/terraform-modules.git//modules/vpc?ref=v2.1.0"
}

# GitHub SSH
module "vpc" {
  source = "git::ssh://git@github.com/org/terraform-modules.git//modules/vpc?ref=v2.1.0"
}

# Bitbucket
module "vpc" {
  source = "git::https://bitbucket.org/org/terraform-modules.git//modules/vpc?ref=v1.0.0"
}
```

Verify Git access:

```bash
# Test SSH access to GitHub
ssh -T git@github.com

# Test HTTPS clone
git ls-remote https://github.com/org/terraform-modules.git

# Check if the ref (branch/tag) exists
git ls-remote --tags https://github.com/org/terraform-modules.git
```

### Solution 4: Adjust version constraints

Update the version constraint to match available module versions:

```hcl
# Too restrictive — no matching version
module "vpc" {
  source  = "app.terraform.io/my-org/vpc/aws"
  version = ">= 3.0.0, < 4.0.0"
}

# More flexible — allows any 2.x version
module "vpc" {
  source  = "app.terraform.io/my-org/vpc/aws"
  version = "~> 2.0"
}

# Latest version (not recommended for production)
module "vpc" {
  source  = "app.terraform.io/my-org/vpc/aws"
  version = ">= 2.0"
}

# Pin to exact version for reproducibility
module "vpc" {
  source  = "app.terraform.io/my-org/vpc/aws"
  version = "2.1.0"
}
```

Check available versions:

```bash
terraform init -backend=false

# Or query the registry API directly
curl -s "https://registry.terraform.io/v1/modules/my-org/vpc/aws" | jq '.versions'
```

## Common Scenarios

**Scenario 1: Module moved or renamed after first init**

A module repository reorganized its directory structure. The `.terraform/modules` cache still references the old path, and `terraform init` fails. Delete the `.terraform` directory and reinitialize.

**Scenario 2: CI/CD pipeline missing module credentials**

A pipeline runs Terraform but the registry credentials are not injected as environment variables. Add the token as a CI/CD secret and export it as `TF_TOKEN_<hostname>`.

**Scenario 3: Module version constraint too tight**

After a module releases breaking changes in v3.0.0, a configuration pins `version = ">= 2.0"`, which allows v3.0.0 and breaks. Use pessimistic constraint `~> 2.0` to stay within minor versions.

## Prevent It

- **Use `terraform init` locally before committing**: Catch module access issues early by running `terraform init` in your development environment.
- **Pin module versions in production**: Always specify exact or `~> x.y` version constraints for production modules.
- **Store module credentials in CI/CD secrets**: Never hardcode registry tokens. Use environment variables and secret management.

## Related Pages

- [Terraform Provider Error](/tools/terraform/terraform-provider-error/) — Provider download failures
- [Terraform Backend Error](/tools/terraform/terraform-backend-error/) — Backend initialization issues
- [Terraform Workspace Error](/tools/terraform/terraform-workspace-error/) — Workspace configuration
