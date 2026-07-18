---
title: "[Solution] Python Checkov IaC Scanning Error — How to Fix"
description: "Fix Python Checkov IaC scanning errors. Resolve configuration, framework, and suppression issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Checkov IaC Scanning Error

A `checkov.common.errors` or `checkov.terraform` occurs when Checkov fails to scan infrastructure code, encounters invalid configuration, or when framework detection fails.

## Why It Happens

Checkov scans Infrastructure as Code for misconfigurations. Errors arise when the scan directory is empty, when framework files are not detected, when check suppressions are invalid, or when the output format is unsupported.

## Common Error Messages

- `error: No IaC files found`
- `checkov.terraform.TerraformParser: failed to parse`
- `error: Check not found`
- `Warning: 20 misconfigurations found`

## How to Fix It

### Fix 1: Scan correctly

```bash
# Wrong — no directory specified
# checkov

# Correct — specify directory
checkov -d terraform/
checkov -d .
checkov -f main.tf
```

### Fix 2: Configure checks

```bash
# Skip specific checks
checkov -d . --check CKV_AWS_18

# Skip check type
checkov -d . --skip-check terraform

# Run specific framework
checkov -d . --framework terraform
```

### Fix 3: Handle suppressions

```python
# terraform.tf
resource "aws_s3_bucket" "example" {
  #checkov:skip=CKV_AWS_18:Skipping for development
  bucket = "my-bucket"
}
```

### Fix 4: Generate reports

```bash
# JSON output
checkov -d . --output json --output-file result.json

# SARIF for GitHub
checkov -d . --output sarif

# CLI output
checkov -d . --output cli
```

## Common Scenarios

- **No IaC files found** — Directory does not contain Terraform, CloudFormation, or Kubernetes files.
- **Parse error** — Invalid HCL or YAML syntax in IaC files.
- **Check not found** — Check ID does not exist in the current version.

## Prevent It

- Always run `checkov -d .` in CI/CD pipelines before deploying infrastructure.
- Use `--check` to focus on specific security checks.
- Document suppressions with `#checkov:skip` comments.

## Related Errors

- [CheckovError](/languages/python/checkov-error/) — scan failed
- [ParseError](/languages/python/parse-error/) — IaC file parse error
- [CheckNotFound](/languages/python/check-not-found/) — check ID not found
