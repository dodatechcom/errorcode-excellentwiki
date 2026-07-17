---
title: "[Solution] Terraform Module Not Found Error — Fix Source"
description: "Fix Terraform module not found errors. Resolve module source paths, registry access, and version issues with practical solutions."
---

## What This Error Means

The `Module not found` error occurs when Terraform cannot locate a module referenced in your configuration. This happens during `terraform init` when Terraform attempts to download or locate the module source.

A typical error output:

```
Error: Module not found

The module address "modules/vpc" could not be found in the module registry
at registry.terraform.io, and no local source path was found at "./modules/vpc".
```

Or with a remote source:

```
Error: Failed to download module

Could not download module "vpc" (source: "git::https://github.com/org/terraform-modules.git//vpc?ref=v2.0.0")
from git: Error running "git clone": exit status 128
```

## Why It Happens

Module not found errors arise from:

- **Incorrect source path**: Typo in the module `source` attribute or wrong relative path.
- **Missing local module**: The local module directory does not exist at the specified path.
- **Network access issues**: Git, HTTP, or registry endpoints are unreachable from your machine.
- **Authentication failures**: Private modules require credentials that are missing or expired.
- **Ref or version not found**: The specified git tag, branch, or module version does not exist.
- **Registry permissions**: The module is private and your API token lacks access.

## How to Fix It

**Step 1: Verify the module source path**

Check that the path matches your directory structure:

```hcl
module "vpc" {
  source = "../../modules/vpc"  # Verify this path exists
  # ...
}
```

```bash
ls -la ../../modules/vpc/
```

**Step 2: Run init with verbose logging**

Enable detailed output to trace module resolution:

```bash
terraform init -upgrade -log-level=TRACE 2>&1 | grep -i "module"
```

**Step 3: Authenticate for private modules**

For private registries, configure credentials:

```bash
terraform login registry.terraform.io
```

For private Git modules, ensure SSH keys or tokens are configured:

```bash
export GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa"
terraform init
```

**Step 4: Use `terraform get` to download modules**

Download modules without full initialization:

```bash
terraform get -update
```

**Step 5: Pin module versions explicitly**

Always specify a version or ref to avoid resolution failures:

```hcl
module "vpc" {
  source  = "app.terraform.io/org/vpc/aws"
  version = "2.1.0"
}
```

## Common Mistakes

- **Relative path mistakes**: Always verify module paths with `ls` before running `terraform init`.
- **Not running `terraform init -upgrade`**: Stale module caches cause outdated resolution. Use the upgrade flag.
- **Forgetting git ref for private repos**: Private Git modules need valid refs and authentication.
- **Mixing module sources inconsistently**: Pick one source pattern (registry, Git, or local) and stick with it.

## Related Pages

- [Terraform Provider Error](/tools/terraform/terraform-provider-error/) — Provider initialization failures
- [Terraform Validation Error](/tools/terraform/terraform-validation-error/) — Variable validation issues
- [Helm Chart Not Found](/tools/helm/helm-chart-not-found/) — Helm chart resolution errors
