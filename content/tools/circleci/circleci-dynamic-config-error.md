---
title: "[Solution] CircleCI Dynamic Config Error"
description: "Fix CircleCI dynamic config errors. Learn why this happens and how to resolve it quickly."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# CircleCI Dynamic Config Error

Dynamic config errors occur when setup workflows or dynamic configuration fails.

## Why This Happens

- Setup workflow error
- Continuation failed
- Parameter missing
- Config generation failed

## Common Error Messages

- `dynamic_config_error`
- `continuation_error`
- `parameter_error`
- `config_generation_error`

## How to Fix It

### Solution 1: Enable dynamic config

Add setup: true to your workflow:

```yaml
workflows:
  setup:
    when: setup
    jobs:
      - generate-config
```

### Solution 2: Use continuation

Continue with generated config:

```yaml
- continuation:
    configuration-path: generated-config.yml
```

### Solution 3: Pass parameters

Use pipeline parameters:

```yaml
parameters:
  run-integration:
    type: boolean
    default: false
```


## Common Scenarios

- **Continuation failed:** Verify the generated config is valid.
- **Parameter missing:** Ensure all parameters are defined.

## Prevent It

- Enable setup workflows
- Validate generated config
- Document parameters
