---
title: "[Solution] Netlify Deploy Timeout Error"
description: "Fix Netlify deploy timeout errors when site deployment exceeds the maximum allowed time."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Netlify deploy times out when the deployment process takes longer than the allowed time limit.

## Common Causes

- Very large site with many files
- Slow build command or postprocessing
- Network issues during file upload
- Exceeding deploy size limits
- Heavy asset optimization during deploy

## How to Fix

- Reduce the number of files in the publish directory
- Optimize build commands to run faster
- Use .netlifyignore to exclude unnecessary files
- Split large deploys into smaller functions

## Examples

```gitignore
# .netlifyignore
node_modules
.git
*.log
.env
```

```toml
# netlify.toml - skip heavy processing
[build]
  command = "npm run build"
  publish = "dist"

[build.environment]
  NODE_VERSION = "18"
```

Check deploy size:

```bash
npx netlify-cli deploy --dir=dist --dry-run
```
