---
title: "[Solution] npm ERR ERESOLVE — Dependency Resolution Failed"
description: "Fix npm ERR ERESOLVE when dependency resolution fails. Understand peer dependency conflicts and use npm overrides."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# npm ERR ERESOLVE

This error appears when npm cannot satisfy the dependency requirements of multiple packages.

## Workarounds

```json
// package.json overrides
{
  "overrides": {
    "old-package": "1.2.3"
  }
}
```

Or use `--legacy-peer-deps` in your CI pipeline.
