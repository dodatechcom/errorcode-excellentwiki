---
title: "[Solution] GitLab CI Include Depth Limit"
description: "Fix GitLab CI include depth limit errors when nested includes exceed the maximum allowed recursion depth."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI Include Depth Limit

GitLab enforces a maximum include depth (default 10) to prevent infinite recursion. When your configuration uses deeply nested includes, the pipeline fails with a depth limit error.

## Common Causes

- Template files include other templates in a chain
- Circular include references between CI files
- Using `include:local`, `include:template`, and `include:project` in deep hierarchies
- Group-level templates that include project-level templates recursively

## How to Fix

### Solution 1: Flatten include hierarchy

Restructure templates to avoid deep nesting:

```yaml
# Instead of A -> B -> C -> D
# Use flat includes:
include:
  - local: '/.gitlab-ci/build.yml'
  - local: '/.gitlab-ci/test.yml'
  - local: '/.gitlab-ci/deploy.yml'
```

### Solution 2: Increase depth limit

Ask your GitLab administrator to raise the limit in application settings:

```
# /etc/gitlab/gitlab.rb
gitlab_rails['ci_max_includes'] = 20
```

### Solution 3: Remove circular references

Audit your include chain for cycles:

```yaml
# Parent file
include:
  - project: 'devops/ci-templates'
    file: '/shared/build.yml'

# shared/build.yml should NOT include parent or grandparent
```

## Examples

```
Included file `build.yml` exceeds maximum include depth of 10
```

## Prevent It

- Limit include chains to 3-4 levels
- Use `include:component` for reusable logic instead of deep nesting
- Regularly audit include dependencies
