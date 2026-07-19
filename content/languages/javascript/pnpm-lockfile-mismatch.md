---
title: "[Solution] pnpm Lockfile Mismatch — Lock File Out of Sync Fix"
description: "Fix pnpm lockfile mismatch when pnpm-lock.yaml doesn't match package.json."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# pnpm Lockfile Mismatch

```bash
# Regenerate lockfile
rm pnpm-lock.yaml
pnpm install
```

Or:

```bash
pnpm install --force
```
