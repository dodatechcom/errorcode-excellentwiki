---
title: "[Solution] ERR_DLOPN_NOT_SUPPORTED — Dynamic Linking Not Supported Fix"
description: "Fix ERR_DLOPN_NOT_SUPPORTED when trying to load native addons on unsupported platforms."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_DLOPN Not Supported

The platform doesn't support dynamic linking of native addons.

## Causes

- Running in Deno/Bun without native addon support
- WebAssembly target
- Browser environment

## Fix

```bash
# Rebuild native modules for current platform
npm rebuild

# Or install platform-specific package
npm install @anthropic-ai/sdk-linux-x64
```
