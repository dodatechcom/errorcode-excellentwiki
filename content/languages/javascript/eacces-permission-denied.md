---
title: "[Solution] EACCES — Permission Denied Fix in Node.js"
description: "Fix EACCES permission denied errors when reading/writing files in Node.js. Check file permissions and ownership."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# EACCES — Permission Denied

The system denies access to a file or directory.

## Fixes

```bash
# Check permissions
ls -la /path/to/file

# Fix ownership
sudo chown -R admin1 /path/to/dir

# Fix permissions
chmod 644 /path/to/file
chmod 755 /path/to/dir
```

Avoid running Node.js as root. Use a reverse proxy (nginx) for port 80/443.
