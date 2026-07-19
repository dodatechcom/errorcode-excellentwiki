---
title: "[Solution] EMFILE — Too Many Open Files Error in Node.js"
description: "Fix EMFILE when Node.js hits the OS limit for open file descriptors. Increase ulimit and use graceful-fs."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# EMFILE — Too Many Open Files

The OS limit on open file descriptors is reached.

## Fix

```bash
# Check current limit
ulimit -n

# Increase (temporary)
ulimit -n 10240

# Permanent: edit /etc/security/limits.conf
# * soft nofile 65536
# * hard nofile 65536
```

In code, use `graceful-fs` as a drop-in replacement:

```javascript
const fs = require('graceful-fs').gracefulify(require('fs'));
```
