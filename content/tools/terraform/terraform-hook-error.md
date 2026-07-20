---
title: "[Solution] Terraform Hook Error"
description: "Fix Terraform hook errors when pre-commit or hook scripts fail."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

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
