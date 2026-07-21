---
title: "[Solution] GitLab CI YAML Anchor Merge Conflict"
description: "Fix GitLab CI YAML anchor merge conflicts when YAML anchors and aliases produce unexpected merged configurations."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI YAML Anchor Merge Conflict

YAML anchor merge conflicts occur when anchors (`&`) and aliases (`*`) produce unintended merged configurations, overriding or duplicating keys.

## Common Causes

- Anchor defines a key that is also defined in the job
- Merge key (`<<:`) conflicts with explicit key definitions
- Nested anchors create unexpected override chains
- Alias references a non-existent anchor

## How to Fix

### Solution 1: Understand anchor priority

YAML merge gives explicit keys priority over merged keys:

```yaml
.base_config: &base
  image: node:18
  before_script:
    - npm install

build_job:
  <<: *base
  image: node:20  # This overrides the anchor's image
  script:
    - npm run build
```

### Solution 2: Restructure to avoid conflicts

Split shared configuration into distinct anchors:

```yaml
.docker_base: &docker
  image: node:18
  services:
    - docker:24.0-dind

.npm_base: &npm
  before_script:
    - npm ci

build_job:
  <<: [*docker, *npm]
  script:
    - npm run build
```

### Solution 3: Validate with CI Lint

Use the GitLab CI Lint page to verify merged configurations before committing.

## Examples

```
Error in .gitlab-ci.yml: undefined anchor '&base_config'
```

## Prevent It

- Test YAML merge behavior in an online YAML parser
- Keep anchor hierarchies shallow
- Use CI Lint to validate after changes
