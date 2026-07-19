---
title: "[Solution] EACCES — Permission Denied When Creating Directory"
description: "Fix EACCES mkdir errors in Node.js. Ensure parent directories exist and have correct permissions."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# EACCES — Permission Denied on mkdir

Node.js cannot create a directory due to insufficient permissions.

```javascript
const fs = require('fs');

// Will fail if /data is owned by root
fs.mkdirSync('/data/logs', { recursive: true });
```

## Fix

```bash
sudo chown -R admin1 /data
```
