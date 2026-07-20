---
title: "[Solution] GitHub Actions Download Canceled"
description: "Fix GitHub Actions artifact download canceled errors."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Download canceled errors occur when artifact download is interrupted:

```
Error: Download canceled by user
```

## Common Causes

- User manually canceled the workflow run.
- Network interruption during download.

## How to Fix

**Handle cancellation gracefully:**

```yaml
steps:
  - uses: actions/download-artifact@v4
    if: ${{ !cancelled() }}
    with:
      name: build-output
```

## Examples

```yaml
steps:
  - uses: actions/download-artifact@v4
    continue-on-error: true
    with:
      name: optional-artifact
```
