---
title: "[Solution] Yarn Error — Peer Dependency Resolution Failed"
description: "Fix Yarn peer dependency resolution errors with --ignore-peer-deps or resolutions field in package.json."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Yarn Peer Dependency Error

Yarn can fail when peer dependencies conflict.

## Fixes

```bash
# Yarn 1
yarn install --ignore-peer-deps

# Yarn Berry (2+)
yarn config set peerDependencyRules.ignore '*' -H
```

Or add to package.json:

```json
{ "resolutions": { "problem-package": "version" } }
```
