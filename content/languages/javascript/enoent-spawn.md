---
title: "[Solution] ENOENT — No Such File or Directory on Child Process Spawn"
description: "Fix ENOENT when using child_process.spawn(). Verify executable path, use shell option, and check PATH."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ENOENT on Child Process Spawn

The `ENOENT` error during `spawn()` means the executable was not found.

```javascript
const { spawn } = require('child_process');

// Wrong — absolute path missing, shell not used
spawn('my-script.sh');

// Correct — use shell or provide full path
spawn('my-script.sh', [], { shell: true });
```

## Checklist

- Verify executable exists: `which <command>`
- Use `path.join(__dirname, 'script.sh')` for local scripts
- Set `shell: true` for scripts without shebang
