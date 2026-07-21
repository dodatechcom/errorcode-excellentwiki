---
title: "Docker Compose Build Error"
description: "Docker Compose build process fails during image construction"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Docker Compose Build Error

Docker Compose build process fails during image construction

## Common Causes

- Dockerfile syntax error or invalid instruction
- Base image not found or pull failed
- Build context too large or .dockerignore misconfigured
- COPY/ADD referencing files not in build context

## How to Fix

1. Check Dockerfile syntax: `docker build -t test .`
2. View build output: `docker-compose build --no-cache`
3. Verify .dockerignore excludes unnecessary files
4. Check base image availability: `docker pull <base-image>`

## Examples

```bash
# Build with no cache
docker-compose build --no-cache

# Check Dockerfile for errors
docker build --check .

# Verify base image
docker pull ubuntu:22.04
```
