---
title: "[Solution] GitLab CI DAG Circular Dependency"
description: "Fix GitLab CI DAG circular dependency errors when needs-based job relationships create an unresolvable cycle."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
---

# GitLab CI DAG Circular Dependency

DAG circular dependency errors occur when `needs` keyword references create a cycle in the job dependency graph, making execution order impossible to determine.

## Common Causes

- Job A needs Job B and Job B needs Job A
- Indirect cycles through three or more jobs
- Inherited jobs from includes introduce hidden cycles
- Merge of explicit stage ordering with needs-based dependencies

## How to Fix

### Solution 1: Break the cycle with a shared ancestor

```yaml
# Wrong - circular
build_frontend:
  needs: [build_backend]

build_backend:
  needs: [build_frontend]

# Fixed - common ancestor
prepare:
  stage: prepare
  script: ./prepare.sh

build_frontend:
  needs: [prepare]

build_backend:
  needs: [prepare]
```

### Solution 2: Use optional needs

```yaml
job_a:
  needs:
    - job: job_b
      optional: true

job_b:
  needs:
    - job: job_a
      optional: true
```

### Solution 3: Visualize and validate

```bash
# Extract job dependencies
grep -A 5 "needs:" .gitlab-ci.yml
```

## Examples

```
ERROR: Circular dependency detected in pipeline graph
needs reference creates a cycle between 'build' and 'test'
```

## Prevent It

- Review the pipeline graph after adding `needs`
- Use CI Lint to validate before pushing
- Prefer linear dependency chains over complex graphs
