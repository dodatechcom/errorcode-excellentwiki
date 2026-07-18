---
title: "[Solution] GitLab CI Lint Error"
description: "Fix GitLab CI lint errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Lint Error

Lint errors occur when configuration validation fails before execution.

## Why This Happens

- Syntax error
- Invalid rule
- Undefined variable
- Include not found

## Common Error Messages

- `lint_syntax_error`
- `lint_rule_error`
- `lint_variable_error`
- `lint_include_error`

## How to Fix It

### Solution 1: Run CI Lint

Use the API or UI to validate:

```bash
curl --request POST --header "PRIVATE-TOKEN: $TOKEN" \
  --data @.gitlab-ci.yml \
  "https://gitlab.example.com/api/v4/ci/lint"
```

### Solution 2: Fix deprecated syntax

Migrate from only/except to rules:

```yaml
# Replace
only:
  - main
# With
rules:
  - if: $CI_COMMIT_BRANCH == "main"
```

### Solution 3: Add a lint job

Validate changes in CI:

```yaml
lint:
  stage: test
  script:
    - yamllint .gitlab-ci.yml
```


## Common Scenarios

- **Replace deprecated syntax:** Migrate from only/except to rules.
- **Include not found:** Verify file paths are correct.

## Prevent It

- Always run CI Lint first
- Use API for automation
- Stay current with deprecations
