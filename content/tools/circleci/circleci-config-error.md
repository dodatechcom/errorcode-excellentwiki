---
title: "[Solution] CircleCI Config Error"
description: "Fix CircleCI config errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Config Error

CircleCI config errors occur when the .circleci/config.yml file has syntax or structural issues.

## Why This Happens

- YAML syntax error
- Missing required fields
- Invalid version
- Duplicate keys

## Common Error Messages

- `config_syntax_error`
- `config_missing_field`
- `config_invalid_version`
- `config_duplicate_key`

## How to Fix It

### Solution 1: Validate with CLI

Run `circleci config validate` to catch syntax errors.

### Solution 2: Use config.process

Preview the processed config:

```bash
circleci config process .circleci/config.yml
```

### Solution 3: Check config version

Ensure you're using version 2.1:

```yaml
version: 2.1
```


## Common Scenarios

- **Validation passes but pipeline fails:** Check for runtime errors not caught by validation.
- **Config not loading:** Verify the file path is exactly `.circleci/config.yml`.

## Prevent It

- Always validate before pushing
- Use version 2.1
- Enable YAML highlighting
