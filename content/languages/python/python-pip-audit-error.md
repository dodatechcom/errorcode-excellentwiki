---
title: "[Solution] Python pip-audit Error — How to Fix"
description: "Fix Python pip-audit dependency errors. Resolve scanning, fix, and configuration issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python pip-audit Error

A `pip_audit._service.VulnerabilityServiceError` or `pip_audit._fixer.FixerError` occurs when pip-audit fails to scan, encounters network issues, or when the vulnerability database is unreachable.

## Why It Happens

pip-audit checks installed packages for known vulnerabilities. Errors arise when the PyPI JSON API is unavailable, when packages are not properly installed, when the fix command encounters conflicts, or when the output format is invalid.

## Common Error Messages

- `VulnerabilityServiceError: failed to query PyPI`
- `pip_audit._fixer.FixerError: could not fix vulnerability`
- `AuditError: no dependencies found to audit`
- `Warning: found 5 vulnerabilities`

## How to Fix It

### Fix 1: Run audit correctly

```bash
# Wrong — no output format
# pip-audit

# Correct — specify output format
pip-audit --format json
pip-audit --format columns
pip-audit --format cyclonedx
```

### Fix 2: Fix vulnerabilities

```bash
# Audit and fix
pip-audit --fix

# Fix with dry run
pip-audit --fix --dry-run

# Fix specific vulnerability
pip-audit --fix --vulnerability-id 51457
```

### Fix 3: Handle requirements files

```bash
# Audit requirements file
pip-audit -r requirements.txt

# Audit with hashes
pip-audit -r requirements.txt --require-hashes
```

### Fix 4: Configure for CI/CD

```bash
# Fail on vulnerabilities
pip-audit --exit-code

# JSON output for parsing
pip-audit --format json --output audit-results.json

# Ignore specific vulnerabilities
pip-audit --ignore-vulnerability 51457
```

## Common Scenarios

- **Network unavailable** — pip-audit cannot reach PyPI to check vulnerabilities.
- **Package not installed** — Dependency is in requirements but not installed.
- **Fix conflicts** — Automatic fix creates dependency conflicts.

## Prevent It

- Always run `pip-audit` in CI/CD pipelines before deploying.
- Use `--require-hashes` for supply chain security.
- Keep `requirements.txt` updated with pinned versions.

## Related Errors

- [VulnerabilityServiceError](/languages/python/vulnerability-error/) — PyPI query failed
- [FixerError](/languages/python/fixer-error/) — could not fix vulnerability
- [AuditError](/languages/python/audit-error/) — no dependencies found
