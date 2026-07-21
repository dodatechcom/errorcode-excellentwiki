---
title: "[Solution] CircleCI Config Validation Error"
description: "Fix CircleCI config validation errors when config.yml contains syntax or structural issues that prevent pipeline execution."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Config Validation Error

Configuration validation errors occur when `config.yml` contains syntax mistakes, unsupported keys, or structural issues that prevent CircleCI from processing the pipeline.

## Common Causes

- YAML syntax error (indentation, missing colon, etc.)
- Unknown configuration keys used in the file
- Version mismatch with the `version` key
- Invalid executor or job name references
- Orb version conflicts or syntax errors

## How to Fix

### Solution 1: Validate with the CLI

```bash
# Validate locally before pushing
circleci config validate .circleci/config.yml

# Process config to check for runtime errors
circleci config process .circleci/config.yml
```

### Solution 2: Use the web validator

Navigate to your project in CircleCI and check the **Config Editor** for inline validation errors.

### Solution 3: Fix common YAML issues

```yaml
version: 2.1  # Must be 2.1 for orbs

jobs:
  build:
    docker:
      - image: cimg/node:18.0
    steps:
      - checkout
      - run:
          name: Build
          command: npm run build  # Proper indentation
```

## Examples

```
Error: Invalid config version. Expected '2.1'
Error: Unknown job key 'comand' (did you mean 'command'?)
```

## Prevent It

- Run `circleci config validate` in CI before deploying
- Use an editor with YAML linting
- Keep config.yml simple and well-organized
