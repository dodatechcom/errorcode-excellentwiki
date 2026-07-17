---
title: "[Solution] Node.js ENOSPC: system limit reached Error Fix"
description: "Fix Node.js ENOSPC: no space left on device or system limit reached. Resolve disk full, inotify limit, and file watcher issues."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["enospc", "disk-full", "inotify", "file-watcher", "system-limit"]
weight: 5
---

# Node.js ENOSPC — system limit reached

This error occurs when the system runs out of disk space, inotify watch limits, or other OS-level resource limits. It is common during development with file watchers.

## What This Error Means

Common error messages:

- `Error: ENOSPC: system limit reached`
- `Error: ENOSPC: no space left on device`
- `ENOSPC: System limit for number of file watchers reached`

The `ENOSPC` code means "Error NO SPaCe" — the system has exhausted its available resources.

## Common Causes

```javascript
// Cause 1: Disk full — writing files when disk is at capacity
const fs = require('fs');
fs.writeFileSync('/full-disk/file.txt', data); // ENOSPC

// Cause 2: Too many file watchers (common with webpack/vite)
// Error: ENOSPC: System limit for number of file watchers reached

// Cause 3: /tmp partition full
// Node.js uses /tmp for temp files

// Cause 4: Docker container storage limit reached
```

## How to Fix

### Fix 1: Increase inotify watch limit (Linux)

```bash
# Check current limit
cat /proc/sys/fs/inotify/max_user_watches

# Increase temporarily
sudo sysctl fs.inotify.max_user_watches=524288

# Make permanent
echo "fs.inotify.max_user_watches=524288" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

### Fix 2: Free disk space

```bash
# Check disk usage
df -h

# Find large files
du -sh /tmp/* | sort -rh | head

# Clean npm cache
npm cache clean --force

# Remove old node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Fix 3: Reduce file watchers in webpack/vite

```javascript
// webpack.config.js
module.exports = {
  watchOptions: {
    ignored: /node_modules/,
    aggregateTimeout: 300,
    poll: 1000,
  },
};

// vite.config.js
export default {
  server: {
    watch: {
      ignored: ['**/node_modules/**'],
    },
  },
};
```

### Fix 4: Use chokidar with fewer watchers

```javascript
const chokidar = require('chokidar');

const watcher = chokidar.watch('src/**/*', {
  ignored: /node_modules/,
  persistent: true,
  ignoreInitial: true,
  depth: 5, // limit directory depth
});

watcher.on('change', (path) => {
  console.log(`File changed: ${path}`);
});
```

## Examples

```javascript
// This triggers ENOSPC
const fs = require('fs');

try {
  for (let i = 0; i < 100000; i++) {
    fs.writeFileSync(`/tmp/test-${i}.txt`, 'data');
  }
} catch (err) {
  console.error(err.code); // "ENOSPC"
}
```

## Related Errors

- [EACCES Permission Denied]({{< relref "/languages/javascript/eacces-npm" >}}) — permission denied error
- [ERR_FILE_TOO_LARGE]({{< relref "/languages/javascript/err_file_too_large" >}}) — file exceeds size limit
- [ENOENT]({{< relref "/languages/javascript/enoent-node" >}}) — file not found
