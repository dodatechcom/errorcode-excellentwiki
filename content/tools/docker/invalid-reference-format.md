---
title: "[Solution] Docker Invalid Reference Format — invalid reference format"
description: "Fix Docker invalid reference format error. Correct image name and tag syntax."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# invalid reference format

This error occurs when an image name, tag, or reference does not follow Docker's naming convention. The format must be `[registry/]repository[:tag][@digest]`.

## Common Causes

- Extra spaces or special characters in image name
- Incorrect use of uppercase letters
- Missing or malformed tag syntax
- Invalid characters in repository name
- Wrong format for digest references

## How to Fix

### Valid Image Name Format

```
[registry/]repository[:tag][@sha256:digest]
```

Examples:
```bash
nginx
nginx:latest
myregistry.com/myimage:v1.0
myregistry.com/myimage@sha256:abc123def456
library/nginx
```

### Check Image Name Characters

- Use only lowercase letters, numbers, hyphens, underscores, and periods
- No spaces or special characters
- Tag must start with a letter or number

### Validate Dockerfile

```bash
docker build --no-cache -t myimage:latest .
```

## Examples

```bash
# Example 1: Invalid tag
docker run MyImage:latest
# Fix: docker run myimage:latest (lowercase)

# Example 2: Extra space
docker run my image:latest
# Fix: docker run myimage:latest

# Example 3: Invalid digest format
docker pull nginx@sha256:abc
# Fix: docker pull nginx@sha256:abc123def456... (full digest)
```

## Related Errors

- [Dockerfile parse error]({{< relref "/tools/docker/dockerfile-parse-error" >}}) — related error
- [Image not found]({{< relref "/tools/docker/image-not-found-manifest-unknown" >}}) — related error
