---
title: "[Solution] pnpm ERR — No Store Found / Store Error Fix"
description: "Fix pnpm errors related to the content-addressable store. Rebuild store and fix corrupted cache."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# pnpm Store Error

pnpm uses a content-addressable store that can become corrupted.

## Fixes

```bash
# Rebuild the store
pnpm store repair

# Or prune and reinstall
pnpm prune
rm -rf node_modules pnpm-lock.yaml
pnpm install
```
