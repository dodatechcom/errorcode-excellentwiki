---
title: "[Solution] npm Cannot Find Module — Global Installation Fix"
description: "Fix 'cannot find module' for globally installed npm packages. Check PATH, use npx, and verify installation."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# npm Cannot Find Module — Global

When a globally installed package cannot be found after installation.

## Fixes

```bash
# Verify global prefix
npm prefix -g

# Add to PATH
export PATH="/home/admin1/.nvm/versions/node/v22.23.1/bin:/home/admin1/.nvm/versions/node/v22.23.1/bin:/home/admin1/.cargo/bin:/home/admin1/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/admin1/.fzf/bin"

# Or use npx
npx <command>
```
