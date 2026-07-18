---
title: "[Solution] GitLab CI Extends Error"
description: "Fix GitLab CI extends errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Extends Error

Extends errors occur when template inheritance chains are broken or circular.

## Why This Happens

- Template not defined
- Infinite extends loop
- Key conflict
- Depth too deep

## Common Error Messages

- `extends_not_found`
- `extends_infinite_loop`
- `extends_key_conflict`
- `extends_depth_error`

## How to Fix It

### Solution 1: Verify template exists

Template names must start with a dot and be defined before use.

### Solution 2: Fix circular extends

Ensure the extends chain has a finite depth. Check with `gitlab-ci-lint`.

### Solution 3: Override keys properly

Use the `!reference` tag for complex overrides:

```yaml
.test:
  script: echo test
my_job:
  extends: .test
  script: !reference [.test, script]
```


## Common Scenarios

- **Template not found:** Define the template with a dot prefix before using it.
- **Infinite loop:** Check the extends chain for circular references.

## Prevent It

- Use .template_name format
- Document chains
- Avoid deep inheritance
