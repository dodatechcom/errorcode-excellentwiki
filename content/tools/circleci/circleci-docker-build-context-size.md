---
title: "[Solution] CircleCI Docker Build Context Size"
description: "Fix CircleCI Docker build context size errors when the build context exceeds the maximum allowed size for Docker builds."
tools: ["circleci"]
error-types: ["tool-error"]
severities: ["error"]
---

# CircleCI Docker Build Context Size

Docker build context size errors occur when the Docker build context sent to the daemon is too large, causing the build to fail or timeout.

## Common Causes

- `.dockerignore` file is missing or incomplete
- Large files like `node_modules`, `.git`, or data files are included
- Build context includes build artifacts from previous steps
- Docker daemon memory is insufficient for the context size

## How to Fix

### Solution 1: Create a comprehensive `.dockerignore`

```
# .dockerignore
.git
node_modules
dist
build
coverage
*.log
.env
.DS_Store
```

### Solution 2: Build from a subdirectory

```yaml
jobs:
  build:
    steps:
      - checkout
      - run: npm run build
      - run:
          name: Build Docker image
          command: |
            cd app
            docker build -t myapp:$CIRCLE_SHA1 .
```

### Solution 3: Use Docker BuildKit

```yaml
jobs:
  build:
    environment:
      DOCKER_BUILDKIT: "1"
    steps:
      - run: docker build --progress=plain .
```

## Examples

```
ERROR: context cancelled: build context too large
ERROR: failed to solve: unable to prepare context: total size exceeds limit
```

## Prevent It

- Always include a `.dockerignore` file
- Review build context size before building
- Use multi-stage builds to reduce final image size
