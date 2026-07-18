---
title: "[Solution] GitLab CI Rule Error"
description: "Fix GitLab CI rule errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Rule Error

Rule errors occur when rules conditions prevent jobs from running unexpectedly.

## Why This Happens

- Deprecated only/except syntax
- Rule syntax invalid
- Rules never match
- Conflicting rules

## Common Error Messages

- `rule_syntax_error`
- `rule_not_matching`
- `rule_conflict`
- `rule_evaluation_error`

## How to Fix It

### Solution 1: Fix conflicts

First matching rule wins. Place specific rules before general ones.

### Solution 2: Migrate from only/except

Replace deprecated syntax:

```yaml
# Old (deprecated)
deploy:
  only:
    - main
# New
rules:
  - if: $CI_COMMIT_BRANCH == "main"
```

### Solution 3: Test with CI simulator

Use the CI/CD > Pipelines > CI Simulator to test rules.


## Common Scenarios

- **Uses deprecated syntax:** Migrate from only/except to rules.
- **Rules evaluation:** Use `rules:when: on_success` as default behavior.

## Prevent It

- Use rules instead of only/except
- Test with CI Simulator
- Place specific rules first
