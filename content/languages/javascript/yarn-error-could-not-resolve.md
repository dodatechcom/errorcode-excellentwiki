---
title: "[Solution] Yarn Error — Could Not Resolve Dependency Fix"
description: "Fix Yarn resolution errors when packages cannot be found or version conflicts exist."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Yarn Could Not Resolve

```bash
# Check resolution
yarn why <package>

# Use resolutions to override
yarn config set resolutions.package-name version -H
```

Or in package.json:

```json
{
  "resolutions": {
    "old-package": "new-version"
  }
}
```
