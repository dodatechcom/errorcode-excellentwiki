---
title: "[Solution] npm package-lock.json Conflict — Merge Conflict Fix"
description: "Fix npm lock file merge conflicts. Regenerate package-lock.json after resolving conflicts."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# npm Lock File Conflict

```bash
# Option 1: Accept theirs and reinstall
git checkout --theirs package-lock.json
npm install

# Option 2: Accept ours
git checkout --ours package-lock.json
npm install

# Option 3: Regenerate entirely
rm package-lock.json node_modules
npm install
```

Never manually edit package-lock.json.
