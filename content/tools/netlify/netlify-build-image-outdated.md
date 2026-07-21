---
title: "[Solution] Netlify Build Image Outdated Error"
description: "Fix Netlify build image outdated errors when the build environment uses an old Node or Ubuntu version."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["error"]
---

# Netlify Build Image Outdated Error

Netlify build fails because the build image uses an outdated runtime version.

```
Build image is outdated and no longer supported
```

## Common Causes

- Using deprecated build image version
- Node.js version not supported by build image
- Ubuntu version in build image is EOL
- Build plugins require newer image features
- Environment variables reference old paths

## How to Fix

### Configure Build Image in netlify.toml

```toml
[build]
  # Use the latest build image
  image = "ubuntu20"
```

### Check Current Build Image

```bash
# In build script
cat /etc/os-release
node --version
python3 --version
```

### Use Environment Variables

```toml
[build.environment]
  NODE_VERSION = "18"
  NPM_VERSION = "9"
```

### Update Build Command

```toml
[build]
  command = "npm ci && npm run build"
  publish = "dist"
```

### Migrate from Deprecated Image

```toml
# Old (deprecated)
# image = "ubuntu-xenial"

# New (supported)
[build]
  image = "ubuntu20"
```

## Examples

```toml
# Complete netlify.toml with modern build image
[build]
  image = "ubuntu20"
  command = "npm ci && npm run build"
  publish = ".next"

[build.environment]
  NODE_VERSION = "20"
  NEXT_TELEMETRY_DISABLED = "1"
```
