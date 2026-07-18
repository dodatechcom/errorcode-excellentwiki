---
title: "[Solution] GitLab CI YAML Error"
description: "Fix GitLab CI yaml errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI YAML Error

YAML errors in `.gitlab-ci.yml` prevent the pipeline from loading entirely. Common issues include syntax errors, incorrect indentation, duplicate keys, and wrong value types. These errors are caught before any jobs run, making the pipeline appear to not exist.

## Why This Happens

- Syntax error in YAML (missing colons, unclosed brackets)
- Incorrect indentation (GitLab CI requires consistent 2-space indentation)
- Duplicate keys at the same level (silently uses last value)
- Wrong value types (strings vs numbers vs booleans vs lists)
- Special characters not properly quoted

## Common Error Messages

- `yaml_syntax_error: could not parse YAML`
- `yaml_indentation_error: unexpected indentation`
- `yaml_duplicate_key: duplicate key found`
- `yaml_invalid_value: invalid value type`

## How to Fix It

### Solution 1: Validate with yamllint before pushing

Install and run yamllint to catch syntax issues:

```bash
pip install yamllint
yamllint .gitlab-ci.yml
```

Fix all reported issues including trailing whitespace, missing document markers, and incorrect indentation levels. You can also add a `.yamllint` configuration file to customize rules.

### Solution 2: Check indentation consistency

GitLab CI YAML requires consistent 2-space indentation:

```yaml
# Correct
build_job:
  stage: build
  script:
    - make build
    - make test

# Wrong - inconsistent indentation
test_job:
stage: test  # Missing indentation
  script:
    - make test
```

Use a YAML-aware editor like VS Code with the YAML extension to catch indentation errors automatically.

### Solution 3: Remove duplicate keys

YAML does not allow duplicate keys at the same level. The last value silently wins:

```yaml
# Wrong - duplicate 'script' key
test_job:
  script: echo "first"
  script: echo "second"  # This wins silently

# Correct
test_job:
  script:
    - echo "first"
    - echo "second"
```

Search your YAML files for duplicate keys and merge them into lists.

### Solution 4: Quote values that need to be strings

Some keys require specific types. Quote values that should be strings but look like numbers or booleans:

```yaml
variables:
  PORT: "8080"  # Quoted as string
  ENABLED: "true"  # Quoted as string
  COUNT: "42"  # Quoted as string
```

Without quotes, YAML may interpret `8080` as a number and `true` as a boolean.


## Common Scenarios

- **YAML parses correctly but CI lint shows errors:** Use the GitLab CI Lint API to get detailed validation errors beyond basic YAML syntax.
- **Unexpected character at specific line:** Check for tabs (use spaces only), trailing whitespace, or unprintable special characters in the file.

## Prevent It

- Always validate `.gitlab-ci.yml` with GitLab CI Lint before pushing
- Use 2-space indentation consistently throughout the file
- Enable YAML syntax highlighting in your editor to catch errors early
