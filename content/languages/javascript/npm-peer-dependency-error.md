---
title: "[Solution] npm Peer Dependency Error — ERESOLVE Unable to Resolve Dependency Tree"
description: "Fix npm ERESOLVE unable to resolve dependency tree. Use --legacy-peer-deps, --force, or update conflicting packages."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# npm Peer Dependency ERESOLVE Error

npm cannot automatically resolve peer dependency conflicts.

## Fixes

```bash
# Option 1: legacy peer deps
npm install --legacy-peer-deps

# Option 2: force install
npm install --force

# Option 3: check the conflict
npm ls
```

## Preventing It

Keep dependencies updated and avoid deeply nested dependency trees.
