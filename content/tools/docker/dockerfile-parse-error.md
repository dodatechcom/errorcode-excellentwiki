---
title: "[Solution] Docker Dockerfile Parse Error — Dockerfile parse error"
description: "Fix Docker Dockerfile parse error. Resolve syntax issues in Dockerfile instructions."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 4
---

# dockerfile parse error

This error occurs when Docker cannot parse the Dockerfile due to syntax errors. The Dockerfile format is strict and small mistakes can cause parse failures.

## Common Causes

- Unclosed quotes in RUN or CMD instructions
- Invalid escape characters
- Missing newline at end of file
- Invalid instruction keyword
- Incorrect line continuation with backslash
- Tabs vs spaces in commands

## How to Fix

### Validate Dockerfile Syntax

```bash
docker build --check .
# or with hadolint
hadolint Dockerfile
```

### Common Syntax Rules

```dockerfile
# Each instruction must be uppercase (convention)
FROM ubuntu:20.04

# Line continuation with backslash
RUN apt-get update &&     apt-get install -y curl

# Multi-line command
RUN echo "line 1" &&     echo "line 2"

# Proper quoting
CMD ["python", "app.py"]
```

### Check for Hidden Characters

```bash
file Dockerfile
cat -A Dockerfile
```

### Use Hadolint for Validation

```bash
docker run --rm -i hadolint/hadolint < Dockerfile
```

## Examples

```bash
# Example 1: Missing backslash
RUN apt-get update
RUN apt-get install -y curl
# Fix: combine with && and backslash

# Example 2: Wrong CMD format
CMD python app.py
# Fix: CMD ["python", "app.py"]

# Example 3: Check file encoding
file Dockerfile
# Dockerfile: UTF-8 Unicode text
```

## Related Errors

- [Invalid reference format]({{< relref "/tools/docker/invalid-reference-format" >}}) — related error
- [Build failed]({{< relref "/tools/docker/build-failed2" >}}) — related error
