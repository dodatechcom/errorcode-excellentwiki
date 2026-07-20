---
title: "[Solution] GitHub Actions GPU Minutes Not Available"
description: "Fix GitHub Actions GPU runner minutes not available errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

GPU minutes not available errors occur when GPU runners are not accessible:

```
Error: GPU runner not available for this repository
```

## Common Causes

- GPU runners require special access.
- Organization does not have GPU runners provisioned.

## How to Fix

**Request GPU runner access:**

```yaml
runs-on: [self-hosted, gpu, cuda-12]
```

## Examples

```yaml
runs-on: [self-hosted, gpu, nvidia-a100]
```
