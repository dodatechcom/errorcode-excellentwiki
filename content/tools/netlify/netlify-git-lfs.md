---
title: "[Solution] Netlify Git LFS Error"
description: "Fix Netlify Git LFS errors. Resolve Git Large File Storage issues."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

Netlify Git LFS Error can prevent your application from working correctly.

## Common Causes

- LFS not installed
- File not tracked
- LFS pointer invalid
- Storage limit exceeded

## How to Fix

### Install LFS

```bash
git lfs install
git lfs track "*.psd"
```

